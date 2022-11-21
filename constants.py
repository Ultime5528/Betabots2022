from networktables.util import ntproperty


class Ports:
    """
    Convention : ( sous-système ) + _ + ( composante )
    """

    # CAN
    base_pilotable_moteur_fl = 1
    base_pilotable_moteur_fr = 2
    base_pilotable_moteur_rl = 3
    base_pilotable_moteur_rr = 4

    # PWM
    ...

    # DIO
    ...


class _Proprietes:
    pilotage_max_x = ntproperty("/Proprietes/PilotageMaxX", 0.4, writeDefault=False)
    pilotage_max_y = ntproperty("/Proprietes/PilotageMaxY", 0.4, writeDefault=False)
    pilotage_max_z = ntproperty("/Proprietes/PilotageMaxZ", 0.2, writeDefault=False)
    pilotage_deadzone = ntproperty("/Proprietes/PilotageDeadzone", 0.05, writeDefault=False)


Proprietes = _Proprietes()
