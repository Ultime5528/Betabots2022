import wpilib
import commands2
from utils import safecommandbase
from subsystems.tireur import Tireur
from constants import *


class TirerLoin(safecommandbase):
    def __init__(self, tireur: Tireur):
        self.tireur = tireur
        self.timer = wpilib.Timer()
        self.addRequirements([tireur])

    def initialize(self):
        self.timer.stop()
        self.timer.reset()

    def execute(self):
        self.tireur.tirer(Proprietes.tirer_speed_long)

    def is_finished(self) -> bool:
        return self.timer.get() >= Proprietes.tirer_temps_loin

    def end(self, interrupted: bool) -> None:
        self.tireur.stop()
        self.timer.stop()

