import wpilib
from utils import safecommandbase
from subsystems.basepilotable import BasePilotable

import constants


class AlignerUltrason(safecommandbase.SafeCommandBase):
    def __init__(self, basepilotable: BasePilotable):
        self.basepilotable = basepilotable

    def execute(self) -> None:
        pass
        # if self.basepilotable.get_ultrasound_left() > 3:


