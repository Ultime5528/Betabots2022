
from utils.safecommandbase import SafeCommandBase
from subsystems.tireur import Tireur
from constants import *


class TirerProche(SafeCommandBase):
    def __init__(self, tireur: Tireur):
        super().__init__()
        self.tireur = tireur
        self.addRequirements(tireur)

    def execute(self):
        self.tireur.tirer_proche()

    def end(self, interrupted: bool) -> None:
        self.tireur.stop()
