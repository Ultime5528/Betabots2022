import wpilib
from utils import safecommandbase
from subsystems.basepilotable import BasePilotable

import constants


class AlignerUltrason(safecommandbase.SafeCommandBase):
    def __init__(self, basepilotable: BasePilotable):
        super().__init__()
        self.basepilotable = basepilotable

    def execute(self) -> None:
        error = self.basepilotable.get_ultrasound_left() - self.basepilotable.get_ultrasound_right()
        left_speed = 0.5
        right_speed = 0.5

        if abs(error) > constants.Proprietes.aligner_threshold:
            correction = K * error
            left_speed += correction
            right_speed -= correction

        if self.basepilotable.get_ultrasound_left() <= constants.Proprietes.aligner_distance:
            left_speed = 0
        if self.basepilotable.get_ultrasound_right() <= constants.Proprietes.aligner_distance:
            right_speed = 0

        self.basepilotable.tank_drive(left_speed, right_speed)

    def isFinished(self) -> bool:
        return self.basepilotable.get_ultrasound_right() <= constants.Proprietes.aligner_distance and self.basepilotable.get_ultrasound_left() <= constants.Proprietes.aligner_distance

    def end(self, interrupted: bool) -> None:
        self.basepilotable.tank_drive(0, 0)
