#imports the face_recognition module as fr
import face_recognition as fr
#imports the os
import os
#imports the cv2 module
import cv2
#imports the face_recognition module
import face_recognition
#imports the numpy module as np
import numpy as np
#imports the sleep function from the time module
from time import sleep
#imports the call function from the subprocess module
from subprocess import call
import time

#creates a function called get_encoded_faces
def get_encoded_faces():
    #creates an array called encoded
    encoded = {}
    #gets each part of the file names in the folder faces
    for dirpath, dnames, fnames in os.walk("./voted"):
        #for each files with a name, run code
        for f in fnames:
            #checks if the file ends with .jpg or .png
            if f.endswith(".jpg") or f.endswith(".png"):
                #creates a variable caled face and sets it to the image file and naem
                face = fr.load_image_file("faces/" + f)
                #puts the filename into a temporary variable
                encoding = fr.face_encodings(face)[0]
                #removes the .jpg or .png from the filename
                encoded[f.split(".")[0]] = encoding
    #returns the encoded image
    return encoded

#crates a function called unknown_image_encoded and recieves the image
def unknown_image_encoded(img):
    #sets the face variable to the loaded image file
    face = fr.load_image_file("faces/" + img)
    #sets a variable called encoding to the unknown face
    encoding = fr.face_encodings(face)[0]
    #returns the encoded image
    return encoding

#creates a function called classify_face and recieves the image as im
def classify_face(im):
    #gets the encoded face
    faces = get_encoded_faces()
    #gets the encoded value of the files
    faces_encoded = list(faces.values())
    #gets the names of the files
    known_face_names = list(faces.keys())

    #reads the image of current.jpg
    img = cv2.imread(im, 1)
    #resizes the image to make it smaller
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    img = img[:,:,::-1]

    #gets the face locations from the face_recognition module (eye spacing etc)
    face_locations = face_recognition.face_locations(img)
    #gets the face locations from the face_recognition module (eye spacing etc)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    #writing each line is boring especically if its just for you to see, basically next it just checks if there is a similar face in the faces file, then there is
    #some if statements to ask if the user wants to add a new face. I haven't created the actual voting system yet it just says if the ID is verified and then quits.
    name = "Unknown"
    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)

        


    # Display the resulting image
    if name == "Unknown":
            call(["python", "end.py"])
    else:
        print("\033c", end='')
        print("------------------------------\nWelcome to the voting system\n")
        print("Voting as:",name,"\n------------------------------")
        print("Checking voting status...")
        time.sleep(3)
        print("\nSorry you can only vote once.\n")
        print("restarting program...")
        time.sleep(3)
        os.system('cls')
        call(["python", "start.py"]) 



a = (classify_face("current.jpg"))
