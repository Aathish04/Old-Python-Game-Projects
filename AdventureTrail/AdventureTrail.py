#This game was developed in joint by Rhys Van Der Kruk and Aathish Sivasubrahmanian
#Shoutout to Matthew Riedel, a classmate of mine.
#All My Imports
import time
print("Welcome to Adventure Trail. The Word Game where what you do affects your rate of survival.")
time.sleep(0.5)
playername =(input("Now, What is the name of our brave adventurer? \n > "))#Receives Playername
print("Welcome, " + playername)
time.sleep(0.5)
pathchoose=input("Do you choose the left path, where you can see a forest, or do you go to the right path, where you can see a few buffaloes grazing ? \n >") #The Initial Pathway split, Choosing one or the other pits the player against different obstacles.
if pathchoose=='left':
    print("You have chosen the left path")
    time.sleep(0.5)
    print("You walk down the path towards the dark forest.")
    forest=input("A wizard appears before the entrance. He says: Go through the forest or go around, "+playername+", it's your choice. \n > ") #The Second Decision.
    if forest=='go through':
        print("You enter the forest.")
        time.sleep(0.5)
        sketchings=input("You see sketchings on a tree. Do you attempt to read them? \n > ")
        if sketchings=='yes':
            print("They can barely be seen but they say urbytejywkyaoirbke, "+ playername)
            time.sleep(0.5)
            print("You wonder how your name is here.")
        if sketchings=='no':
            print("The marks don't seem important. You keep walking on.")
            time.sleep(0.5)
        dagger=input("As you continue through the forest you almost trip on a dagger. Do you take it? \n >") # The Player chooses whether to take a weapon or not.
        if dagger=='yes':
            print("You pick up the dagger. You feel its sharp edge")
            time.sleep(0.5)
        if dagger=='no':
            print("Dejectedly, you kick it away, It never was your favourite weapon anyway.")
            time.sleep(0.5)
        
        print("You walk into a nearly invisible giant spider web. It's resident, the spider, crawls slowly towards you.")
        if dagger=='yes':
            print("You take hold of your dagger, glad you picked up.You cut through the web and run away as fast as you can with the spider at your heels.")
            time.sleep(0.5)
            print("It chases you to the front of a cave, dimly lit with torches.")
            time.sleep(0.5)
            cave=input("Do you enter the cave? \n >")
            if cave=="yes":
                time.sleep(0.5)
                print("You slowly creep into the cave. You take a torch from the nearby stand, and keep walking.")
                time.sleep(0.5)
            if cave=="no":
                time.sleep(0.5)
                print("You decide not to go into the eery cave, which even the spider doesn't want to go near.")
                time.sleep(0.5)
                print("You notice that there are two paths; each leading different ways")
                crossroad1=input("Do you go left, or do you go right?")
                if crossroad1=="left" or "go left":
                    time.sleep(0.5)
                    print("You have gone left")
                if crossroad1=="right" or "go right":
                    time.sleep(0.5)
                    print("You have gone right.")
        if dagger=='no':
            time.sleep(0.5)
            print("Now you wish you had the dagger with you. You sense your death coming near")
            answer=input(" The Spider says: 'I see you have no weapon to defend yourself. As a gift of mercy, I will ask you a riddle: The riddle is: \n Stronger than steel, yet lighter than cotton \n Found in a corner, forever forgotten, \n I bother so many, but marvel a few \n You can't seem to make me, I'm a mystery to you. \n Now answer or I shall feast. You only get a single chance'  \n >")
            if answer==('Spider Silk'):
                time.sleep(0.5)
                print("It seems you have got it correct. Perhaps you are not biological waste after all.(the spider cuts you free)")
                cave=input("You then run far away, to a cave, dimly lit with almost stuttering torches. Do you go in? \n>")
                if cave=="yes" or "Yes":
                    print("You slowly step into the cave, taking a lacquer torch from the sides.")
                if cave=="no":
                    print("You take a step back, not wanting to go into the eery cave.")
                    crossroad2=input("You see that you have arrived at a crossroads. \n Go left or go right? \n >")
                    if crossroad2=="left":
                        print("You have gone left.")
                    
                    if crossroad2=="right":
                        print("You have gone right.")
            else:
                time.sleep(0.5)
                print("That is incorrect! Now I shall feast. The spider injects you with venom, paralyizing you. Dark spots appear in your eyes. the blood draining out of you and your body liquefyng. Your last thought is...At least I made a pretty good meal for a spider. You are now dead," +playername)
    
    if forest=="go around":
        time.sleep(0.5)
        print("You decide to go around the forest")
        time.sleep(0.5)
        print("You walk around with the trees to your left")
        sword=input("You see a slightly rusted bronze sword. Do you pick it up?  \n >")
        if sword=="yes":
            time.sleep(0.5)
            print("You pick up the sword and strap it to your back. You feel defended now.")
            time.sleep(0.5)
            print("You continue around the Forest.")
            time.sleep(0.5)
            ogres=input("You see some ogres. Do you attack or run? \n >")
            if ogres=="attack":
                print("You manage to successfully stab the nearest one to you without getting eaten, you spin and lop the leg off the second one. The third one, a child, is quivering and shaking in fear.")
                time.sleep(0.5)
                child=input("Do you kill the child as well? \n > ")
                if child=="yes":
                    time.sleep(0.5)
                    print("You look the child in the eye, and stab it in the heart, you cruel monster!")
                    time.sleep(0.5)
                    bracelet=input("You find that the ogre child has an emerald bracelet. Take Bracelet? \n > ")
                    if bracelet=="yes":
                        time.sleep(0.5)
                        print("Despicable! Stealing from a murdered child!")
                    if bracelet=="no":
                        time.sleep(0.5)
                        print("You feel disgusted at stealing from a dead body.")
                        sheath=input("Sheath Sword? \n > ")
                    if sheath=="yes":
                        time.sleep(0.5)
                        print("You leave the child's body.")
                    if sheath=="no":
                        time.sleep(0.5)
                        print("You keep your sword in your hand, ready to defend yourself if necessary. \n You slip on a pool of blood, and impale yourself on your own sword, because you didn't sheath it.")
                if child=="no":
                    time.sleep(0.5)
                    print("You turn your back on the child, sword still in hand.")
                    time.sleep(0.5)
                    sheath=input("Sheath Sword? \n > ")
                    if sheath=="yes":
                        time.sleep(0.5)
                        print("You leave the child crying near the bodies of her murdered parents.")
                        # Add more scenarios here
                    if sheath=="no":
                        time.sleep(0.5)
                        print("You Turn around, sword in hand, you hear a sharp whistling sound an a thwack, as the child fires a dart into your back. \n You see funny colours and black out. You are now dead. ")
            if ogres=="run":
                print("You quickly run away from the ogre campsite")
                time.sleep(0.5)
                print("As you keep walking, you find a boat, moored to the river.")
                time.sleep(0.5)
                river=input("Do you cross the river or sail? \n >")
                if river=="cross":
                    time.sleep(0.5)
                    print("You use the boat to cross the river, and continue on your journey.")
                if river=="sail":
                    time.sleep(0.5)
                    print("You use the boat to sail down the river.")
                    print("You sail for days on end, and all at once, you see a port!")
                    port==input("Do you dock the boat here? \n >")
                    if port=="yes"or"yes":
                        print("You throw a rope onto the port and pull yourself to the banks of the river.")
                        #add more scenarios here
                    if port=="no" or "No":
                        print("You lie back down, thinking that the port isnt worth the trouble, a few days later you have expended all your food. \n You slip into a coma, and your boat falls off a waterfall")
                        print("Congrajulations, " +playername+ ", You are now dead")
        if sword=="no":
            time.sleep(0.5)
            print("You decide to leave the sword alone. You feel like you have made a bad choice.")
            time.sleep(0.5)
            print("You continue around the Forest.")
            time.sleep(0.5)
            ogres=input("You see some ogres. Do you attack or run? \n >")
            if ogres=="run":
                time.sleep(0.5)
                print("You try to run but the ogres spot you and shoot you with a poison dart. You see funny colours and black out. \n You are now dead" +playername+ "because you tried to run from bloody ogres!")
            if ogres=="attack":
                print("You hit one of the ogres in the face with your fist. The ogre is agitated and flicks you into space.You land on the moon, dazed. You think 'I'm on the moon so that means...Can't....Breath.' \n Great job, you died because you thought you could take down an entire ogre without a weapon, "+playername)
