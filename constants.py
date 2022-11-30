from networktables.util import ntproperty


class Ports:
    """
    Convention : sous_systeme + _ + composante
    """

    # CAN
    base_pilotable_moteur_fl = 2
    base_pilotable_moteur_fr = 3
    base_pilotable_moteur_rl = 1
    base_pilotable_moteur_rr = 4

    shooter_ultrasound_left = 4
    shooter_ultrasound_right = 5

    # PWM
    tireur_moteur = 0
    tireur_moteur_twist = 1

    # DIO
    ...


class _Proprietes:
    pilotage_max_x = ntproperty("/Proprietes/PilotageMaxX", 0.4, writeDefault=False)
    pilotage_max_y = ntproperty("/Proprietes/PilotageMaxY", 0.4, writeDefault=False)
    pilotage_max_z = ntproperty("/Proprietes/PilotageMaxZ", 0.2, writeDefault=False)
    pilotage_deadzone = ntproperty("/Proprietes/PilotageDeadzone", 0.05, writeDefault=False)

    tireur_twist_speed = ntproperty("/Proprietes/Tireur/Twist_speed", 1, writeDefault=True)
    tireur_speed_proche = ntproperty("/Proprietes/Tireur/Speed_proche", -0.2, writeDefault=True)
    tireur_speed_loin = ntproperty("/Proprietes/Tireur/Speed_loin", -0.5, writeDefault=True)


    aligner_threshold = ntproperty("/Proprietes/Tirer/aligner_threshold", 0.5, writeDefault=True)
    aligner_vitesse = ntproperty("/Proprietes/Tirer/aligner_vitesse", 0.1, writeDefault=True)
    aligner_distance = ntproperty("/Proprietes/Tirer/aligner_distance", 0.1, writeDefault=True)



Proprietes = _Proprietes()
