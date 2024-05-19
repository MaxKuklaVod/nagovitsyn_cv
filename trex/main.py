import webbrowser
import pyautogui
import time
import cv2
import numpy as np

webbrowser.open("https://chromedino.com/black/", new=2)

time.sleep(5)

template = pyautogui.locateOnScreen("trex/trex.png", confidence=0.997)
l, t, w, h = int(template[0]), int(template[1]), int(template[2]), int(template[3])
time_time = time.perf_counter()
pyautogui.press("space", presses=1)

while True:
    trex = pyautogui.screenshot("trex/screenshot.png", region=(l, t, w, h))
    image = cv2.imread("trex/screenshot.png")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    _, thresh = cv2.threshold(hsv[:, :, 1], 1, 255, cv2.THRESH_BINARY)

    kernel = np.ones((25, 25), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=1)

    cur_time = time.perf_counter()
    timer = cur_time - time_time
    sleeper = 0.1

    width = w / 6

    if (
        thresh[int(h / 4), int(width + 80)] == 0
        and thresh[int(h / 1.2), int(width + 80)] == 0
    ):
        start = time.time()
        end = time.time()

    else:
        end = time.time()

    if end - start > 0.01:
        sleeper = end - start

    if (
        thresh[int(h / 4), int(width)] == 255
        and thresh[int(h / 1.3), int(width)] == 255
        or thresh[int(h / 1.3), int(width)] == 255
    ) or (
        thresh[int(h / 4), int(width / 1.4)] == 255
        and thresh[int(h / 1.3), int(width / 1.4)] == 255
        or thresh[int(h / 1.3), int(width / 1.4)] == 255
    ):
        pyautogui.press("space")
        time.sleep(sleeper)
        pyautogui.keyDown("down")
        time.sleep(0.01)
        pyautogui.keyUp("down")

    if thresh[int(h / 3), int(width)] == 255 and thresh[int(h / 1.3), int(width)] == 0:
        time.sleep(abs(sleeper * 3))
        pyautogui.keyUp("down")

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
