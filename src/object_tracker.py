import cv2
from ultralytics import YOLO


class ObjectTracker:
    """
    Real-time object detection and tracking using YOLO and OpenCV.
    """

    def __init__(self, model_path="yolo11n.pt"):
        self.model = YOLO(model_path)

    def run(self, camera_index=0):
        """
        Start webcam-based object detection and tracking.
        """

        cap = cv2.VideoCapture(camera_index)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        print("Object detection started.")
        print("Press 'q' to quit.")

        while True:
            success, frame = cap.read()

            if not success:
                print("Error: Could not read frame.")
                break

            # YOLO object detection + tracking
            results = self.model.track(
                source=frame,
                persist=True,
                conf=0.40,
                verbose=False
            )

            # Draw detections and tracking IDs
            annotated_frame = results[0].plot()

            cv2.imshow(
                "CodeAlpha - Object Detection and Tracking",
                annotated_frame
            )

            # Press q to exit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    tracker = ObjectTracker()
    tracker.run()