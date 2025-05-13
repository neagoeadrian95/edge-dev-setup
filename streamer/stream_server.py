from flask import Flask, Response
import cv2

app = Flask(__name__)

# === Config ===
USE_WEBCAM = True
VIDEO_FILE_PATH = "test.mp4"
VIDEO_SOURCE = 0 if USE_WEBCAM else VIDEO_FILE_PATH

cap = cv2.VideoCapture(VIDEO_SOURCE)
if not cap.isOpened():
    raise RuntimeError(f"❌ Unable to open video source: {VIDEO_SOURCE}")
else:
    print(f"✅ Video source opened: {VIDEO_SOURCE}")

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            print("⚠️ Frame read failed")
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video')
def video_feed():
    print("📡 Client connected to /video")
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("🚀 Starting video stream at http://0.0.0.0:5050/video")
    app.run(host='0.0.0.0', port=5050)

