from subprocess import call
import cv2
import os
import time
with open("name.txt", "r") as f:
    name = f.read()
f.close()

with open("vote.txt", "r") as f:
    vote = f.read()
f.close()

print("Processing...")
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cam.release()
    cv2.destroyAllWindows()
    img_name = name
    path = ("voted\\"+img_name+".jpg")
    cv2.imwrite(path, frame)
    break
with open("vote.txt", "r") as f:
    vote = f.read()
f.close()
print("\nYou have successfully voted for Cadidate",vote.upper())
print("\nrestarting program...")
time.sleep(3)
os.system('cls')
call(["python", "start.py"])
