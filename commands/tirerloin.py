import wpilib
import commands2
from utils import safecommandbase
from subsystems.tireur import Tireur


class TirerLoin(safecommandbase):
    def __init__(self, tireur: Tireur):
        self.tireur = tireur
        self.timer = wpilib.Timer()

        self.tireur_speed = 0.2
        self.tempsTirer = 2

    def initialize(self):
        self.timer.stop()
        self.timer.reset()

    def execute(self):
        self.tireur.tirer(self.tireur_speed)

    def is_finished(self) -> bool:
        return self.timer.get() >= Constants.temps_tirer_loin

    def end(self, interrupted: bool) -> None:
        self.tireur.stop()
        self.timer.stop()

