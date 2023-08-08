#!/usr/bin/env python3

import rospy
from drivetrain_driver import DriveTrain
# from std_msgs.msgs import Float64
from geometry_msgs.msg import Twist

from rasbot_msgs.msg import drive_msg


import numpy as np

class DriveNode(DriveTrain):
	def __init__(self, max_val = 150):
		super().__init__()
		rospy.init_node('drive_controller')
		rospy.loginfo("Start drive_controller")
		self.stop()
		# self.create_publishers()

		self.speed = 0.0
		# self.current_twist = Twist()
		self.current_speeds = drive_msg()

	def main(self):
		rospy.Subscriber("/actual_drive_vel", drive_msg, self.callback)
		rospy.spin()

	def callback(self, msg):
		if msg != self.current_speeds:
			# self.current_twist = twist_msg
			self.current_speeds = msg

			# if self.current_twist.linear.y >= 0:
			# 	left = self.current_twist.linear.x
			# 	right = self.current_twist.linear.x - self.current_twist.linear.y
			# else:
			# 	left = self.current_twist.linear.x - self.current_twist.linear.y
			# 	right = self.current_twist.linear.x

			self.command(
				left_speed=int(self.current_speeds.left),
				right_speed=int(self.current_speeds.right)
			)

	def stop(self):
		rospy.loginfo("motors stopped")
		super().stop()

	def drive(self, speed):
		rospy.loginfo(f"new velocity command of {speed}")
		super().drive(speed)

	def command(self, left_speed, right_speed):
		rospy.loginfo(f"Left Speed: {left_speed} -- Right Speed {right_speed}")
		super().command(left_speed, right_speed)

if __name__ == "__main__":
	# speed_control = VelocityController(init_vel = 0, init_accel = 1.0)
	# speed_control.main()

	drive = DriveNode()
	drive.main()
	drive.stop()
