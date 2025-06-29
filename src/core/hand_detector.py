import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        
        
        # Initialize MediaPipe hands module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )
        self.mp_drawing = mp.solutions.drawing_utils

        # FPS calculation variables
        self.prev_time = 0
        self.current_time = 0
        
    def find_hands(self, image, draw=True):
        # Convert BGR to RGB (OpenCV uses BGR, MediaPipe uses RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)
            
            # Check if hands are detected
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_drawing.draw_landmarks(
                        image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )
        return image
    
    def find_fps(self, image):
        self.current_time = time.time()
        fps = 1 / (self.current_time - self.prev_time)
        self.prev_time = self.current_time
        
        # Draw FPS on image
        cv2.putText(image, f"FPS: {int(fps)}", (10, 30), 
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        
        return fps, image
    

    def find_position(self, image, hand_no=0, draw=True):
        landmark_list = []
        
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) > hand_no:
                my_hand = self.results.multi_hand_landmarks[hand_no]
                
                for id, landmark in enumerate(my_hand.landmark):
                    height, width, channels = image.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    landmark_list.append([id, cx, cy])
                    
                    if draw:
                        cv2.circle(image, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        
        return landmark_list