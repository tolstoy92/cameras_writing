import os
import cv2
import json
import atexit
import numpy as np
from time import time
from src.cameraconnector import CameraConnector
from src.videowriter import VideoWriter
from src.writercontroller import VideoWriterController


SINGLE_WRITING_DURATION = 30

FPS = 20 
DOWNSLACE_FACTOR = 2
RESOLUTION = (2*1280//DOWNSLACE_FACTOR, 720//DOWNSLACE_FACTOR) 

DIR_TO_SAVE = os.path.join(os.getcwd(), 'data_to_save')

with open('connect_data.json', 'r') as connection_file:
    connection_data = json.load(connection_file)

camera1 = CameraConnector()
camera2 = CameraConnector()


writer_controller = VideoWriterController(SINGLE_WRITING_DURATION, DIR_TO_SAVE, FPS, RESOLUTION)


@atexit.register
def close():
    camera1.close_capture()
    camera2.close_capture()
    writer_controller.close_writer()
    cv2.destroyAllWindows()


camera1.init_capture(
    connection_data['username'],
    connection_data['password'],
    connection_data['cam1_ip'],
    connection_data['rtsp_port'],
    fps=FPS
)
camera2.init_capture(
    connection_data['username'],
    connection_data['password'],
    connection_data['cam2_ip'],
    connection_data['rtsp_port'],
    fps=FPS
)
writer_controller.init_writer()

while True:
    frame1 = camera1.get_frame()
    frame2 = camera2.get_frame()

    result = np.hstack([frame1, frame2])
    result = cv2.resize(result, RESOLUTION)

    writer_controller.write_frame(result)
    if writer_controller.writing_time_is_end():
        writer_controller.reload_writer()
        
close()
