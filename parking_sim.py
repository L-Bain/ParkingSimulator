import random

print("WELCOME TO UQ PARKING SIMULATOR")
print("You wake up on a Monday morning and roll over to check the time on your clock.")
print("7:45 a.m.")
print("Uh oh, looks like you have 15 minutes to make it to class on time.")
print("What do you do now?")

left_bed = False
brushed_teeth = False
dressed = False
in_car = False
at_uni = False
at_bay = False
scanned_in = False
parked = False
on_Hyperloop = False

while True:
    move = input("> ")
    move = move.lower()

    if "bed" in move and ("leave" in move or "get out" in move): 
        left_bed = True
        print("You get out of bed...")
    elif "brush teeth" in move:
        if not left_bed:
            print("You should probably get out of bed first...")
        else:
            brushed_teeth = True
            print("You brush your teeth. Good dental hygiene but YOU'RE RUNNING LATE!")
    elif "dressed" in move or "clothes" in move:
        if not left_bed:
            print("You should probably get out of bed first...")
        else:
            dressed = True
            print("You put on something casual but fashionable. NOW GET TO YOUR CAR!")
    elif "car" in move and ("get in" in move or "enter" in move):
        if not left_bed:
            print("You should probably get out of bed first...")
        else:
            if not dressed:
                print("Put on some clothes first you animal!")
            else:
                in_car = True
                print("You get in your car...")
    elif "drive" in move and ("uni" in move or "university" in move):
        if not left_bed:
            print("You should probably get out of bed first...")
        else:
            if not in_car:
                print("You should probably get in your car first...")
            else:
                print("You drive to university...")
                print("Time is 7:55 a.m.")
                print("Better find a park soon...")
                at_uni = True
    elif "park" in move and at_uni:
        if not left_bed:
            print("You should probably get out of bed first...")
        else:
            if not in_car:
                print("You should probably get in your car first...")
            else:
                print("If it is an on-campus park you seek, your dice roll must not be weak...")
                print("Do you wish to roll the dice [Y/N]")
                dice_roll = input("> ")
                dice_roll = dice_roll.lower()
                if dice_roll == "y":
                    roll = random.randint(1, 6)
                    print("You roll a {}".format(roll))
                    if roll == 6:
                        print("Congrats you found a park")
                        break
                    else:
                        print("You fail to find a park and are now late to class.")
                        print("Next time try the off-campus parking bay.")
                        break
                else:
                    print("You park your car in the middle of the street...")
                    print("Controversial, but brave. Respect.")
                    print("You make it to class but cause a 10 car pile up...")
                    print("It probably would have been better if you drove to the off-campus parking bay instead.")
    elif "drive" in move and "parking bay" in move:
        if not left_bed:
            print("You should probably get out of bed first...")
        else:
            if not dressed:
                print("Put on some clothes first you animal!")
            else:
                print("You drive to the UQ off-campus parking bay...")
                print("Time is 7:50 a.m.")
                print("You pull up to the boom gate, there is a ID scanner to your right...")
                at_bay = True
    elif "scan" in move:
        if not at_bay:
            print("Scan what?")
        else:
            print("You scan your student ID and the boom gate opens...")
            print("You should probably find a park...")
            scanned_in = True
    elif "park" in move and scanned_in:
        print("You easily park in one of the many available spots...")
        print("You look over and see the Hyperloop station...")
        parked = True
    elif "car" in move and ("out" in move or "exit" in move or "leave" in move) and scanned_in:
        print("You get out of your car...")
        in_car = False
    elif "hyperloop" in move and ("board" in move or "get on" in move) and parked and in_car:
        print("You need to get out of your car first!")
    elif "hyperloop" in move and ("board" in move or "get on" in move) and parked and not in_car:
        print("You board the Hyperloop and reach the UQ campus with 3 minutes to spare...")
        print("Congrats, you made it to class on time!")
        break
    else:
        print("You can't do that!")
