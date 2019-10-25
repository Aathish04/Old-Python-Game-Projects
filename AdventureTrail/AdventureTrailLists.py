#This is a revised version of Adventure Trail, and includes inventories with the help of Lists.
#This was developed by Aathish Sivasubrahmanian.

#Setting Inventory
inventory = []

#Importing Modules
import time

#Game Begins
print("Welcome to Adventure Trail, the Text Based RPG!")
time.sleep(1)
print("Once Upon a time, long ago, there was once an Adventurer named...")
time.sleep(1)
playername=input("Type in Your Name. \n >") # Player's name is received
time.sleep(1)
print("Once upon a time, long ago, there was once an adventurer named " +playername+ ", who explored the whole world.")
time.sleep(1)
print("The adventurer sailed the Seven Seas, battling everything from dragons, to witches.")
time.sleep(1)
print("But then, suddenly, the inexplicable happened.")
time.sleep(1)
print("After being shipwrecked, the adventurer washed up on a small island, and unlike other times, was completely lost.")
time.sleep(1)
print("That adventurer, is you, my friend. You will either survive, or die, based on the decisions that you make.")
time.sleep(1)
print("You wake up on a craggy rock not far from the ocean.")
time.sleep(1)
print("You see that you can go to two places.")
time.sleep(0.5)
leftright=input("Do you left, where you can see a great forest, or do you go right, where you can see some buffaloes? \n >")
if leftright=="left":
    time.sleep(1)
    print("You have gone left.")
    time.sleep(1)
    print("You slowly hobble through the forest, and suddenly; come across a tree with carvings.")
    time.sleep(1)
    markings=input("Do you attempt to read the gibberish?")
    if markings=="yes":
        time.sleep(1)
        print("You can make out some scratches reading urbytejywkyaoirbke," + playername)
        time.sleep(1)
        print("You wonder how your name got here.")
        time.sleep(1)
        print("You continue walking. A few metres into the forest, you almost trip on a short bronze dagger. ")
        dagger=input("Do you pick up the dagger? \n >")

if leftright=="right":
    time.sleep(1)
    print("You have gone right.")
