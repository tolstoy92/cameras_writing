from time import time
from src.videowriter import VideoWriter


class VideoWriterController:
    def __init__(self, single_write_duration, dir_to_write, fps, resolution):
        self.__single_write_duration = single_write_duration
        self.__dir_to_write = dir_to_write
        self.__fps = fps
        self.__resolution = resolution

        self.__writer = None

        self.__start_time = None

    def init_writer(self):
        self.__writer = VideoWriter()
        self.__writer.init_writer(self.__dir_to_write, self.__fps, self.__resolution)
    
    def close_writer(self):
        self.__writer.close_writer()
    
    def write_frame(self, frame):
        if self.__start_time is None:
            self.__start_time = time()
        self.__writer.write_frame(frame)
    
    def writing_time_is_end(self):
        current_time = time()   
        elapsed_time = current_time - self.__start_time
        elapsed_time_min = elapsed_time / 60.0
        return elapsed_time_min >= self.__single_write_duration
    
    def reload_writer(self):
        self.__start_time = None
        self.close_writer()
        self.init_writer()
