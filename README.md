# Gesture Controlled Mouse

A gesture-controlled mouse using OpenCV and MediaPipe that allows users to control their computer cursor using hand gestures.

## 🎯 Goal
Build a high-performance, user-friendly application that replaces traditional mouse control with hand gestures captured through webcam.

## 🚀 Current Progress 

### Completed Features
- ✅ **Hand Detection Module** 
  - Real-time hand tracking using MediaPipe
  - Supports up to 2 hands detection
  - FPS counter for performance monitoring
  - Landmark position extraction (21 points per hand)
  
- ✅ **Gesture Recognition Module** 
  - Distance calculation between landmarks
  - Left click gesture (thumb + index finger pinch)
  - Right click gesture (thumb + middle finger pinch)
  - Default move gesture for cursor control
  - 30-pixel threshold for pinch detection
  
- ✅ **Testing Infrastructure**
  - Visual feedback for gesture detection
  - Color-coded gesture indicators
  - Real-time FPS monitoring

### Project Structure
```
gesture-mouse/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── hand_detector.py
│   │   └── gesture_recognizer.py
│   └── __init__.py
├── venv/
├── test_hand_detector.py
├── test_gesture_recognizer.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Technologies Used
- **Python 3.x**
- **OpenCV** (4.8.1.78) - Computer vision and image processing
- **MediaPipe** (0.10.8) - Google's hand tracking solution
- **NumPy** (1.24.3) - Numerical computations
- **PyAutoGUI** (0.9.54) - Mouse control automation

## 🔧 Installation

1. Clone the repository
```bash
git clone git@github.com:Hameed1117/Gesture-Controlled-Mouse.git
cd gesture-mouse
```

2. Create virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Test the installation
```bash
python test_hand_detector.py  # Test hand detection
python test_gesture_recognizer.py  # Test gesture recognition
```

## 🎮 Current Gestures
| Gesture | Action | How to Perform |
|---------|--------|----------------|
| Move | Move cursor | Open hand |
| Left Click | Left mouse click | Pinch thumb + index finger |
| Right Click | Right mouse click | Pinch thumb + middle finger |

## 📋 TODO - Next Steps

1. **Complete Gesture Recognition** 
   - [ ] Scroll gesture (two fingers up/down movement)
   - [ ] Drag gesture (closed fist)
   - [ ] Gesture smoothing for stability

2. **Mouse Controller Module** 
   - [ ] Screen coordinate mapping (camera to screen)
   - [ ] Smooth cursor movement with position averaging
   - [ ] Click, drag, and scroll implementation
   - [ ] Movement sensitivity controls

3. **Main Application** 
   - [ ] Integration of all modules
   - [ ] Start/stop controls
   - [ ] Performance optimization

4. **User Interface**
   - [ ] Settings panel for sensitivity adjustment
   - [ ] Visual feedback overlay
   - [ ] System tray integration

5. **Deployment**
   - [ ] Package as standalone executable
   - [ ] Create installer for Windows
   - [ ] User documentation

## 🏗️ Architecture Overview
- **Modular Design**: Separate modules for detection, recognition, and control
- **Real-time Processing**: Optimized for <30ms latency
- **Configurable**: Adjustable sensitivity and gesture thresholds
- **Visual Feedback**: Color-coded gesture indicators for user guidance

## 🐛 Known Issues
- Pinch detection threshold may need adjustment based on camera distance
- FPS may vary based on system performance

