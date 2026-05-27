import imageio
import cv2
import numpy as np

reader = imageio.get_reader(r"D:\user_profile\Desktop\Boat_detection\input\boat.mp4")
fps = reader.get_meta_data()['fps']

out = cv2.VideoWriter(
    r"D:\user_profile\Desktop\Boat_detection\input\boat_fixed.mp4",
    cv2.VideoWriter_fourcc(*"XVID"), fps, (640, 360))

for frame in reader:
    frame_bgr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    frame_resized = cv2.resize(frame_bgr, (640, 360))
    out.write(frame_resized)

out.release()
print("Done! boat_fixed.mp4 created!")