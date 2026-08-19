import cv2
import numpy as np
import mediapipe as mp

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# Camera
cap = cv2.VideoCapture(0)

# Canvas
canvas = np.zeros((480, 640, 3), np.uint8)

px, py = 0, 0

print("Press 'q' to exit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img = cv2.resize(img, (640, 480))

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)

            lm = hand_lms.landmark
            h, w, _ = img.shape

            # Index finger
            ix, iy = int(lm[8].x * w), int(lm[8].y * h)

            # Finger states
            index_up = lm[8].y < lm[6].y
            middle_up = lm[12].y < lm[10].y

            # Mode selection
            if index_up and middle_up:
                mode = "erase"
            elif index_up:
                mode = "draw"
            else:
                mode = "none"

            # Drawing logic
            if mode == "draw" or mode == "erase":

                if px == 0 and py == 0:
                    px, py = ix, iy

                if mode == "draw":
                    cv2.line(canvas, (px, py), (ix, iy), (255, 0, 255), 10)
                    cv2.putText(img, "DRAW", (10, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif mode == "erase":
                    cv2.line(canvas, (px, py), (ix, iy), (0, 0, 0), 30)
                    cv2.putText(img, "ERASE", (10, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                px, py = ix, iy

            else:
                # STOP when hand closed or fingers down
                px, py = 0, 0

    else:
        px, py = 0, 0

    # Merge canvas with camera
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas)

    cv2.imshow("Virtual Paint - Laiba", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()