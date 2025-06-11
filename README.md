# Emotion Detection using AI 

This project demonstrates real-time emotion detection using AI with Python, OpenCV, and the DeepFace library. It captures video from your webcam and identifies the dominant emotion of any face detected in the frame, displaying the result with confidence percentage.

#Technologies Used

- Python
- OpenCV(`opencv-python`)
- DeepFace(`deepface`)

#Features

- Real-time video processing from webcam
- Emotion detection with bounding box and label
- Displays confidence score for detected emotion
- Handles frames even if no face is detected (`enforce_detection=False`)

#Emotions Recognized

- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral

#How It Works

1. The webcam captures a live frame.
2. DeepFace analyzes the frame to detect any human face(s).
3. It then identifies the dominant emotion on each detected face.
4. A green rectangle is drawn around the face with the emotion label and confidence score.

# Install Required Libraries

1. pip install opencv-python 
2. pip install deepface

