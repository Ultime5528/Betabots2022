#!/usr/bin/env python3

import commands2
import wpilib

from commands.auto4cubes import Auto4Cubes
from commands.avancerx import AvancerX
from commands.piloter import Piloter
from commands.tournerX import TournerX
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
        JoystickButton(self.xbox_controller, 1).whileHeld((TirerProche(self.tireur)))
        JoystickButton(self.xbox_controller, 2).whileHeld((TirerLoin(self.tireur)))
        # Bouger d'un cube
        JoystickButton(self.stick, 3).whenPressed(AvancerX(self.base_pilotable, 0, 0.4, 0, 0.5))
        JoystickButton(self.stick, 4).whenPressed(AvancerX(self.base_pilotable, 0, -0.4, 0, 0.5))

        # JoystickButton(self.xbox_controller, 1).whenPressed((Auto4Cubes(self.base_pilotable, self.tireur)))
        # JoystickButton(self.stick, 11).whenPressed(TournerX(self.base_pilotable, 90, 0.5))
        # JoystickButton(self.stick, 12).whenPressed(TournerX(self.base_pilotable, -90, 0.5))
        # JoystickButton(self.stick, 4).whenPressed((AvancerX(self.base_pilotable, 1, -1, 0.1, 0.2)))

        # JoystickButton(self.stick, 1).whenPressed((TirerLoin(self.tireur, False)))
        # wpilib.SmartDashboard.putData("Commandes/AlignerUltrason", AlignerUltrason(self.base_pilotable))
        # wpilib.SmartDashboard.putData("Commandes/Tourner", AlignerUltrason(self.base_pilotable))

        # wpilib.SmartDashboard.putData("Commandes/TournerX", TournerX(self.base_pilotable, 90, 0.1))


if __name__ == "__main__":
    wpilib.run(Robot)
