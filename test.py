from ultralytics import YOLO
model = YOLO("yolov8n.pt")
print("Model loaded successfully!")
print("Class names:", model.names)