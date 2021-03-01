import cv2


class CameraConnector:
    def __init__(self):
        self.__capture = None
    
    def init_capture(self, username, password, camera_ip, rtsp_port, fps=10):
        conncection_link = self.__create_connection_link(username, password, camera_ip, rtsp_port)
        self.__create_capture(conncection_link, fps)

    def get_frame(self):
        ret, frame = self.__capture.read()
        return frame if ret else None

    def close_capture(self):
        if self.__capture is not None:
            self.__capture.release()

    @staticmethod
    def __create_connection_link(username, password, camera_ip, rtsp_port):
        connection_link = f'rtsp://{username}:{password}@{camera_ip}:{rtsp_port}/Streaming/Channels/1'
        return connection_link
    
    def __create_capture(self, connection_link, fps):
        self.__capture = cv2.VideoCapture(connection_link)
        self.__capture.set(cv2.CAP_PROP_FPS, fps)
    
    # def __del__(self):
    #     self.close_capture()