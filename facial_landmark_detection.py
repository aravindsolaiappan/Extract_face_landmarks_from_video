from imutils import face_utils
import numpy as np
import argparse
import os
import imutils
import dlib
import cv2
import face_recognition
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

if os.path.isfile(args["shape_predictor"]):
	pass
else:
	cmd = "wget -c --progress=bar http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
	os.system(cmd)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
#image = plt.imread(args["image"]+str("/face"+i+".png"))
# I am generating output for only the first 9 images, expand as per you need
for j in range(1,10):
	imagetemp= args["image"]
	#image = plt.imread(str(imagetemp)+"/face"+str(j)+".jpg")
	#image= face_recognition.load_image_file(str(imagetemp)+"/face"+str(j)+".jpg")
	image= face_recognition.load_image_file(str(imagetemp)+"/output"+str(j)+".png")
	orig = image
	image = imutils.resize(image, width=500)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	rects = detector(gray, 1)

	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		(x, y, w, h) = face_utils.rect_to_bb(rect)
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

		cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

		for (x, y) in shape:
			cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

	plt.subplot(121)
	plt.imshow(orig)
	plt.xticks([])
	plt.yticks([])
	plt.title("Input")

	plt.subplot(122)
	plt.imshow(image)
	plt.xticks([])
	plt.yticks([])
	plt.title("Output")

	fname = "results/"+"result_" + str(j)

	plt.savefig(fname)
	plt.show()

