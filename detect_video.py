from ultralytics import YOLO
import cv2


model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(r"D:\user_profile\Desktop\Boat_detection\input\boat_fixed.mp4")

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter(r"D:\user_profile\Desktop\Boat_detection\output\result.mp4",
      cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

frame_number = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_number += 1

    
    results = model(frame, classes=[8], conf=0.3, verbose=False)

   
    annotated = results[0].plot()

    count = len(results[0].boxes)
    print(f"Frame {frame_number} → Boats detected: {count}")

    out.write(annotated)

cap.release()
out.release()
print("Done! Open output/result.mp4 to see the result")