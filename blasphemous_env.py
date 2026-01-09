import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2
import mss
import time
from collections import deque
from action_controller import do_action

# ==============================
# CONFIG
# ==============================
GAME_REGION = {
    "top": 120,
    "left": 200,
    "width": 1520,
    "height": 720
}

FRAME_STACK = 4
MAX_STEPS = 300

# ==============================
# ENVIRONMENT
# ==============================
class BlasphemousEnv(gym.Env):
    metadata = {"render_modes": []}

    def __init__(self):
        super().__init__()

        # Actions: LEFT, RIGHT, JUMP, ATTACK, DODGE, STAY
        self.action_space = spaces.Discrete(6)

        # Observation: 4 stacked grayscale frames
        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(4, 84, 84),
            dtype=np.uint8
        )

        self.frames = deque(maxlen=FRAME_STACK)
        self.steps = 0
        self.prev_frame = None

        self.sct = mss.mss()

    # --------------------------
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.frames.clear()
        self.steps = 0
        self.prev_frame = None

        # Warm-up frames
        for _ in range(FRAME_STACK):
            frame = self._get_frame()
            self.frames.append(frame)

        obs = np.stack(self.frames, axis=0)
        return obs, {}

    # --------------------------
    def step(self, action):
        self.steps += 1

        # Execute action (SAFE)
        do_action(action)

        # Small delay so game reacts
        time.sleep(0.05)

        frame = self._get_frame()
        self.frames.append(frame)

        obs = np.stack(self.frames, axis=0)

        # ------------------
        # SIMPLE REWARD
        # ------------------
        reward = 0.0

        if self.prev_frame is not None:
            diff = np.mean(np.abs(frame - self.prev_frame))
            reward = diff * 0.01   # movement = reward

        self.prev_frame = frame

        terminated = False
        truncated = self.steps >= MAX_STEPS

        return obs, reward, terminated, truncated, {}

    # --------------------------
    def _get_frame(self):
        screenshot = self.sct.grab(GAME_REGION)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (84, 84), interpolation=cv2.INTER_AREA)
        return resized.astype(np.uint8)
