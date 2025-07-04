import cv2
from src.core.hand_detector import HandDetector
from src.core.gesture_recognizer import GestureRecognizer

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam

# Create detector and recognizer objects
detector = HandDetector()  # Your existing hand detector
recognizer = GestureRecognizer()  # Your new gesture recognizer

# Variables for visual feedback
click_feedback_timer = 0  # Timer to show click feedback
click_type = ""  # Store type of click for display

while True:
    # Read frame from webcam
    success, frame = cap.read()  # success = True/False, frame = image
    
    if success:
        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)  # 1 = horizontal flip
        
        # Detect hands and draw landmarks
        frame = detector.find_hands(frame)  # Draws hand skeleton
        
        # Get landmark positions
        landmarks = detector.find_position(frame)  # Returns list of 21 points
        
        # Recognize gesture if hand found
        if landmarks:  # If landmarks list is not empty
            gesture = recognizer.recognize_gesture(landmarks)  # Get gesture name
            
            # Check if a click was detected
            if gesture == "left_click":  # Thumb-index pinch detected
                click_feedback_timer = 30  # Show feedback for 30 frames
                click_type = "LEFT CLICK!"  # Set feedback text
            elif gesture == "right_click":  # Thumb-middle pinch detected
                click_feedback_timer = 30  # Show feedback for 30 frames
                click_type = "RIGHT CLICK!"  # Set feedback text
            
            # Display current gesture with colored background
            gesture_color = (0, 255, 0)  # Default green
            if gesture == "left_click":
                gesture_color = (0, 255, 255)  # Yellow for left click
            elif gesture == "right_click":
                gesture_color = (0, 165, 255)  # Orange for right click
            
            # Draw gesture status box
            cv2.rectangle(frame, (10, 10), (300, 70), (0, 0, 0), -1)  # Black background
            cv2.rectangle(frame, (10, 10), (300, 70), gesture_color, 2)  # Colored border
            cv2.putText(frame, f"Gesture: {gesture}",  # Text to display
                       (20, 45),  # Position inside box
                       cv2.FONT_HERSHEY_SIMPLEX,  # Font type
                       0.8,  # Font scale
                       gesture_color,  # Matching color
                       2)  # Thickness
            
            # Display pinch instructions with icons
            # Left click instruction
            cv2.putText(frame, "Thumb + Index = Left Click",  # Instruction text
                       (10, 100),  # Position
                       cv2.FONT_HERSHEY_SIMPLEX,  # Font type
                       0.6,  # Smaller font scale
                       (0, 255, 255),  # Yellow color
                       1)  # Thinner line
            
            # Right click instruction
            cv2.putText(frame, "Thumb + Middle = Right Click",  # Instruction text
                       (10, 130),  # Position
                       cv2.FONT_HERSHEY_SIMPLEX,  # Font type
                       0.6,  # Smaller font scale
                       (0, 165, 255),  # Orange color
                       1)  # Thinner line
            
            # Draw visual indicators on the actual fingers when pinching
            if landmarks:
                # Get finger positions for visual feedback
                thumb_tip = landmarks[4]  # Thumb tip position
                index_tip = landmarks[8]  # Index tip position
                middle_tip = landmarks[12]  # Middle tip position
                
                if gesture == "left_click":
                    # Draw circles on thumb and index when pinching
                    cv2.circle(frame, (int(thumb_tip[1]), int(thumb_tip[2])), 15, (0, 255, 255), -1)  # Yellow circle on thumb
                    cv2.circle(frame, (int(index_tip[1]), int(index_tip[2])), 15, (0, 255, 255), -1)  # Yellow circle on index
                    # Draw line between them
                    cv2.line(frame, (int(thumb_tip[1]), int(thumb_tip[2])), 
                            (int(index_tip[1]), int(index_tip[2])), (0, 255, 255), 3)  # Yellow line
                            
                elif gesture == "right_click":
                    # Draw circles on thumb and middle when pinching
                    cv2.circle(frame, (int(thumb_tip[1]), int(thumb_tip[2])), 15, (0, 165, 255), -1)  # Orange circle on thumb
                    cv2.circle(frame, (int(middle_tip[1]), int(middle_tip[2])), 15, (0, 165, 255), -1)  # Orange circle on middle
                    # Draw line between them
                    cv2.line(frame, (int(thumb_tip[1]), int(thumb_tip[2])), 
                            (int(middle_tip[1]), int(middle_tip[2])), (0, 165, 255), 3)  # Orange line
        
        # Show click feedback popup
        if click_feedback_timer > 0:  # If we should show feedback
            # Calculate center position for popup
            center_x = frame.shape[1] // 2  # Half of frame width
            center_y = frame.shape[0] // 2  # Half of frame height
            
            # Draw colored rectangle as background
            if "LEFT" in click_type:
                cv2.rectangle(frame, (center_x - 120, center_y - 40), 
                             (center_x + 120, center_y + 40), (0, 255, 255), -1)  # Yellow box
            else:
                cv2.rectangle(frame, (center_x - 120, center_y - 40), 
                             (center_x + 120, center_y + 40), (0, 165, 255), -1)  # Orange box
            
            # Draw click text
            cv2.putText(frame, click_type,  # Click type text
                       (center_x - 80, center_y + 10),  # Centered position
                       cv2.FONT_HERSHEY_SIMPLEX,  # Font type
                       1.2,  # Larger font
                       (0, 0, 0),  # Black text
                       3)  # Thick text
            
            click_feedback_timer -= 1  # Decrease timer each frame
        
        # Show FPS - FIXED: Pass frame to find_fps()
        fps = detector.find_fps(frame)  # Get FPS from detector with frame parameter
        
        # Show the frame
        cv2.imshow("Gesture Test - Pinch Control", frame)  # Window name and image
    
    # Check for 'q' key press to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):  # waitKey(1) = wait 1ms for key
        break  # Exit the loop

# Clean up
cap.release()  # Release webcam
cv2.destroyAllWindows()  # Close all OpenCV windows