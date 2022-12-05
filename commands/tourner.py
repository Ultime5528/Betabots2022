import math

from commands2 import CommandBase

import wpilib

from constants import Proprietes
from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase


class Tourner(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, angle, vitesse):
        self.setname("TournerX")
        super().__init__()
        self.base_pilotable = base_pilotable
        self.angle = angle
        self.vitesse = vitesse
        self.erreur = math.inf
        self.addRequirements(base_pilotable)

    def initialize(self):
        self.base_pilotable.resetOdometry()

    def execute(self):
        self.erreur = self.base_pilotable.getAngle() - self.angle
        self.base_pilotable.driveCartesian(0, 0, math.copysign(self.vitesse, self.erreur))

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.erreur) <= 5

