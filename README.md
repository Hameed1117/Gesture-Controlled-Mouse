# Gesture Controlled Mouse

A gesture-controlled mouse using OpenCV and MediaPipe that allows users to control their computer cursor using hand gestures.

## 🎯Goal
Build a high-performance, user-friendly application that replaces traditional mouse control with hand gestures captured through webcam.

## 🚀 Current Progress

### Completed Features
- ✅ **Hand Detection Module** (`src/core/hand_detector.py`)
  - Real-time hand tracking using MediaPipe
  - Supports up to 2 hands detection
  - FPS counter for performance monitoring
  - Landmark position extraction (21 points per hand)
  
### Project Structure
```
gesture-mouse/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   └── hand_detector.py
│   └── __init__.py
├── venv/
├── test_hand_detector.py
├── test_setup.py
├── requirements.txt
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
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Test the installation
```bash
python test_hand_detector.py
```

## 📋 TODO - Next Steps

1. **Gesture Recognition Module** 
   - Implement finger counting
   - Click gesture (index finger pinch)
   - Right-click gesture
   - Scroll gesture
   - Drag gesture

2. **Mouse Controller Module**
   - Map hand position to screen coordinates
   - Smooth cursor movement
   - Click actions implementation
   - Sensitivity controls

## 🏗️ Architecture Overview
- **Modular Design**: Separate modules for detection, recognition, and control
- **Real-time Processing**: Optimized for low latency
- **Configurable**: Adjustable sensitivity and gesture settings