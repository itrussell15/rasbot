import rospy
from std_msgs.msg import Int16

from .servo_driver import ServoController, SERVO_VALUE

class CameraServoController(ServoController):

    def __init__(self, servo_value, init_angle, node_name):
        super().__init__(servo_value=servo_value)
        self._node_name = node_name
        rospy.init_node(self._node_name)
        self.move(init_angle)

    def main(self):
        rospy.Subscriber(f"/{self._node_name}", Int16, self.callback)
        rospy.spin()

    def callback(self, msg):
        rospy.loginfo(f"Servo value changed to {msg.data}")
        self.move(msg.data)

class PitchController(CameraServoController):

    def __init__(self, init_angle = 20):
        super().__init__(
            servo_value=SERVO_VALUE.PITCH,
            init_angle=init_angle,
            node_name="camera_pitch"
        )
        rospy.loginfo("Start camera pitch controller")

    def callback(self, msg):
        rospy.loginfo(f"Pitch value changed to {msg.data}")
        self.move(msg.data)

class YawController(CameraServoController):

    def __init__(self, init_angle = 79):
        super().__init__(
            servo_value=SERVO_VALUE.YAW,
            init_angle=init_angle,
            node_name="camera_yaw"
        )
        rospy.loginfo("Start camera yaw controller")

    def callback(self, msg):
        rospy.loginfo(f"Yaw value changed to {msg.data}")
        self.move(msg.data)