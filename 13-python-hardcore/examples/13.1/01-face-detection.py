# pip install opencv-python matplotlib requests Pillow numpy

import cv2, requests
import numpy as np
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

url = "https://i3.ytimg.com/vi/__VUu6gN_dM/maxresdefault.jpg"
img = np.array(Image.open(BytesIO(requests.get(url).content)).convert("RGB"))

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

img_draw = img.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(img_draw, (x, y), (x+w, y+h), (0, 255, 0), 3)

plt.imshow(img_draw)
plt.axis("off")
plt.show()
