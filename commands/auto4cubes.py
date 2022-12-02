from subsystems.basepilotable import BasePilotable
from subsystems.tireur import Tireur
from commands.avancer import Avancer
from commands.tourner import Tourner
from commands.tirerproche import TirerProche
import commands2

class Auto4Cubes(commands2.SequentialCommandGroup):
    def __init__(self, base_pilotable: BasePilotable, tireur: Tireur):
        super().__init__(
            commands2.SequentialCommandGroup(
                commands2.WaitCommand(0.5),
                #avancer: dist. x, dist. y, vitesse
                #tourner: angle, vitesse

                #aller chercher les cubes:
                Avancer(base_pilotable, -46, 0, -0.5),
                Avancer(base_pilotable, 0, 66, 0.5),
                Avancer(base_pilotable, 60, 0, 0.5),
                Tourner(base_pilotable, 90, 0.5),
                Avancer(base_pilotable, 130, 0, 0.5),
                Tourner(base_pilotable, 90, 0.5),
                Avancer(base_pilotable, 60, 0, 0.5),

                #aller porter les cubes vers l'accumulateur:
                Avancer(base_pilotable, 265, 0, 0.5),
                #placer les cubes:
                Avancer(base_pilotable, 0, 30, 0.5),
                TirerProche(tireur),
                Avancer(base_pilotable, 0, 15, 0.5),
                TirerProche(tireur),
                Avancer(base_pilotable, 0, 15, 0.5),
                TirerProche(tireur),
                Avancer(base_pilotable, 0, 15, 0.5 ),
                TirerProche(tireur),

            ),
        )
        self.setName(Auto4Cubes)
