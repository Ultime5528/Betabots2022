import wpilib
import commands2
from constants import Ports


class Tireur(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.motor_tireur = wpilib.PWMVictorSPX(Ports.port_moteur_tireur)
        self.motor_twist = wpilib.PWMVictorSPX(Ports.port_moteur_twist)

    def tirer(self, speed_tirer, speed_twist):
        self.motor_tireur.set(speed_tirer)
        self.motor_twist.set(speed_tirer)

    def stop(self):
        self.motor_tireur.stopMotor()
        self.motor_twist.stopMotor()
