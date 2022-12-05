import wpilib

import constants
from utils.safecommandbase import SafeCommandBase
from subsystems.tireur import Tireur


class TirerLoin(SafeCommandBase):
    def __init__(self, tireur: Tireur, is_timed: bool = False):
        self.setName("TirerLoin")
        super().__init__()
        self.tireur = tireur
        self.addRequirements(tireur)
        self.is_timed = is_timed
        self.timer = wpilib.Timer()

    def initialize(self) -> None:
        if self.is_timed:
            self.timer.reset()
            self.timer.start()

    def execute(self):
        print(self.is_timed)
        self.tireur.tirer_loin()

    def isFinished(self) -> bool:
        if self.is_timed:
            print(self.timer.get())
            return self.timer.get() >= constants.Proprietes.tireur_time_loin
        else:
            return False

    def end(self, interrupted: bool) -> None:
        self.tireur.stop()
        self.timer.stop()




