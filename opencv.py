import cv2
import numpy as np
from PIL import ImageGrab
from pynput.keyboard import Controller
import time
key = Controller()
xx=0
y=0
while True:
	img = ImageGrab.grab()
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
	width ,height = 500 , 500
	imgResize = cv2.resize(frame,(width,height))
	imgCropped = imgResize[130:155,180:207+y]
	imCropResize  = cv2.resize(imgCropped,(imgResize.shape[1],imgResize.shape[0]))

	a = cv2.cvtColor(imCropResize, cv2.COLOR_RGB2BGR)
	print(a)
	xx+=1
	if xx%300==0:
		y+=1
	for x in a:
		if np.array([83]) in x:
			print("Jump")
			key.press(" ")
			time.sleep(0.3)
			key.release(" ")
			break
	if cv2.waitKey(1) == 27:
		break