# Import the camera server
from cscore import CameraServer

# Import OpenCV and NumPy
import cv2
import numpy as np
from networktables import NetworkTables

import constants


def main():
    NetworkTables.initialize(server="10.55.28.2")
    cs = CameraServer.getInstance()
    cs.enableLogging()

    # Capture from the first USB Camera on the system
    camera = cs.startAutomaticCapture()

    # Get a CvSink. This will capture images from the camera
    cv_sink = cs.getVideo()

    # (optional) Setup a CvSource. This will send images back to the Dashboard
    outputStream = cs.putVideo("Camera", 320, 240)

    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(320, 240, 3), dtype=np.uint8)

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        time, img = cv_sink.grabFrame(img)
        if time == 0:
            # Send the output the error.
            outputStream.notifyError(cv_sink.getError())
            # skip the rest of the current iteration
            continue

        #
        # Insert your image processing logic here!
        #
        cv2.line(img, [constants.Proprietes.vision_ligne_gauche], [constants.Proprietes.vision_ligne_droit], (0, 255, 0), 2)
        cv2.line(img, [constants.Proprietes.vision_ligne_gauche, 0], [constants.Proprietes.vision_ligne_droite], (0, 255, 0), 2)

        # (optional) send some image back to the dashboard
        outputStream.putFrame(img)
