#call subprocess import
from subprocess import call
#imports cv2
import cv2
#sets variable cam to the video capture function of cv2. 0 is default cam
cam = cv2.VideoCapture(0)
#runs until broken
while True:
    #set variables ret and frame to the image taken by the camera
    ret, frame = cam.read()
    #runs if ret is empty
    if not ret:
        #outputs failed to grab frame
        print("failed to grab frame")
        #breaks loop
        break
    #sets a variable img_name to current.jpg
    img_name = "current.jpg"
    #uses the imwrite function of cv2 to save the image with the img_name
    cv2.imwrite(img_name, frame)
    #breaks loop
    break
#releases the camera
cam.release()
#destroys a window if it opens
cv2.destroyAllWindows()
#calls the face_rec file
call(["python", "face_rec.py"])

