from subprocess import call
import os
import time
with open("name.txt", "r") as f:
    name = f.read()
f.close()

print("\033c", end='')
print("------------------------------\nWelcome to the voting system\n")
print("Voting as:",name,"\n------------------------------")
print("Checking voting status...")
time.sleep(3)
print("You are still able to vote\n")
print("Who would you like to vote for?")
print("\nCandidate A")
print("Candidate B")
while True:
    q = input("\nCadidate: ").lower()
    if q == "a" or q == "b":
        break
    else:
        print("Sorry unrecognised input, please type 'A' or 'B'")

f = open("vote.txt", "w")
f.write(q)
f.close()
call(["python", "face_v.py"])
