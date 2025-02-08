import cv2
import ntcore
from pupil_apriltags import Detector

class MultiCamApriltagCenterer:    
    def __init__(self,
                 camera_count,
                 table="jetson",
                 cam_topic="/jetson/cam_mode"
                 ):
        # Initialize NetworkTables subscriber for camera index
        inst = ntcore.NetworkTableInstance.getDefault()
        table = inst.getTable(table)
        cam_topic = table.getIntegerTopic(cam_topic)
        self.cam_topic_sub = cam_topic.subscribe(-1)

        # Initialize cameras
        self.camera_count = camera_count
        for i in range(camera_count):
            cams[i] = cv2.VideoCapture(i)

        # Initialize apriltag detector
        self.apriltag_detector = Detector(
            families="tag36h11",
            nthreads=1,
            quad_decimate=1.0,
            quad_sigma=0.0,
            refine_edges=1,
            decode_sharpening=0.25,
            debug=0
        )
