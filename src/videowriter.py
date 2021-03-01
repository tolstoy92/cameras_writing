import os
import cv2
from datetime import datetime


class VideoWriter:
    def __init__(self):
        self.__video_writer = None

    def init_writer(self, dir_to_write, fps=20, resolution=(640, 480), camera_num=None):
        dst_folder = self.__create_dirname()
       
        dst_fname = self.__create_fname()
        if not os.path.exists(os.path.join(dir_to_write, dst_folder)):
            os.mkdir(os.path.join(dir_to_write, dst_folder))

        if camera_num:
            sub_dir_name = f'camera_{camera_num}'
            if not os.path.exists(os.path.join(dir_to_write, dst_folder, sub_dir_name)):
                os.mkdir(os.path.join(dir_to_write, dst_folder, sub_dir_name))

            full_path_to_save = os.path.join(dir_to_write, dst_folder, sub_dir_name, dst_fname)
        else:
            full_path_to_save = os.path.join(dir_to_write, dst_folder, dst_fname)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        # fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        # fourcc = cv2.VideoWriter_fourcc(*'H624')
        self.__video_writer = cv2.VideoWriter(full_path_to_save, fourcc, fps, resolution)

    def write_frame(self, frame):
        self.__video_writer.write(frame)
    
    def close_writer(self):
        self.__video_writer.release()

    @staticmethod
    def __create_fname():
        current_date = datetime.now()
        start_time = current_date.strftime('%H:%M')
        return f'{start_time}.avi'
        # return f'{start_time}.mp4'
    
    @staticmethod
    def __create_dirname():
        current_date = datetime.now()
        current_date_str = current_date.strftime('%d_%m_%Y')
        return current_date_str

    # def __del__(self):
    #     self.close_writer()