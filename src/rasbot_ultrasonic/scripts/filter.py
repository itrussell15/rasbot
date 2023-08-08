#!/usr/bin/env python3

import rospy
import numpy as np
from sensor_msgs.msg import Range

class Filter:

    def __init__(self):
        rospy.init_node(f"ultrasonic_filtered")
        rospy.loginfo("Start ultrasonic sensor filter")
        self.queue = []

    def main(self):
        rospy.Subscriber("/ultrasonic_raw", Range, self.callback)
        rospy.spin()

    def callback(self, msg):
        rospy.loginfo(msg.range)

if __name__ == "__main__":

    filtered = Filter()
    filtered.main()