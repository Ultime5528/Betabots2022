import math

from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase

class Avancer(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, distanceX, distanceY, vitesse):
        super().__init__()

        self.base_pilotable = base_pilotable
        self.distance = math.hypot(abs(distanceX), abs(distanceY))
        self.vitesseX = distanceX * vitesse
        self.vitesseY = distanceY * vitesse
        self.erreur = math.inf

    def initialize(self):
        self.base_pilotable.resetOdometry()

    def execute(self):
        self.erreur = self.distance - sum(self.base_pilotable.getEncoderDistances())/4
        self.base_pilotable.driveCartesian(self.vitesseX, self.vitesseY, 0)

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return self.erreur <= 0.0005
