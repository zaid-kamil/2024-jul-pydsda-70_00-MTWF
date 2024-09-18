import cv2
def process_something(frame):
    # do whatever u want here
    return frame

def read_webcam(idx=0):
    # 0 means your default camera
    video = cv2.VideoCapture(idx)
    while True:
        state, frame = video.read()
        if not state:
            break
        frame = process_something(frame)
        cv2.imshow('frame', frame)         
        if cv2.waitKey(10) == ord('q'):     
            break                          
    video.release()                        
    cv2.destroyAllWindows()       

# execute outside function
if __name__ == "__main__":
    read_webcam()