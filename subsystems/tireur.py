import wpilib
import commands2
from constants import Ports, Proprietes


class Tireur(commands2.SubsystemBase):
    def __init__(self):
        self.setname("Tireur")
        super().__init__()
        self.motor_tireur = wpilib.PWMVictorSPX(Ports.tireur_moteur)
        self.motor_twist = wpilib.PWMVictorSPX(Ports.tireur_moteur_twist)

    def tirer_loin(self):
        self.motor_tireur.set(Proprietes.tireur_speed_loin)
        self.motor_twist.set(Proprietes.tireur_twist_speed)

    def tirer_proche(self):
        self.motor_tireur.set(Proprietes.tireur_speed_proche)
        self.motor_twist.set(Proprietes.tireur_twist_speed)

    def stop(self):
        self.motor_tireur.stopMotor()
        self.motor_twist.stopMotor()

