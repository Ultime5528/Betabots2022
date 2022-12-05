import math

from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase


class AvancerX(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, distanceX, distanceY, vitesse):
        self.setname("AvancerX")
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
        self.erreurX = math.inf
        self.erreurY = math.inf
        print(self.base_pilotable.odometry.getPose().X(), self.base_pilotable.odometry.getPose().Y())

    def execute(self):
        self.erreurX = abs(self.distanceX - self.base_pilotable.odometry.getPose().X())
        self.erreurY = abs(self.distanceY + self.base_pilotable.odometry.getPose().Y())

        vx = self.vitesseX
        vy = self.vitesseY

        if self.erreurX <= self.erreur_max:
            vx = 0
        if self.erreurY <= self.erreur_max:
            vy = 0

        self.base_pilotable.driveCartesian(vx, vy, 0)

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return self.erreurX <= self.erreur_max and self.erreurY <= self.erreur_max
