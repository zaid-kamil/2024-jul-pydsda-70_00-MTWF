import cv2

def add_filters(frame):
    bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('bw_frame', bw_frame)
    cv2.imshow('rgb_frame', rgb_frame)
    return frame

def read_video(path):
    video = cv2.VideoCapture(path)
    while True:
        state, frame = video.read()
        if not state:
            break
        frame = add_filters(frame)
        cv2.imshow('frame', frame)          # display the frame
        if cv2.waitKey(10) == ord('q'):      # if you pressed 'q', 
            break                           # then quit
    video.release()                         # free the object
    cv2.destroyAllWindows()                 # close the window

# execute outside function
if __name__ == "__main__":
    read_video(r"C:\Users\ZAID\Videos\obama.mp4")   

