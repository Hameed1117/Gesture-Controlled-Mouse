import math


class GestureRecognizer:
    def __init__(self):
        # Define finger tip indices from MediaPipe
        self.THUMB_TIP = 4  # Thumb tip landmark index
        self.INDEX_TIP = 8  # Index finger tip landmark index
        self.MIDDLE_TIP = 12  # Middle finger tip landmark index
        
        # Pinch detection threshold
        self.PINCH_THRESHOLD = 30  # Distance in pixels to consider fingers touching
        
    def calculate_distance(self, p1, p2):
        # Calculate distance between two points
        # p1 and p2 are in format [id, x, y]
        x1, y1 = p1[1], p1[2]  # Extract x,y from first point
        x2, y2 = p2[1], p2[2]  # Extract x,y from second point
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Pythagorean theorem
        return distance
        
    def recognize_gesture(self, landmarks):
        # Check if we have all landmarks
        if not landmarks or len(landmarks) < 21:
            return "none"
        
        # Get finger tip landmarks
        thumb_tip = landmarks[self.THUMB_TIP]  # Get thumb tip position
        index_tip = landmarks[self.INDEX_TIP]  # Get index finger tip position
        middle_tip = landmarks[self.MIDDLE_TIP]  # Get middle finger tip position
        
        # Calculate distances between thumb and other fingers
        thumb_index_distance = self.calculate_distance(thumb_tip, index_tip)  # For left click
        thumb_middle_distance = self.calculate_distance(thumb_tip, middle_tip)  # For right click
        
        # Check which gesture is being performed
        # Check order matters - most specific gestures first
        if thumb_index_distance < self.PINCH_THRESHOLD:  # Thumb touching index finger
            return "left_click"  # This is a left click gesture
        elif thumb_middle_distance < self.PINCH_THRESHOLD:  # Thumb touching middle finger
            return "right_click"  # This is a right click gesture
        else:
            return "move"  # Default - just moving the cursor