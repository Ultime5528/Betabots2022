import math

from commands2 import CommandBase

import wpilib

import constants
from constants import Proprietes
from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase


class TournerX(SafeCommandBase):
    def __init__(self, drive: BasePilotable, angle: float, speed: float):
        super().__init__()
        self.angle = angle
        self.drive = drive
        self.speed = speed
        self.addRequirements(self.drive)
        self.error = float('inf')

    def initialize(self):
        self.drive.resetOdometry()

    def execute(self):
        self.error = self.drive.getAngle() - self.angle
        self.drive.deadzoneDriveCartesian(0, 0, math.copysign(self.speed, self.error))

    def end(self, interrupted: bool):
        self.drive.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.error) <= 3

