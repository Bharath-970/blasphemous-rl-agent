import pyautogui
import time

# Safety: move mouse to top-left corner to stop
pyautogui.FAILSAFE = True

print("Starting in 5 seconds...")
time.sleep(5)

# MOVE RIGHT
print("Move Right")
pyautogui.keyDown('d')
time.sleep(2)
pyautogui.keyUp('d')

time.sleep(1)

# JUMP
print("Jump")
pyautogui.press('space')

time.sleep(1)

# MOVE LEFT
print("Move Left")
pyautogui.keyDown('a')
time.sleep(2)
pyautogui.keyUp('a')

print("Done")