from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase

class AvancerX(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, distance, speed):
        super().__init__()

        self.base_pilotable = base_pilotable
        self.distance = distance
        self.speed = speed

    def initialize(self):
        self.base_pilotable.resetOdometry()

    def execute(self):
        self.base_pilotable.driveCartesian(self.speed, self.speed, 0)

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return sum(self.base_pilotable.getEncoderDistances())/4 >= self.distance
