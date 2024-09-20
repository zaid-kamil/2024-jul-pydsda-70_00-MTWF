import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def process_image(frame, detection):
    frame.flags.writeable = False
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # color conversion
    results = detection.process(frame) # process the image
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)   # color conversion
    frame.flags.writeable = True
    if results.detections:
        for output in results.detections:
            mp_drawing.draw_detection(frame, output)
    return frame

def read_webcam(idx=0):
    with mp_face_detection.FaceDetection() as detection:
        video = cv2.VideoCapture(idx)
        while True:
            state, frame = video.read()
            if not state:
                break
            frame = process_image(frame, detection)
            cv2.imshow('frame', frame)         
            if cv2.waitKey(10) == ord('q'):     
                break                          
        video.release()                        
    cv2.destroyAllWindows()       

# execute outside function
if __name__ == "__main__":
    read_webcam()