import cv2
import mediapipe as mp
import pyautogui
import controls


Scroll = controls.Scroll
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Tracking middle of nose to move curstor
        landmark = landmarks[6]            
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 0))
        screen_x = screen_w * landmark.x
        screen_y = screen_h * landmark.y
        pyautogui.moveTo(screen_x, screen_y)

        # Left eye
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        # Right eye
        right = [landmarks[374], landmarks[386]]
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        # Lips
        lips = [landmarks[13],landmarks[14]]
        for landmark in lips:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (255, 255, 255))
        
        if abs(lips[0].y - lips[1].y) > 0.07:
            Scroll.scroll(landmark.y)
        else:
            Scroll.scroll_started = False
            if (left[0].y - left[1].y) < 0.009:
                pyautogui.click()
            elif (right[0].y - right[1].y) < 0.009:
                pyautogui.click(button='right')

    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)