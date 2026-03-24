import cv2
import numpy as np
import os
import database  # <--- NEW: Database file ko import kiya

print("🚀 AI Productivity Monitor + Database Started...")

# --- 1. SETUP ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("❌ Error: Haar Cascade nahi mila!")
    exit()

# --- 2. TRAINING ---
path = "faces/Harsh.jpg"
if not os.path.exists(path):
    print("❌ Error: Photo nahi mili!")
    exit()

try:
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        print("❌ Error: Training photo mein chehra nahi dikha!")
        exit()

    (x, y, w, h) = faces[0]
    face_roi = gray[y:y+h, x:x+w]

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train([face_roi], np.array([1])) 
    print("✅ Training Complete!")

except Exception as e:
    print(f"❌ Error: {e}")
    exit()

# --- 3. CAMERA & LOGGING ---
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)

    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y+h, x:x+w]

        try:
            id_num, confidence = recognizer.predict(roi_gray)

            if confidence < 80:
                name = "Harsh Singh"
                color = (0, 255, 0)
                
                # --- NEW: Database mein likho ---
                database.log_entry(name) 
                # -------------------------------
            else:
                name = "Unknown"
                color = (0, 0, 255)
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 0.9, color, 2)
            
        except Exception as e:
            pass

    cv2.imshow('AI Productivity Monitor', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()