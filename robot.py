#!/usr/bin/env python3

import commands2
import wpilib

from commands.piloter import Piloter
from subsystems.basepilotable import BasePilotable
import os

class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        wpilib.CameraServer.launch('vision/vision.py:run')

        self.base_pilotable = BasePilotable()

        self.stick = wpilib.Joystick(0)
        self.xbox_controller = wpilib.Joystick(1)

        self.base_pilotable.setDefaultCommand(Piloter(self.base_pilotable, self.stick, self.xbox_controller))


if __name__ == "__main__":
    wpilib.run(Robot)
