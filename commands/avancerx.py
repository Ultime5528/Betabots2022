import math

from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase

class AvancerX(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, distanceX, distanceY, vitesse:
        super().__init__()

        self.base_pilotable = base_pilotable
        self.distanceX = distanceX
        self.distanceY = distanceY
        self.vitesseX = math.copysign(vitesse, distanceX)
        self.vitesseY = math.copysign(vitesse, distanceY)
        self.erreurX = math.inf
        self.erreurY = math.inf
        self.erreur_max = 0.05

    def initialize(self):
        self.base_pilotable.resetOdometry()

    def execute(self):
        self.erreurX = abs(self.distanceX - self.base_pilotable.odometry.getPose().X())
        self.erreurY = abs(self.distanceY + self.base_pilotable.odometry.getPose().Y())
        self.base_pilotable.driveCartesian(self.vitesseX, self.vitesseY, 0)
        print(self.erreurY)
        if self.erreurX <= self.erreur_max:
            print("x")
            self.vitesseX = 0
        if self.erreurY <= self.erreur_max:
            print("y")
            self.vitesseY = 0

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return self.erreurX <= self.erreur_max and self.erreurY <= self.erreur_max
