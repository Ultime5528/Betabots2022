from commands2 import CommandBase

import wpilib
from constants import Proprietes
from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase


class Piloter(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, stick: wpilib.Joystick, xbox_controller: wpilib.Joystick):
        super().__init__()

        self.stick = stick
        self.xbox_controller = xbox_controller
        self.base_pilotable = base_pilotable
        self.addRequirements(base_pilotable)

    def execute(self):
        # Si bouton deux pressed, on peut faire tourner le robot. Sinon, il est en mecanum pure.
        if self.stick.getRawButton(2):
            # Avec rotation
            self.base_pilotable.deadzoneDriveCartesian(
                0.0,
                Proprietes.pilotage_max_y * -self.stick.getY(),
                Proprietes.pilotage_max_x * self.stick.getX()
            )
        else:
            # Sans rotation / Mecanum pure
            self.base_pilotable.deadzoneDriveCartesian(
                Proprietes.pilotage_max_x * self.stick.getX(),
                Proprietes.pilotage_max_y * -self.stick.getY(),
                0.0
            )
        # self.base_pilotable.driveCartesian(Proprietes.pilotage_max_x * self.stick.getX(), Proprietes.pilotage_max_y * -self.stick.getY(), Proprietes.pilotage_max_z * self.stick.getZ())

