#!/usr/bin/env python3

from servo_scripts.camera_position_controller import YawController

if __name__ == "__main__":

    yaw = YawController()
    yaw.main()