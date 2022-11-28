import math

from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase

class AvancerX(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, distance, vitesse):
        super().__init__()

        self.base_pilotable = base_pilotable
        self.distance = distance
        self.vitesse = vitesse
        self.erreur = math.inf

    def initialize(self):
        self.base_pilotable.resetOdometry()

    def execute(self):
        self.erreur = self.distance - sum(self.base_pilotable.getEncoderDistances())/4
        self.base_pilotable.driveCartesian(self.vitesse, 0, 0)

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return self.erreur <= 0.05
