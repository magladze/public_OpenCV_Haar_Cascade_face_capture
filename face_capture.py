import cv2
import boto3
import os
import time

# Initialize the AWS S3 client
s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

# Initialize the face detection cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture from webcam (adjust the index based on your webcam)
cap = cv2.VideoCapture(1)

# Define the directory to store captured faces
output_dir = 'captured_faces'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the limit to the number of customer faces to capture
limit_faces = 5
face_count = 0

#time limit (seconds) to wait before initiating new capture from camera
time_limit = 1

#see you have reached your set limit
faces_logged = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Save the captured face to a file
        face_filename = os.path.join(output_dir, f'face_{face_count}.jpg')
        cv2.imwrite(face_filename, frame[y:y + h, x:x + w])

        # Upload the captured face to AWS S3
        s3.upload_file(face_filename, 'your-s3-bucket-name', f'captured_faces/face_{face_count}.jpg')

        #sleep for 'time_limit' seconds to ensure that face can also leave the frame and not instantly captured again
        #for sample purposes our code waits for 1 second
        time.sleep(time_limit)

        face_count += 1

        if face_count >= limit_faces:
            faces_logged = True
            break

    cv2.imshow('Customer Face Recognition', frame)

    #if the total number of faces fails to log in the interval, quit by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q') or faces_logged:
        break

cap.release()
cv2.destroyAllWindows()