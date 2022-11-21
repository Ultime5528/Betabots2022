from commands2 import CommandBase

import wpilib

from constants import Proprietes
from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase

class Turn(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, angle, speed):
        super().__init__()

        self.base_pilotable = base_pilotable
        self.angle = angle
        self.speed = speed

    def initialize(self):
        self.base_pilotable.resetOdometry()

    def execute(self):
        self.base_pilotable.driveCartesian(0, 0, abs(self.angle) / self.angle * self.speed)

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.base_pilotable.getAngle()) >= abs(self.angle)

