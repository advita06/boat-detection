from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
results = model("input/boat.jpg", classes=[8], conf=0.3)
annotated = results[0].plot()
boat_count = len(results[0].boxes)
print(f"Boats detected: {boat_count}")
cv2.imwrite("output/result.jpg", annotated)
print("Result saved to output/result.jpg")
