import easyocr
import os
import pyttsx3
import cv2

cap = cv2.VideoCapture(0)
last_text = ""
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
reader = easyocr.Reader(['en'])
while True:
    ret, frame = cap.read()
    if not ret:
        print("webcam error")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = reader.readtext(gray, detail=0)
    print(result)
    if result:
        result = " ".join(result)
        print("Detected:", result)
    if result != last_text:
        last_text = result
        engine.say(result)
        engine.runAndWait()
        engine.save_to_file("ouput.mp3")
        engine.runAndWait()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()