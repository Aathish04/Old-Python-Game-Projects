#Code Setting Up Starts
# All Modules are imported
import time
import random
hp=30
count=0
peg="false"

#All functions are defined
def get_input(prompt, accepted): # This function returns an error message if the input doesnt make sense.
    while True:
        value=input(prompt).lower()
        if value in accepted:
            return value
        else:
            print("This is not a recognised answer. It must be one of", accepted)

def handle_room(location): #This function handles where the player will be, the forest, the village, etc.
    global hp 
    global player
    global count
    global speed
    global peg
    global inventory
    # The actual Game Starts Here.
    if location=="start":
        time.sleep(1)
        choice=get_input("Welcome, traveller. Now, what species might you be? \nWe only cater to dwarves,humans or elves. \n >", ["human","elf","dwarf"])

        if choice=="human":
            return "human"
        if choice=="dwarf":
            return "dwarf"
        if choice=="elf":
            return "elf"

    if location=="human":
        print("The human is equipped with a small sheild and sword.")
        equip=get_input("Be a Human?\n >",["yes","no"])
        if equip=='no':
            return "start"
        if equip=="yes":
            player="human"
            return "Dungeon"

#Do not remove, change or in any way edit the code below.
location="start"
while location != "end":
    location=handle_room(location)