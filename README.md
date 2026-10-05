\# CodeAlpha Object Detection and Tracking



An AI-based real-time object detection and tracking system developed for the CodeAlpha Artificial Intelligence Internship — Task 4.



\## Features



\- Real-time webcam object detection

\- YOLO object detection model

\- Bounding boxes around detected objects

\- Object class labels

\- Detection confidence scores

\- Object tracking with tracking IDs

\- OpenCV webcam interface



\## Technologies Used



\- Python

\- YOLO

\- Ultralytics

\- OpenCV

\- PyTorch



\## How It Works



1\. OpenCV captures frames from the webcam.

2\. YOLO detects objects in each frame.

3\. Detected objects are displayed with bounding boxes and labels.

4\. YOLO tracking maintains tracking IDs between frames.

5\. The processed video is displayed in real time.



\## Installation



Create and activate a virtual environment:



```powershell

py -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

