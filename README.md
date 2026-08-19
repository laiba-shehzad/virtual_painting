# Virtual Paint

A Python-based virtual painting application that uses **OpenCV**, **NumPy**, and **MediaPipe** to detect hand movements and allow users to draw or erase on a virtual canvas using hand gestures.

## Overview

Virtual Paint uses a webcam to track a user's hand in real time. The application detects the index and middle fingers and uses their positions to determine the current interaction mode.

The application provides three modes:

- **Draw** — Raise the index finger while keeping the middle finger down.
- **Erase** — Raise both the index and middle fingers.
- **None** — Lower the index finger to stop drawing or erasing.

The drawing is created on a separate virtual canvas and then combined with the live camera feed.

## Features

- Real-time webcam input
- Hand landmark detection using MediaPipe
- One-hand tracking
- Index finger tracking
- Middle finger gesture detection
- Gesture-based drawing
- Gesture-based erasing
- Virtual 640×480 canvas
- Real-time drawing on the camera feed
- Mirrored camera view
- On-screen Draw/Erase mode indicator
- Keyboard control to exit the application

## Technologies Used

- **Python**
- **OpenCV**
- **NumPy**
- **MediaPipe**

## How It Works

```text
Webcam
   ↓
OpenCV captures video
   ↓
MediaPipe detects the hand
   ↓
Hand landmarks are extracted
   ↓
Finger positions are analyzed
   ↓
Gesture is classified
   ↓
Draw / Erase / None
   ↓
Virtual canvas is updated
   ↓
Canvas is combined with camera feed
   ↓
Result is displayed
```

## Gesture Controls

| Gesture | Action |
|---|---|
| Index finger up | Draw |
| Index + middle fingers up | Erase |
| Fingers down | Stop drawing/erasing |
| `Q` | Exit application |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Virtual-Paint.git
cd Virtual-Paint
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python virtual_paint.py
```

Make sure your computer has a working webcam.

## Requirements

- Python 3.x
- Webcam
- OpenCV
- NumPy
- MediaPipe

## Project Structure

```text
Virtual-Paint/
│
├── virtual_paint.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Current Limitations

This version does not currently include:

- Multiple color selection
- Adjustable brush size
- Save/export functionality
- Undo/redo
- Shape tools
- Text tools
- Multiple-hand support
- Graphical user interface controls

## Future Improvements

Possible future improvements include:

- Multiple brush colors
- Adjustable brush and eraser sizes
- Clear canvas gesture/button
- Undo and redo functionality
- Save artwork as an image
- Additional drawing tools
- Shape recognition
- Multiple-hand interaction
- Improved gesture controls
- A dedicated graphical user interface

## Author

**Laiba**

## License

This project is available for educational and personal use.
