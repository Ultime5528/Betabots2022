from subsystems.basepilotable import BasePilotable
from subsystems.tireur import Tireur
from commands.avancerx import AvancerX
from commands.tournerX import TournerX
from commands.tirerproche import TirerProche
from commands.tirerloin import TirerLoin
import commands2


class Auto4Cubes(commands2.SequentialCommandGroup):
    def __init__(self, base_pilotable: BasePilotable, tireur: Tireur):

        super().__init__(
            commands2.WaitCommand(0.5),
            AvancerX(base_pilotable, 1.00, 0, 0.2, 0),
            TournerX(base_pilotable, -145, 0.25),
            AvancerX(base_pilotable, 1.70, 0, 0.2, 0),
            TournerX(base_pilotable, 97, 0.25),
            AvancerX(base_pilotable, 1.00, 0, 0.2, 0),
            AvancerX(base_pilotable, 3.00, 1.00, 0.2, 0.3),
            AvancerX(base_pilotable, 0.50, 0, 0.1, 0),
            commands2.ParallelRaceGroup(
                TirerLoin(tireur),

                commands2.WaitCommand(2)
            ),
            AvancerX(base_pilotable, 0.20, 0.70, 0.15, 0.3),
            commands2.ParallelRaceGroup(
                TirerProche(tireur),

                commands2.WaitCommand(2)
            ),

        )
        self.setName("Auto4Cubes")