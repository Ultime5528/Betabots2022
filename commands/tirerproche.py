import wpilib
import commands2
from utils import safecommandbase
from subsystems.tireur import Tireur
from constants import *


class TirerProche(safecommandbase):
    def __init__(self, tireur: Tireur):
        self.tireur = tireur
        self.addRequirements([tireur])

    def execute(self):
        self.tireur.tirer_proche()

    def end(self, iterrupted: bool) -> None:
        self.tireur.stop()
