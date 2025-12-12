

#PROJECT: Emotion Detection using AI

import cv2 #Library: OpenCv : pip install opencv-python  # OpenCV :for webcam + image processing
from deepface import DeepFace  #Library : DeepFace : pip install deepface  #DeepFace: a powerful deep learning library for face/emotion analysis

cap = cv2.VideoCapture(0) # Start video capture (webcam)

while True:
    r, frame = cap.read() #r: r is True if frame is read correctly #frame contains the actual image data #cap.read() reads one frame from the webcam.

    if not r:
        break #Breaks the loop if webcam is not giving video frames.

    try:
        # Detect emotion
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        '''
        DeepFace.analyze(...): Detects all faces in the frame and returns their emotions
        actions=['emotion']: Only detect emotions, not age/gender/etc
        enforce_detection=False: Prevents crashing if face is not clearly visible
        '''

        for result in results:
            x, y, w, h = result['region']['x'], result['region']['y'], result['region']['w'], result['region']['h']
            # face bounding box (top-left (x, y), width (w) and height (h)) 

            emotion = result['dominant_emotion'] #dominant_emotion: the most likely emotion (e.g., "happy", "sad")
            confidence = result['emotion'][emotion]  #result['emotion'][emotion]: gets the confidence score of that emotion (in %)

            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            '''
            (x, y): Top-left corner of the bounding box
            (x + w, y + h): Bottom-right corner
            (0, 255, 0): Color of the rectangle in BGR format (green in this case)
            2: Thickness of the rectangle border
            '''

            # Display emotion and confidence
            text = f'{emotion} ({confidence:.2f}%)'
            '''
            emotion: The detected emotion label (e.g., "Happy", "Sad")
            confidence: The prediction confidence (e.g., 93.56), formatted to 2 decimal places
            '''
            
            # Display emotion
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            '''
            cv2.putText: Writes text on the image
            (x, y - 10): Position of the text
            cv2.FONT_HERSHEY_SIMPLEX: Font style
            0.9: Font size (scale)
            2: Thickness of the text
            '''

    except Exception as e:
        #  no face detected),
        print("Error:", e)

    # Show the result frame
    cv2.imshow("Real-Time Emotion Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #Stops webcam
cv2.destroyAllWindows() # Closes OpenCV windows
print("Webcam stopped. Program exited.")

=======


#PROJECT: Emotion Detection using AI

import cv2 #Library: OpenCv : pip install opencv-python  # OpenCV :for webcam + image processing
from deepface import DeepFace  #Library : DeepFace : pip install deepface  #DeepFace: a powerful deep learning library for face/emotion analysis

cap = cv2.VideoCapture(0) # Start video capture (webcam)

while True:
    r, frame = cap.read() #r: r is True if frame is read correctly #frame contains the actual image data #cap.read() reads one frame from the webcam.

    if not r:
        break #Breaks the loop if webcam is not giving video frames.

    try:
        # Detect emotion
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        '''
        DeepFace.analyze(...): Detects all faces in the frame and returns their emotions
        actions=['emotion']: Only detect emotions, not age/gender/etc
        enforce_detection=False: Prevents crashing if face is not clearly visible
        '''

        for result in results:
            x, y, w, h = result['region']['x'], result['region']['y'], result['region']['w'], result['region']['h']
            # face bounding box (top-left (x, y), width (w) and height (h)) 

            emotion = result['dominant_emotion'] #dominant_emotion: the most likely emotion (e.g., "happy", "sad")
            confidence = result['emotion'][emotion]  #result['emotion'][emotion]: gets the confidence score of that emotion (in %)

            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            '''
            (x, y): Top-left corner of the bounding box
            (x + w, y + h): Bottom-right corner
            (0, 255, 0): Color of the rectangle in BGR format (green in this case)
            2: Thickness of the rectangle border
            '''

            # Display emotion and confidence
            text = f'{emotion} ({confidence:.2f}%)'
            '''
            emotion: The detected emotion label (e.g., "Happy", "Sad")
            confidence: The prediction confidence (e.g., 93.56), formatted to 2 decimal places
            '''
            
            # Display emotion
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            '''
            cv2.putText: Writes text on the image
            (x, y - 10): Position of the text
            cv2.FONT_HERSHEY_SIMPLEX: Font style
            0.9: Font size (scale)
            2: Thickness of the text
            '''

    except Exception as e:
        #  no face detected),
        print("Error:", e)

    # Show the result frame
    cv2.imshow("Real-Time Emotion Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #Stops webcam
cv2.destroyAllWindows() # Closes OpenCV windows
print("Webcam stopped. Program exited.")

