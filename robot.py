#!/usr/bin/env python3

import commands2
import wpilib

from commands.piloter import Piloter
from commands.tourner import Tourner
from commands.avancerx import AvancerX
from subsystems.basepilotable import BasePilotable
from commands2.button import JoystickButton


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        # wpilib.CameraServer.launch('vision.py:main')
        self.base_pilotable = BasePilotable()

        self.stick = wpilib.Joystick(0)
        self.xbox_controller = wpilib.Joystick(1)

        self.base_pilotable.setDefaultCommand(Piloter(self.base_pilotable, self.stick, self.xbox_controller))
        JoystickButton(self.stick, 5).whenPressed((AvancerX(self.base_pilotable, 5, 1000, 352)))
        JoystickButton(self.stick, 4).whenPressed((Tourner(self.base_pilotable, -90, 1)))



if __name__ == "__main__":
    wpilib.run(Robot)
