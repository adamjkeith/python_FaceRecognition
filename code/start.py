#call subprocess import
from subprocess import call
#program title
print("------------------------------\nVoting Program Start\n------------------------------")
#asks a question if the user wants to vote. makes it lowercase
q = input("Would you like to vote?: ").lower()
#checks if input is yes
if q == "yes" or q == "y":
    #outputs loading
    print("Loading...")
    #calls the face_get.py file
    call(["python", "face_get.py"])
#runs if the input is anything but yes
else:
    #closes program
    quit()
