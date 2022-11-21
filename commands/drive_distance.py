import math
import commands2
from wpimath.geometry import Pose2d

from subsystems.basepilotable import BasePilotable


class DriveDistance(commands2.CommandBase):
    def __init__(self, drive: BasePilotable, speed_x: float = 0, speed_y: float = 0, x: float = 0,
                 y: float = 0) -> None:
        super().__init__()
        self.drive = drive
        self.distance_x = x
        self.distance_y = y

        self.end_position = Pose2d(x, y, 0)


        self.speed_x = speed_x
        self.speed_y = speed_y
        self.drive = drive
        self.addRequirements([drive])

    def initialize(self) -> None:
        self.drive.resetOdometry()

    def execute(self) -> None:
        transform = self.end_position - self.drive.odometry.getPose()
        x_speed = self.speed_x
        y_speed = self.speed_y
        dx = transform.X()
        dy = transform.Y()
        if abs(dx) <= 0.1:
            x_speed = 0.0
        if abs(dy) <= 0.1:
            y_speed = 0.0
        self.drive.driveCartesian(math.copysign(y_speed, -dy), math.copysign(x_speed, dx), 0)

    def end(self, interrupted: bool) -> None:
        self.drive.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        distance = self.drive.odometry.getPose().translation().distance(self.end_position.translation())
        return distance <= 0.15  # TODO: add to constants
