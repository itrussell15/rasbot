from I2C_Control import LowLevelI2C
import enum
import numpy as np

class SERVO_VALUE(enum.IntEnum):
    YAW = 1
    PITCH = 2

class ServoController(LowLevelI2C):

    def __init__(self, servo_value: SERVO_VALUE, register = 0x03):
        super().__init__(0x16, 1)
        self.register = register
        self.pos_value = servo_value

        self.min_val = 0
        self.max_val = 180

    def move(self, angle):
        self.write_array(
            reg=self.register,
            data=[self.pos_value.value, self.clamp(angle, self.min_val, self.max_val)]
        )

    @staticmethod
    def clamp(value, min=0, max=180):
        # return int(max(min, min(value, max)))
        return int(np.clip(value, a_min = min, a_max = max))


if __name__ == "__main__":

    import time

    servo_pitch = ServoController(servo_value=SERVO_VALUE.PITCH)
    servo_pitch.move(25)
    time.sleep(2)
    servo_pitch.move(79)

    # time.sleep(2)
    # print("move bottom")
    # servo_yaw = ServoController(servo_value=SERVO_VALUE.YAW)
    # servo_yaw.move(0)
    # time.sleep(2)
    # servo_yaw.move(25)




