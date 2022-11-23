import wpilib
import commands2
from utils import safecommandbase
from subsystems.tireur import Tireur
from constants import *


class Shake(safecommandbase):
    def __init__(self, tireur: Tireur):
        self.tireur = tireur
        self.timer = wpilib.Timer()
        self.addRequirements([tireur])

    def initialize(self):
        self.timer.stop()
        self.timer.reset()

    def execute(self):
        self.tireur.shake(Proprietes.shake_speed)

    def is_finished(self) -> bool:
        return self.timer.get() >= Proprietes.shake_temps

    def end(self, interrupted: bool) -> None:
        self.tireur.stop_shake()
        self.timer.stop()