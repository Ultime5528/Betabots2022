import wpilib
from utils import safecommandbase
from subsystems.tireur import Tireur
from subsystems.basepilotable import BasePilotable

import constants


class AlignerUltrason(safecommandbase.SafeCommandBase):
    def __init__(self, tireur: Tireur, basepilotable: BasePilotable):
        self.tireur = tireur
        self.basepilotable = basepilotable

    def execute(self) -> None:
        if self.tireur.get_ultrasound_left() > 3:


