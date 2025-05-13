import cv2
import numpy as np

# Video properties
width, height = 640, 480
fps = 20
duration_sec = 5
frames_total = duration_sec * fps

# Output file
output = "test.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, fps, (width, height))

for i in range(frames_total):
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Draw a moving circle
    center_x = int((i / frames_total) * width)
    cv2.circle(frame, (center_x, height // 2), 50, (0, 255, 0), -1)

    # Add frame number text
    cv2.putText(frame, f"Frame {i}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    out.write(frame)

out.release()
print("✅ test.mp4 created.")

