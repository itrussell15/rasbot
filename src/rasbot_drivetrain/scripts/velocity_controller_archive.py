#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

from rasbot_msgs.msg import DriveMsg

import numpy as np


class VelocityController:

    def __init__(self, init_accels: Vector3, rate: int = 5):

        self._target_twist = Twist()
        self._actual_twist = Twist()

        self._accel_values = init_accels

        rospy.init_node("drive_speed_controller")
        rospy.loginfo("Starting speed controller")

        # Subscribers
        rospy.Subscriber("/desired_drive_vel", Twist, self.new_target_vel)

        # {x: Accel, y: Decel, z: Angular}
        rospy.Subscriber("/drive_accels", Vector3, self.new_accelerations)

        # Actual velocity publisher
        self.pub = rospy.Publisher("actual_drive_vel", DriveMsg, queue_size=10)
        self.pub.publish(DriveMsg())
        self.rate = rospy.Rate(rate)

    def new_accelerations(self, accels: Vector3):
        if accels != self._accel_values:
            rospy.loginfo(f"New acceleration values of {accels}")
            self._accel_values = accels

    def new_target_vel(self, velocity: Twist):
        rospy.loginfo(f"Target Velocity Set to {velocity}")
        self._target_twist = self._extract_speeds(velocity)

    def _extract_speeds(self, twist_msg: Twist):
        angle = np.radians(twist_msg.angular.z)

        twist_msg.angular.z = 0
        twist_msg.linear.x = twist_msg.linear.x * np.cos(angle)
        twist_msg.linear.y = twist_msg.linear.x * np.sin(angle)
        return twist_msg

    def twist2drive(self, msg: DriveMsg, current_twist: Twist):

        # Check if there was a change
        if current_twist != self._target_twist:
            # If we want to spin in place
            if np.abs(self._target_twist.angular.y) > 0:
                current_twist.angular.y = self.apply_acceleration(current_twist.angular.y,
                                                            self._target_twist.angular.y,
                                                            accel = self._accel_values.z,
                                                            deccel = self._accel_values.z)


                msg.left = self.apply_acceleration(
                    msg.left,
                    self._target_twist.angular.y,
                    accel = self._accel_values.z,
                    deccel = self._accel_values.z
                )

                msg.right = self.apply_acceleration(
                    msg.right,
                    -self._target_twist.angular.y,
                    accel = self._accel_values.z,
                    deccel = self._accel_values.z
                )

            else:
                current_twist.linear.x = self.apply_acceleration(current_twist.linear.x,
                                                                      self._target_twist.linear.x,
                                                                      accel=self._accel_values.x,
                                                                      deccel=self._accel_values.y)
                current_twist.linear.y = self.apply_acceleration(current_twist.linear.y,
                                                                      self._target_twist.linear.y,
                                                                      accel=self._accel_values.x,
                                                                      deccel=self._accel_values.y)
                # current_twist.angular.z = self.apply_acceleration(current_twist.angular.z,
                #                                                        self._target_twist.angular.z,
                #                                                        accel=self._accel_values.z,
                #                                                        deccel=self._accel_values.z)

                if current_twist.linear.y >= 0:
                    msg.left = current_twist.linear.x
                    msg.right = current_twist.linear.x - current_twist.linear.y

                else:
                    msg.left = current_twist.linear.x - current_twist.linear.y
                    msg.right = current_twist.linear.x

        msg.left = int(msg.left)
        msg.right = int(msg.right)
        return (msg, current_twist)


    @staticmethod
    def apply_acceleration(current, target, accel, deccel):
        diff = target - current

        # Positive means we need to speed up
        # Negative means we need to slow down
        if diff >= 0:
            if np.abs(diff) >= accel:
                current += accel
            else:
                current = target
        else:
            if np.abs(diff) >= deccel:
                current -= deccel
            else:
                current = target

        return current

    def main(self):
        current_twist = Twist()
        drive_out = DriveMsg()

        while not rospy.is_shutdown():

            drive_out, current_twist = self.twist2drive(drive_out, current_twist)
            if drive_out is not None:
                self.pub.publish(drive_out)
            self.rate.sleep()


            # if self._actual_twist != self._target_twist:
            #
            #     # Handle static rotation
            #     if np.abs(self._target_twist.angular.y) > 0:
            #         self._actual_twist.linear.x = self.apply_acceleration(self._actual_twist.linear.x, self._target_twist.angular.y,
            #                                                      accel=self._accel_values.x,
            #                                                      deccel=self._accel_values.y)
            #         self._actual_twist.linear.y = self.apply_acceleration(self._actual_twist.linear.y, -self._target_twist.angular.y,
            #                                                      accel=self._accel_values.x,
            #                                                      deccel=self._accel_values.y)
            #         self._actual_twist.angular.z = self.apply_acceleration(self._actual_twist.angular.z, 0,
            #                                                       accel=self._accel_values.z,
            #                                                       deccel=self._accel_values.z)
            #
            #         if np.abs(self._target_twist.linear.x) > 0:
            #             rospy.logwarn(f"Linear set to {self._target_twist.linear.x} while rotating. This will be ignored")
            #
            #         if np.abs(self._target_twist.angular.z) > 0:
            #             rospy.logwarn(f"Angular set to {self._target_twist.angular.z} while rotating. This will be ignored")
            #
            #     else:
            #         # Handles "normal" bike model motion
            #         self._actual_twist.linear.x = self.apply_acceleration(self._actual_twist.linear.x, self._target_twist.linear.x,
            #                                                      accel=self._accel_values.x,
            #                                                      deccel=self._accel_values.y)
            #         self._actual_twist.linear.y = self.apply_acceleration(self._actual_twist.linear.y, self._target_twist.linear.y,
            #                                                      accel=self._accel_values.x,
            #                                                      deccel=self._accel_values.y)
            #         self._actual_twist.angular.z = self.apply_acceleration(self._actual_twist.angular.z, self._target_twist.angular.z,
            #                                                       accel=self._accel_values.z,
            #                                                       deccel=self._accel_values.z)
            #
            # drive_out = self.twist2drive(self._actual_twist)
            # self.pub.publish(drive_out)
            # self.rate.sleep()

if __name__ == "__main__":

    accels = Vector3(
        x=3,
        y=8,
        z=5
    )
    speed_controller = VelocityController(init_accels=accels)
    speed_controller.main()