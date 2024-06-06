# Customer Face Recognition System

## Introduction
This Python script uses OpenCV for real-time face detection in a restaurant drive-through scenario. Captured faces are saved as images and uploaded to AWS S3 for storage and analysis.

### Brief History of OpenCV
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It was initially developed by Intel in 1999 and has since been continuously improved by a vast community of developers. OpenCV provides a wide range of functions for real-time computer vision applications.

### How OpenCV Works
OpenCV allows for the manipulation and analysis of visual data, such as images and videos, through its extensive set of functions and algorithms. It provides tools for tasks like image processing, object detection, feature extraction, and more. OpenCV is written in C++ and has Python bindings for easy integration with Python applications.

### Haar Cascade Classifier
The Haar Cascade classifier is a machine learning-based approach used for object detection in images. It works by training a cascade function with positive and negative images to identify objects based on their features. In this code, the `haarcascade_frontalface_default.xml` file contains pre-trained data for detecting frontal faces in images.

### Use-Cases for This Code
1. **Restaurant Drive-Through:** Identify and capture customer faces for personalized service or security purposes in a restaurant drive-through setting.
2. **Security Systems:** Implement facial recognition for access control or surveillance systems.
3. **Customer Analytics:** Analyze customer demographics or behavior based on captured faces.
4. **Personalized Marketing:** Tailor marketing strategies based on customer facial recognition data.
5. **Attendance Systems:** Automate attendance tracking using facial recognition technology.

## Prerequisites
- Python 3.x
- OpenCV
- Boto3
- AWS S3 Bucket

## Setup
1. Install the required libraries using `pip install opencv-python boto3`.
2. Place the `haarcascade_frontalface_default.xml` file in the same directory.
3. Replace `YOUR_ACCESS_KEY` and `YOUR_SECRET_KEY` with your AWS IAM user credentials.
4. Adjust the `limit_faces` variable to set the limit for the number of customer faces to capture.
5. Adjust the `time_limit` variable to set wait time in seconds before initiating new capture from camera.
6. Run the script and ensure your webcam is correctly configured.

## Usage
- Ensure good lighting conditions for optimal face detection.
- Press 'q' to exit the program.

## Notes
- Captured faces are stored in the `captured_faces` directory.
- Uploaded faces are stored in the specified AWS S3 bucket.

Feel free to reach out if you need further assistance or modifications to the code! 