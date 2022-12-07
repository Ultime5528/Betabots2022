import math

from subsystems.basepilotable import BasePilotable
from utils.safecommandbase import SafeCommandBase


class AvancerX(SafeCommandBase):
    def __init__(self, base_pilotable: BasePilotable, distanceX, distanceY, vitesseX, vitesseY):
        self.setName("AvancerX")
        super().__init__()

        self.base_pilotable = base_pilotable
        self.distanceX = distanceX
        self.distanceY = distanceY
        self.vitesseX = vitesseX
        self.vitesseY = vitesseY
        self.erreurX = math.inf
        self.erreurY = math.inf
        self.erreur_max = 0.1

        self.addRequirements(base_pilotable)

    def initialize(self):
        self.base_pilotable.resetOdometry()
        self.erreurX = math.inf
        self.erreurY = math.inf
        print(self.base_pilotable.odometry.getPose().X(), self.base_pilotable.odometry.getPose().Y())

    def execute(self):
        self.erreurX = self.distanceX - self.base_pilotable.odometry.getPose().X()
        self.erreurY = self.distanceY - self.base_pilotable.odometry.getPose().Y()

        self.vx = math.copysign(self.vitesseX, self.erreurX)
        self.vy = -math.copysign(self.vitesseY, self.erreurY)

        if abs(self.erreurX) <= self.erreur_max:
            self.vx = 0
        if abs(self.erreurY) <= self.erreur_max:
            self.vy = 0

        self.base_pilotable.driveCartesian(self.vy, self.vx, 0)

    def end(self, interrupted: bool):
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return self.vx == 0 and self.vy == 0
