try:
    import cv2
    print(f"OpenCV version: {cv2.__version__}")
except ImportError:
    print("OpenCV NOT installed")


    # Test camera
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Camera is accessible")
    cap.release()
else:
    print("Camera NOT accessible")

# Test camera with actual frame capture
cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print("Camera captured a frame successfully")
    cap.release()