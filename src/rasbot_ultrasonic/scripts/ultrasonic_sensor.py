#!/usr/bin/env python3

import rospy
import numpy as np
from sensor_msgs.msg import Range

from ultrasonic_driver import UltrasonicSensor

class RangeReader(UltrasonicSensor):

    def __init__(self, rate = 5):
        super().__init__()
        rospy.init_node("ultrasonic_sensor_reading")
        rospy.loginfo("Start ultrasonic_sensor_reading")
        self.pub = rospy.Publisher("ultrasonic_raw", Range, queue_size = 10)
        self.rate = rospy.Rate(rate)

    def read(self):
        msg = Range()
        msg.min_range = 0.01
        msg.max_range = 1.75
        msg.radiation_type = 0

        while not rospy.is_shutdown():
            msg.range = np.clip(self.read_raw(), a_min = msg.min_range, a_max = msg.max_range)
            # rospy.loginfo(msg)
            self.pub.publish(msg)
            self.rate.sleep()

if __name__ == "__main__":

    sensor = RangeReader()
    sensor.read()
