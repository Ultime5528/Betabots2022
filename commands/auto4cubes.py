from subsystems.basepilotable import BasePilotable
from subsystems.tireur import Tireur
from commands.avancerx import AvancerX
from commands.tournerX import TournerX
from commands.tirerproche import TirerProche
import commands2


class Auto4Cubes(commands2.SequentialCommandGroup):
    def __init__(self, base_pilotable: BasePilotable, tireur: Tireur):
        self.setName("Auto4Cubes")
        super().__init__(
            commands2.SequentialCommandGroup(
                commands2.WaitCommand(0.5),
                # avancer: dist. x, dist. y, vitesse
                # tourner: angle, vitesse

                # aller chercher les cubes:
                AvancerX(base_pilotable, -46, 0, -0.5),
                AvancerX(base_pilotable, 0, 66, 0.5),
                AvancerX(base_pilotable, 60, 0, 0.5),
                TournerX(base_pilotable, 90, 0.5),
                AvancerX(base_pilotable, 130, 0, 0.5),
                TournerX(base_pilotable, 90, 0.5),
                AvancerX(base_pilotable, 60, 0, 0.5),

                # placer les cubes:
                AvancerX(base_pilotable, 265, 30, 0.5),
                TirerProche(tireur),
                AvancerX(base_pilotable, 0, 15, 0.5),
                TirerProche(tireur),
                AvancerX(base_pilotable, 0, 15, 0.5),
                TirerProche(tireur),
                AvancerX(base_pilotable, 0, 15, 0.5),
                TirerProche(tireur),

            ),
        )
