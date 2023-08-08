from I2C_Control import LowLevelI2C
import enum
import numpy as np

class DriveTrain:

    def __init__(self):
        self._llc = LowLevelI2C(0x16, 1)
        self._right = self.DriveSide()
        self._left = self.DriveSide()

    def drive(self, value):
        # print("Drive Command Sent: {}%".format(value))
        array = self._left.drive(value)
        array.extend(self._right.drive(value))
        self._llc.write_array(int(self.Registers.MOVE), array)

    def turn(self, value):
        array = self._left.drive(value)
        array.extend(self._right.drive(-value))
        self._llc.write_array(int(self.Registers.MOVE), array)

    def command(self, left_value, right_value):
        array = self._left.drive(left_value)
        array.extend(self._right.drive(right_value))
        self._llc.write_array(int(self.Registers.MOVE), array)

    def stop(self):
        self._llc.writeByte(int(self.Registers.STOP), 0x00)

    class Registers(enum.IntEnum):
        MOVE = 0x01
        STOP = 0x02
        SERVO = 0x03

    # %%%%% Left and Right side Controller
    class DriveSide:

        def __init__(self, max_value=150):
            self._max_value = max_value

        def drive(self, value):
            dir = 1
            if value > 0:
                dir = 0
            value = np.clip(value, a_min = -self._max_value, a_max = self._max_value)
            return [dir, int(abs(self._drive_value(value)))]

        # Turns 0-100 value into a value that the drivers can use.
        def _drive_value(self, val):
            return self._map_values(val, 0, 100.0, 0, self._max_value)

        @staticmethod
        def _map_values(value, fromMin, fromMax, toMin, toMax):
            # Figure out how 'wide' each range is
            fromSpan = fromMax - fromMin
            toSpan = toMax - toMin

            # Convert the left range into a 0-1 range (float)
            valueScaled = float(value - fromMin) / float(fromSpan)

            # Convert the 0-1 range into a value in the right range.
            return toMin + (valueScaled * toSpan)

if __name__ == "__main__":
    import time

    dt = DriveTrain()
    dt.drive(0.25)
    time.sleep(3)
    dt.stop()
