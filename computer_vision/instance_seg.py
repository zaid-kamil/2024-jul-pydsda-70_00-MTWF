import cv2

from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

model = YOLO("yolov8n-seg.pt")
names = model.model.names
cap = cv2.VideoCapture(0)
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, 
                cv2.CAP_PROP_FRAME_HEIGHT, 
                cv2.CAP_PROP_FPS))

out = cv2.VideoWriter("instance-segmentation.avi", 
        cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))
while True:
    status, frame = cap.read()
    if not status:
        break
    results = model.predict(frame)
    annotator = Annotator(frame, line_width=2)
    if results[0].masks is not None:
        clss = results[0].boxes.cls.cpu().tolist()
        masks = results[0].masks.xy
        for mask, cls in zip(masks, clss):
            color = colors(int(cls), True)
            txt_color = annotator.get_txt_color(color)
            try:
                annotator.seg_bbox(mask=mask, mask_color=color,     
                    label=names[int(cls)], txt_color=txt_color)
            except:
                pass
    out.write(frame)
    cv2.imshow("instance-segmentation", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
