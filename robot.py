#!/usr/bin/env python3

import commands2
import wpilib

from commands.avancerx import AvancerX
from commands.piloter import Piloter
from commands.tourner import Tourner
from commands.tirerloin import TirerLoin
from commands.tirerproche import TirerProche
from commands.alignerultrason import AlignerUltrason
from subsystems.basepilotable import BasePilotable
from subsystems.tireur import Tireur

from commands2.button import JoystickButton
import os


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        wpilib.CameraServer.launch('vision/vision.py:main')

        self.base_pilotable = BasePilotable()
        self.tireur = Tireur()

        self.stick = wpilib.Joystick(0)
        self.xbox_controller = wpilib.Joystick(1)

        self.base_pilotable.setDefaultCommand(Piloter(self.base_pilotable, self.stick, self.xbox_controller))
        # JoystickButton(self.stick, 3).whenPressed((Tourner(self.base_pilotable, 90, 1)))
        # JoystickButton(self.stick, 4).whenPressed((Tourner(self.base_pilotable, -90, 1)))
        JoystickButton(self.stick, 4).whenPressed((AvancerX(self.base_pilotable, 6, -3, 1)))
        JoystickButton(self.stick, 5).whileHeld((TirerProche(self.tireur)))
        JoystickButton(self.stick, 6).whileHeld((TirerLoin(self.tireur)))
        wpilib.SmartDashboard.putData("Commandes/AlignerUltrason", AlignerUltrason(self.base_pilotable))
        wpilib.SmartDashboard.putData("Commandes/Tourner", AlignerUltrason(self.base_pilotable))

if __name__ == "__main__":
    wpilib.run(Robot)
