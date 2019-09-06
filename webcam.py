import cv2

camera = cv2.VideoCapture(1)

face_detector = cv2.CascadeClassifier('Data_Face/templatedata.xml')
while True:
	# Read the Image
	ret,img = camera.read()
	
	# Detect the Faces
	faces = face_detector.detectMultiScale(img,1.1,5)
	
	# Draw the Rect
	for f in faces:
		x,y,w,h = f
		color = (0,255,0)
		cv2.rectangle(img,(x,y),(x+w,y+h),color,5)
	
	# 4. Show the image
	cv2.imshow("Web Cam Video",img)
	cv2.waitKey(1) # Add a delay of 1 ms