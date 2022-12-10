from utils.safecommandbase import SafeCommandBase
from subsystems.tireur import Tireur


class TirerLoin(SafeCommandBase):
    def __init__(self, tireur: Tireur):
        self.setName("TirerLoin")
        super().__init__()
        self.tireur = tireur
        self.addRequirements(tireur)

    def execute(self):
        self.tireur.tirer_loin()

    def end(self, interrupted: bool) -> None:
        self.tireur.stop()

