import mss
import cv2
import numpy as np
from collections import deque

GAME_REGION = {
    "top": 120,
    "left": 200,
    "width": 1520,
    "height": 720
}

FRAME_STACK = 4

class Vision:
    def __init__(self):
        self.frames = deque(maxlen=FRAME_STACK)
        self.sct = mss.mss()

    def _capture(self):
        img = self.sct.grab(GAME_REGION)
        frame = np.array(img)
        return cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    def _preprocess(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (84, 84), interpolation=cv2.INTER_AREA)
        return resized.astype(np.uint8)

    def reset(self):
        self.frames.clear()
        frame = self._preprocess(self._capture())
        for _ in range(FRAME_STACK):
            self.frames.append(frame)
        return np.stack(self.frames, axis=0)

    def step(self):
        frame = self._preprocess(self._capture())
        self.frames.append(frame)
        return np.stack(self.frames, axis=0)
