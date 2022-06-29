from imageai.Detection import VideoObjectDetection
import cv2
import os
import random


class HumanVideoDetection:
    """Detection of humans in a video

    Attributes:
        video_path (str, optional): path to the input video
        output_path (str, optional): path to the output folder
        model: (str, optional): path to the model
    """

    def __init__(
        self,
        input_path: str = "input_videos/miss_dior_hd.mp4",
        model: str = "yolo",
        detection_speed: str = "flash",
    ):
        self.input_path = input_path
        self.output_path = "output_videos/"
        self.model = model
        self.detection_speed = detection_speed
        self.boxes = []
        self.colors = []
        self.fps = None

    def get_boxes_video(self):
        """
        Read a video and perform human detection. Store the rectangle boxes in self.boxes
        """
        # Open video
        video = cv2.VideoCapture(self.input_path)
        self.fps = video.get(cv2.CAP_PROP_FPS)

        # Load detector and choose model
        detector = VideoObjectDetection()
        if self.model == "yolo":
            detector.setModelTypeAsYOLOv3()
            detector.setModelPath("models/yolo.h5")
        elif self.model == "tiny-yolo":
            detector.setModelTypeAsYOLOv3()
            detector.setModelPath("models/yolo-tiny.h5")
        else:
            raise ValueError("Unknown model name")
        detector.loadModel(detection_speed=self.detection_speed)

        # Detect only humans
        custom_objects = detector.CustomObjects(person=True)

        def forFull(output_arrays, count_arrays, average_output_count):
            self.boxes.append(output_arrays)

        # Run detection using the model. Store video
        _ = detector.detectObjectsFromVideo(
            input_file_path=self.input_path,
            output_file_path=os.path.join(self.output_path, "yolo_output"),
            frames_per_second=self.fps,
            log_progress=True,
            video_complete_function=forFull,
            return_detected_frame=True,
        )

    def draw_boxes_video(self):
        """
        Read the video and draw the rectangle boxes stored in self.boxes
        """
        # Read video
        cap = cv2.VideoCapture(self.input_path)
        width_cap = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height_cap = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Output video
        video_name = os.path.split(self.input_path)[-1].split(".")[0]
        output = cv2.VideoWriter(
            os.path.join(self.output_path, f"{video_name}_output.avi"),
            cv2.VideoWriter_fourcc(*"MPEG"),
            self.fps,
            (width_cap, height_cap),
        )
        idx = 0
        # For each frame
        while cap.isOpened():
            ret, frame = cap.read()
            # If frame is valid
            if ret:
                data = self.boxes[0][idx]
                # Get every objects that have been detected on the frame
                color_idx = 0
                for n, detected_person in enumerate(data):
                    # Change color for every person
                    if color_idx >= len(self.colors):
                        # Generate color
                        self.colors.append(random.choices(range(256), k=3))
                    color = self.colors[color_idx]
                    # Assure it is person and draw rectangle
                    if detected_person["name"] == "person":
                        cv2.rectangle(
                            frame,
                            (
                                detected_person["box_points"][0],
                                detected_person["box_points"][1],
                            ),
                            (
                                detected_person["box_points"][2],
                                detected_person["box_points"][3],
                            ),
                            color,
                            2,
                        )
                        color_idx+=1    # Change color only when humain rectangle is drawn

                # Write frame to output
                output.write(frame)
                idx += 1
            else:
                cap.release()

        cv2.destroyAllWindows()
        output.release()

    def human_detection(self):
        """
        Perform human detection on the video
        """
        self.get_boxes_video()
        self.draw_boxes_video()
