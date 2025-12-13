# Emotion Detection using AI

This project demonstrates real-time emotion detection using Artificial Intelligence with Python, OpenCV, and the DeepFace library.  
It captures live video from a webcam and identifies the dominant emotion of any detected face, displaying the emotion label along with its confidence percentage.

## Technologies Used
- Python  
- OpenCV (opencv-python)  
- DeepFace (deepface)  

## Features
- Real-time video processing using webcam  
- Face detection with emotion recognition  
- Displays emotion label with confidence percentage  
- Draws bounding box around detected face  
- Handles frames even when no face is detected (`enforce_detection=False`)  

## Emotions Recognized
- Angry  
- Disgust  
- Fear  
- Happy  
- Sad  
- Surprise  
- Neutral  

## Folder Structure
```text
EmotionDetectionUsingAIProject/
│
├── emotion_detection.py
├── Screenshot*.png          # Output screenshots
├── requirements.txt
└── README.md
```

## How It Works
1. The webcam captures live video frames.  
2. DeepFace analyzes each frame to detect human faces.  
3. The dominant emotion is identified for each detected face.  
4. A green rectangle is drawn around the face with the emotion label and confidence percentage.  

## Install Required Libraries
```bash
pip install opencv-python
pip install deepface
```

## Run the Project
```bash
python emotion_detection.py
```

## Project Use Cases
- Emotion-aware AI systems  
- Human–Computer Interaction  
- Mental health monitoring  
- Computer Vision learning projects  
