from networktables.util import ntproperty


class Ports:
    """
    Convention : sous_systeme + _ + composante
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

    tirer_speed_court = ntproperty("/Proprietes/Tirer/tirer_speed_court", 0.2, writeDefault=True)
    tirer_speed_long = ntproperty("/Proprietes/Tirer/tirer_speed_long", 0.5, writeDefault=True)
    twist_speed = ntproperty("/Proprietes/Tirer/shake_speed", 1, writeDefault=True)

    tirer_temps_court = ntproperty("/Proprietes/Tirer/tirer_temps_court", 2, writeDefault=True)
    tirer_temps_loin = ntproperty("/Proprietes/Tirer/tirer_temps_loin", 1, writeDefault=True)

Proprietes = _Proprietes()
