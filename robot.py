#!/usr/bin/env python3

import commands2
import wpilib

from commands.drop import Drop
from commands.dropreset import DropReset
from commands.hold import Hold
from commands.autogauche import AutoGauche
from commands.autodroit import AutoDroit
from commands.piloter import Piloter
from commands.aligner_pyramide import AlignerPyramide
from commands.aller_pyramide import AllerPyramide
from commands.reset import Reset
from commands.troisdents_idle import TroisDentsIdle

from subsystems.basepilotable import BasePilotable
from subsystems.troisdents import TroisDents

from commands2.button import JoystickButton


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        wpilib.CameraServer.launch('vision.py:main')
        self.base_pilotable = BasePilotable()
        self.troisdents = TroisDents()

        self.stick = wpilib.Joystick(0)
        self.xbox_controller = wpilib.Joystick(1)
        JoystickButton(self.stick, 7).whenPressed(Hold(self.troisdents))
        JoystickButton(self.stick, 8).whenPressed(TroisDentsIdle(self.troisdents))
        JoystickButton(self.stick, 9).whenPressed(Reset(self.troisdents))
        JoystickButton(self.stick, 11).whenPressed(DropReset(self.troisdents))
        JoystickButton(self.stick, 12).whenPressed(Drop(self.troisdents))

        self.base_pilotable.setDefaultCommand(Piloter(self.base_pilotable, self.stick, self.xbox_controller))
        JoystickButton(self.stick, 3).toggleWhenPressed(AlignerPyramide(self.base_pilotable, 0.0))
        JoystickButton(self.stick, 4).toggleWhenPressed(AllerPyramide(self.base_pilotable, 0.0, 1000))
        # JoystickButton(self.stick, 5).whenPressed(AutoGauche(self.troisdents, self.base_pilotable))
        # JoystickButton(self.stick, 6).whenPressed(AutoDroit(self.troisdents, self.base_pilotable))

        # wpilib.SmartDashboard.putData("AlignerPyramide", AlignerPyramide(self.base_pilotable, 1))
        # wpilib.SmartDashboard.putData("Commandes/Pyramide1", AlignerPyramide(self.base_pilotable, 1))
        # wpilib.SmartDashboard.putData("Commandes/Pyramide2", AlignerPyramide(self.base_pilotable, 2))
        # wpilib.SmartDashboard.putData("Commandes/Pyramide3", AlignerPyramide(self.base_pilotable, 3))
        # wpilib.SmartDashboard.putData("Commandes/Pyramide4", AlignerPyramide(self.base_pilotable, 4))
        # wpilib.SmartDashboard.putData("Commandes/Pyramide5", AlignerPyramide(self.base_pilotable, 5))
        wpilib.SmartDashboard.putData("Commandes/Hold", Hold(self.troisdents))
        wpilib.SmartDashboard.putData("Commandes/Reset", Reset(self.troisdents))
        wpilib.SmartDashboard.putData("Commandes/DropReset", DropReset(self.troisdents))
        wpilib.SmartDashboard.putData("Commandes/AutoGauche", AutoGauche(self.troisdents, self.base_pilotable))
        wpilib.SmartDashboard.putData("Commandes/AutoDroit", AutoDroit(self.troisdents, self.base_pilotable))

        self.autoCommand: commands2.CommandBase = None
        self.autoChooser = wpilib.SendableChooser()
        self.autoChooser.setDefaultOption("Rien", None)
        self.autoChooser.addOption("Auto gauche", AutoGauche(self.troisdents, self.base_pilotable))
        self.autoChooser.addOption("Auto droit", AutoDroit(self.troisdents, self.base_pilotable))
        wpilib.SmartDashboard.putData("ModeAutonome", self.autoChooser)

    def autonomousInit(self):
        self.autoCommand = self.autoChooser.getSelected()

        if self.autoCommand:
           self.autoCommand.schedule()

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        if self.autoCommand:
           self.autoCommand.cancel()

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
