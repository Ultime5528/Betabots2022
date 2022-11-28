import wpilib
import commands2
from constants import Ports


class Tireur(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.motor_tireur = wpilib.PWMVictorSPX(Ports.port_moteur_tireur)

    def tirer(self, speed):
        self.motor_tireur.set(speed)

    def stop(self):
        self.motor_tireur.stopMotor()

