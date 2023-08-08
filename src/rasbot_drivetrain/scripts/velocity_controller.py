#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

from rasbot_msgs.msg import drive_msg

import numpy as np


class VelocityController:

    def __init__(self, init_accels: Vector3, rate: int = 5):
        rospy.init_node("drive_speed_controller")
        rospy.loginfo("Starting speed controller")

        self._target_drive = drive_msg()
        self._current_drive = drive_msg()

        # Subscriber to set target_drive
        rospy.Subscriber("/desired_drive_vel", Twist, self.set_target_drive)

        # {x: Accel, y: Decel, z: Angular}
        rospy.Subscriber("/drive_accels", Vector3, self.new_accelerations)
        self._accel_values = init_accels

        # Actual velocity publisher
        self.pub = rospy.Publisher("actual_drive_vel", drive_msg, queue_size=10)

        # Rate object
        self.rate = rospy.Rate(rate)

    def new_accelerations(self, accels: Vector3):
        if accels != self._accel_values:
            rospy.loginfo(f"New acceleration values of {accels}")
            self._accel_values = accels

    def set_target_drive(self, msg: Twist):
        rospy.loginfo(f"Incoming twist message: {msg}")

        if msg.linear.y != 0:
            rospy.logwarn(f"No valid use for linear.y value.. ignoring")

        if msg.linear.z != 0:
            rospy.logwarn(f"No valid use for linear.z value.. ignoring")

        if msg.angular.x != 0:
            rospy.logwarn(f"No valid use for angular x value.. ignoring")

        # Spin in place motion
        if np.abs(msg.angular.y) > 0:
            if msg.linear.x != 0:
                rospy.logwarn(f"Since angular.y was non-zero, ignoring linear.x value")

            if msg.angular.z != 0:
                rospy.logwarn(f"Since angular.y was non-zero, ignoring angular.z value")

            self._target_drive.left = msg.angular.y
            self._target_drive.right = -msg.angular.y
        else:
            # Bike model motion
            raw_angle = msg.angular.z

            if np.abs(raw_angle) > 45:
                rospy.logwarn(f'Angle of {raw_angle} was clipped to be in range -45 to 45')
                raw_angle = np.clip(raw_angle, a_min = -45, a_max = 45)

            angle = np.radians(raw_angle)
            forward = np.cos(angle)
            side = np.sin(angle)

            # Clip this since a forward of 0 can lead to infinity multiplier
            multiplier = 1 - np.abs(side / forward)

            if np.abs(side) == 0:
                self._target_drive.left = msg.linear.x
                self._target_drive.right = msg.linear.x
            else:
                if side >= 0:
                    self._target_drive.left = msg.linear.x
                    self._target_drive.right = msg.linear.x * multiplier
                    print(f"HERE --> {multiplier}")
                else:
                    self._target_drive.left = msg.linear.x * -multiplier
                    self._target_drive.right = msg.linear.x
                    print(f"HERE --> {multiplier}")

            rospy.loginfo(f"Twist message turned to target DriveMsg: {self._target_drive}")

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

        while not rospy.is_shutdown():

            # Check left speed compared to target
            if self._target_drive.left != self._current_drive.left:
                self._current_drive.left = self.apply_acceleration(
                    current = self._current_drive.left,
                    target = self._target_drive.left,
                    accel = self._accel_values.x,
                    deccel=self._accel_values.y
                )

            # Check right speed compared to target
            if self._target_drive.right != self._current_drive.right:
                self._current_drive.right = self.apply_acceleration(
                    current = self._current_drive.right,
                    target = self._target_drive.right,
                    accel = self._accel_values.x,
                    deccel=self._accel_values.y
                )

            self._current_drive.left = int(self._current_drive.left)
            self._current_drive.right = int(self._current_drive.right)
            self.pub.publish(self._current_drive)
            self.rate.sleep()

if __name__ == "__main__":

    accels = Vector3(
        x=5,
        y=5,
        z=5
    )
    speed_controller = VelocityController(init_accels=accels)
    speed_controller.main()