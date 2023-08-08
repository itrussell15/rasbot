#!/usr/bin/env python3

from servo_scripts.camera_position_controller import PitchController

if __name__ == "__main__":

    pitch = PitchController()
    pitch.main()