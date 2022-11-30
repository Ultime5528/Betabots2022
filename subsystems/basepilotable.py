import math

import commands2
import navx
import rev
import wpilib
import wpilib.drive
from wpilib import RobotBase
from wpilib.simulation import SimDeviceSim
from wpimath.geometry import Rotation2d, Pose2d
from wpimath.geometry import Translation2d
from wpimath.kinematics import MecanumDriveOdometry, MecanumDriveWheelSpeeds, MecanumDriveKinematics
from wpilib.drive import Vector2d

from constants import Ports, Proprietes
from utils.sparkmaxsim import SparkMaxSim
from utils.deadzone import linear_deadzone


class BasePilotable(commands2.SubsystemBase):
    # TBD
    pulses_per_meter = 16.68
    use_navx = True

    def __init__(self) -> None:
        super().__init__()
        # TODO correct mesurements
        self.x_wheelbase = 0.58 / 2
        self.y_wheelbase = 0.515 / 2

        self.fl_motor = rev.CANSparkMax(Ports.base_pilotable_moteur_fl, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        self.fr_motor = rev.CANSparkMax(Ports.base_pilotable_moteur_fr, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        self.rl_motor = rev.CANSparkMax(Ports.base_pilotable_moteur_rl, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        self.rr_motor = rev.CANSparkMax(Ports.base_pilotable_moteur_rr, rev.CANSparkMaxLowLevel.MotorType.kBrushless)

        for motor in [self.fl_motor, self.fr_motor, self.rl_motor, self.rr_motor]:
            motor.restoreFactoryDefaults()
            motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)

        self.fr_motor.setInverted(True)
        self.rr_motor.setInverted(True)

        self.fl_encoder = self.fl_motor.getEncoder()
        self.fr_encoder = self.fr_motor.getEncoder()
        self.rl_encoder = self.rl_motor.getEncoder()
        self.rr_encoder = self.rr_motor.getEncoder()

        self.accel = wpilib.BuiltInAccelerometer()

        for encoder in [self.fl_encoder, self.fr_encoder, self.rl_encoder, self.rr_encoder]:
            encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
            encoder.setVelocityConversionFactor(1 / (self.pulses_per_meter * 60))

        if self.use_navx:
            self.gyro = navx.AHRS(wpilib.SerialPort.Port.kMXP)
            self.gyro.reset()
            self.gyro.calibrate()
        # else:
        #     self.gyro = wpilib.ADXRS450_Gyro()

        self.drive = wpilib.drive.MecanumDrive(self.fl_motor, self.rl_motor, self.fr_motor, self.rr_motor)

        self.kinematics = MecanumDriveKinematics(
            Translation2d(self.x_wheelbase, self.y_wheelbase),
            Translation2d(self.x_wheelbase, (self.y_wheelbase)*-1),
            Translation2d((self.x_wheelbase)*-1, self.y_wheelbase),
            Translation2d((self.x_wheelbase)*-1, (self.y_wheelbase)*-1),
        )
        self.wheelSpeeds = MecanumDriveWheelSpeeds()
        self.odometry = MecanumDriveOdometry(self.kinematics, Rotation2d.fromDegrees(0.0))

        if RobotBase.isSimulation():
            from utils.mecanumdrivesim import MecanumDriveSim
            self.field = wpilib.Field2d()
            wpilib.SmartDashboard.putData("Field", self.field)
            self.drive_sim = MecanumDriveSim(self.kinematics)
            self.fl_motor_sim = SparkMaxSim(self.fl_motor)
            self.fr_motor_sim = SparkMaxSim(self.fr_motor)
            self.rl_motor_sim = SparkMaxSim(self.rl_motor)
            self.rr_motor_sim = SparkMaxSim(self.rr_motor)
            self.gyro_sim_device = SimDeviceSim("navX-Sensor[1]")
            self.gyro_yaw_sim = self.gyro_sim_device.getDouble("Yaw")
        self.resetOdometry()

    def driveCartesian(self, ySpeed: float, xSpeed: float, zRot: float) -> None:
        self.drive.driveCartesian(ySpeed, xSpeed, zRot, 0.0)

    def deadzoneDriveCartesian(self, ySpeed: float, xSpeed: float, zRot: float) -> None:
        """
        :param ySpeed: forward
        :param xSpeed: turn
        :param zRot:
        :return:
        """
        self.drive.driveCartesian(linear_deadzone(ySpeed, Proprietes.pilotage_deadzone),
                                  linear_deadzone(xSpeed, Proprietes.pilotage_deadzone),
                                  linear_deadzone(zRot, Proprietes.pilotage_deadzone), 0.0)

    def drivePolar(self, mag: float, angle: float, zRot: float) -> None:
        self.drive.drivePolar(mag, angle, zRot)

    def resetOdometry(self) -> None:
        self.fl_encoder.setPosition(0)
        self.fr_encoder.setPosition(0)
        self.rl_encoder.setPosition(0)
        self.rr_encoder.setPosition(0)
        self.gyro.reset()
        self.odometry.resetPosition(Pose2d(), Rotation2d.fromDegrees(0.0))

        if RobotBase.isSimulation():
            self.drive_sim.resetOdometry()

    def periodic(self) -> None:
        self.wheelSpeeds.frontLeft = self.fl_encoder.getVelocity()
        self.wheelSpeeds.frontRight = self.fr_encoder.getVelocity()
        self.wheelSpeeds.rearLeft = self.rl_encoder.getVelocity()
        self.wheelSpeeds.rearRight = self.rr_encoder.getVelocity()

        self.odometry.update(
            Rotation2d.fromDegrees(self.getAngle()),
            self.wheelSpeeds
        )
        wpilib.SmartDashboard.putNumber("fl_motor/Value", self.fl_motor.get())
        wpilib.SmartDashboard.putNumber("fl_motor/Position", self.fl_encoder.getPosition())
        wpilib.SmartDashboard.putNumber("fl_motor/Velocity", self.fl_encoder.getVelocity())
        wpilib.SmartDashboard.putNumber("fr_motor/Value", self.fr_motor.get())
        wpilib.SmartDashboard.putNumber("fr_motor/Position", self.fr_encoder.getPosition())
        wpilib.SmartDashboard.putNumber("fr_motor/Velocity", self.fr_encoder.getVelocity())
        wpilib.SmartDashboard.putNumber("rl_motor/Value", self.rl_motor.get())
        wpilib.SmartDashboard.putNumber("rl_motor/Position", self.rl_encoder.getPosition())
        wpilib.SmartDashboard.putNumber("rl_motor/Velocity", self.rl_encoder.getVelocity())
        wpilib.SmartDashboard.putNumber("rr_motor/Value", self.rr_motor.get())
        wpilib.SmartDashboard.putNumber("rr_motor/Position", self.rr_encoder.getPosition())
        wpilib.SmartDashboard.putNumber("rr_motor/Velocity", self.rr_encoder.getVelocity())
        pose = self.odometry.getPose()
        wpilib.SmartDashboard.putNumber("Odometry/X", pose.X())
        wpilib.SmartDashboard.putNumber("Odometry/Y", pose.Y())
        wpilib.SmartDashboard.putNumber("Odometry/Rotation", pose.rotation().degrees())
        wpilib.SmartDashboard.putNumber("accelX", self.getAccelX())
        wpilib.SmartDashboard.putNumber("accelY", self.getAccelY())
        wpilib.SmartDashboard.putNumber("accelZ", self.getAccelZ())
        wpilib.SmartDashboard.putBoolean("isMoving", self.isMoving())

    def drive_test(self, value: float):
        self.fl_motor.set(value)
        self.fr_motor.set(value)
        self.rl_motor.set(value)
        self.rr_motor.set(value)

    def simulationPeriodic(self) -> None:
        self.drive_sim.update(
            self.fl_motor.get(), self.fr_motor.get(), self.rl_motor.get(), self.rr_motor.get()
        )
        self.fl_motor_sim.setVelocity(self.drive_sim.getFrontLeftRate())
        self.fl_motor_sim.setPosition(self.drive_sim.getFrontLeftPosition())
        self.fr_motor_sim.setVelocity(self.drive_sim.getFrontRightRate())
        self.fr_motor_sim.setPosition(self.drive_sim.getFrontRightPosition())
        self.rl_motor_sim.setVelocity(self.drive_sim.getRearLeftRate())
        self.rl_motor_sim.setPosition(self.drive_sim.getRearLeftPosition())
        self.rr_motor_sim.setVelocity(self.drive_sim.getRearRightRate())
        self.rr_motor_sim.setPosition(self.drive_sim.getRearRightPosition())
        self.gyro_yaw_sim.set(-self.drive_sim.getHeading().degrees())
        self.field.setRobotPose(self.drive_sim.odometry.getPose())

    def getAngle(self):
        return -math.remainder(self.gyro.getAngle(), 360.0)

    def getEncoderDistances(self):
        return [self.fl_encoder.getPosition(), self.fr_encoder.getPosition(), self.rl_encoder.getPosition(), self.rr_encoder.getPosition()]

    def getAccelX(self):
        # vec = Vector2d(self.gyro.getWorldLinearAccelX(), self.gyro.getWorldLinearAccelY())
        # vec.rotate(-self.gyro.getYaw())
        # return vec.x
        return self.accel.getX()

    def getAccelY(self):
        # vec = Vector2d(self.gyro.getWorldLinearAccelX(), self.gyro.getWorldLinearAccelY())
        # vec.rotate(-self.gyro.getYaw())
        # return vec.y
        return self.accel.getY()

    def getAccelZ(self):
        return self.gyro.getWorldLinearAccelZ()

    def isMoving(self):
        return self.gyro.isMoving()