if pathchoose=='right':
    print("You have chosen the right path")
    print("You walk towards the open plains")
    time.sleep(0.5)
    buffalo=input("You see a herd of wild buffalo. Do you yell or attack? \n > ")
    if buffalo == 'attack' :
        print("You decide to attack the buffaloes. The buffaloes charge and trample you. You are now dead, "+playername)
    if buffalo=="yell":
        time.sleep(0.5)
        print("You yell at the buffalo. They start walking away with caution.")
        book=input("As you walk along the plains, a book appears from the earth and wills you to take it. \n Do you accept the book? \n > ")
        if book=='yes':
            time.sleep(0.5)
            print("Unable to snap out of the trance you touch the book. It opens and shoots a beam of brown light towards your chest.The longer it beams the heavier you seem and the stronger you feel. The last item you see is a emblem made of earth in the shape of a small mountain. It implants itself into your chest. The book clossess and desinagrates into peices of earth never to be seen again")
            time.sleep(0.5)
            print("You get up dazed from what just happened. You move you hands and it causes the earth around to move.You get some ideas to help you. You think you can either tunnel undergroud or launch yourself forward.")
            idea=input("Tunnel or launch? \n > ")
            if idea=="launch":
                time.sleep(0.5)
                print("You launch yourself into sky and land safely on the far side of the plains next to a desert")
            if idea=="tunnel":
                time.sleep(0.5)
                print("You move the earth around you and make a hole that you fall into. Since you can't control your powers (dumbass),am the hole seals up and crushes you. You are now dead"+playername) 
        if book=='no':
            time.sleep(0.5)
            print('You snap out of the trance. The book is too scary to be trusted')
            time.sleep(0.5)
            print('You keep walking through the plains and you see a friendly squirrel.')
            time.sleep(0.5)
            squirrel=input('Pet or keep walking? \n > ')
            if squirrel=="pet" or "pets":
                time.sleep(0.5)
                print("The Squirrel savours the moment, looking at you adoringly. It scurries away, returning a moment later with an Acorn and a Small Brass Key.")
            takestuff=input("Take Key and acorn? \n >")
            if takestuff=="yes":
                print("You place your open palm near the squirrel. It quickly places the things into your hand and scurries off. ")
                print("You come across an old basin of dirt that seems soft enough to dig")
                plant=input("Do you plant the Acorn? \n >")
                if plant=="yes"or"Yes"or"Y":
                    time.sleep(0.5)
                    print("You kneel down and plant the acorn, feeling good about yourself.")
                    time.sleep(0.5)
                    print("As you step back, you feel the ground below you rumbling.")
                    print("You turn around, and notice that the acorn has already sprouted into a small plant, with two branches; the rumbling seems to be coming from the plant")
                    time.sleep(0.5)
                    print("You take a step towards the plant. Suddenly, the plant grows legs, and steps out of the basin.")
                    time.sleep(0.5)
                    print("The plant walks up to you, looks up at you and says 'I am Froot!' \n climbing onto your shoulder, all the while repeating the words 'I am Froot!' ")
                    # More stuff to be added here soon
                time.sleep(0.5)
            if takestuff=="no":
                print("You keep walking.")
                time.sleep(0.5)
                