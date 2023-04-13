from subprocess import call
import cv2
import os
import time
os.system('cls')
print("------------------------------\nFace Registration Program\n------------------------------")
print("Press SPACE to capture face")
print("starting camera...")

cam = cv2.VideoCapture(0)
cv2.namedWindow("Press Space")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Press Space", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        cam.release()
        cv2.destroyAllWindows()
        print("CHECK USER'S ID")
        img_name = input("What is the user's name?: ")
        path = ("faces\\"+img_name+".jpg")
        cv2.imwrite(path, frame)
        print("Face Registered")
        print("\nRestarting Program...\n")
        time.sleep(3)
        os.system('cls')
        call(["python", "start.py"])
        break
