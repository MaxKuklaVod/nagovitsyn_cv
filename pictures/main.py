import numpy as np
import cv2
import mss
import matplotlib.pyplot as plt
from pathlib import Path

path = Path(".") / "pictures"

cap = cv2.VideoCapture("pictures/pictures.avi")

pictures = 0
while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        print("Ошибка в кадре, либо конец видео")
        break

    _, thresh = cv2.threshold(frame[:, :, 1], 250, 255, cv2.THRESH_BINARY)
    distance_map = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    ret, dist_tresh = cv2.threshold(
        distance_map, 2 * np.max(distance_map), 255, cv2.THRESH_BINARY
    )

    confuse = cv2.subtract(thresh, dist_tresh.astype("uint8"))
    ret, markers = cv2.connectedComponents(dist_tresh.astype("uint8"))
    markers += 1
    markers[confuse == 255] = 0

    segments = cv2.watershed(frame, markers + 1)
    cnts, hierrachy = cv2.findContours(
        segments, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0
    count_k = 0
    count_c = 0
    for cont in cnts:
        (cur_x, cur_y), r = cv2.minEnclosingCircle(cont)
        area = cv2.contourArea(cont)
        kub = (r * 2) ** 2
        circle = np.pi * r**2

        if area / kub >= 0.5 and area / kub <= 1 and area > 50000:
            count_k += 1

        if area / circle >= 0.9 and area / circle <= 1 and area > 50000:
            count_c += 1

        if area > 37000:
            count += 1

    path = Path(".") / "pictures/result"
    path.mkdir(exist_ok=True)

    if count == 5 and count_k == 2 and count_c == 0:
        pictures += 1
        plt.clf()
        plt.imshow(frame)
        plt.tight_layout()
        plt.savefig(path / f"{pictures}.png")

    # for i in range(len(cnts)):
    #     if hierrachy[0][i][3] == -1:
    #         cv2.drawContours(frame, cnts, i, (0, 255, 0), 10)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break


cap.release()
print(f"The number of my pictures {pictures}")
cv2.destroyAllWindows()
