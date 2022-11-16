import wpilib
import commands2
from utils import safecommandbase
from subsystems.tireur import Tireur

class TirerLoin(safecommandbase):
    def __init__(self, tireur: Tireur):
        self.tireur_speed = 0.2
        self.tireur = tireur

    def execute(self):
        self.tireur.tirer(self.tireur_speed)



