import wpilib
import commands2

from constants import Proprietes
from utils import safecommandbase
from subsystems.tireur import Tireur


class TirerLoin(safecommandbase):
    def __init__(self, tireur: Tireur):
        self.tireur = tireur
        self.addRequirements([tireur])

    def execute(self):
        self.tireur.tirer_loin()

    def end(self, iterrupted: bool) -> None:
        self.tireur.stop()




