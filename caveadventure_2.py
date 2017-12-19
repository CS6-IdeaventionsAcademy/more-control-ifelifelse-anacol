# Alexander Nacol
# Cave Adventure
# 12/5/2017
items = []
play_again = True

# Left Cave Function
def left_cave():
    print("You walk into the left cave. You come across an underground river.")
    print("""You notice that there is a wooden boat in the river, and there is a
sidewalk along the bank of the river. Or you could also swim in the river,
that's cool too.""")
    river_choice = input("Enter B for boat, S for swim, and W for walk. ").upper()
    return river_choice

# Right Cave Function
def right_cave():
    print("You walk into the right cave. The floor starts sloping downward.")
    print("""You notice a hole in the floor ahead af you, and you also see to
your left a long corridor with a torch at the end of it. Do you want to walk
to the torch or climb down the hole?""")
    hole_or_torch = input("Enter H for hole or T for torch. ").upper()
    return hole_or_torch

# Hole Function
def hole():
    print("""You climb down the hole and you enter a hallway. At the end of it
you see a dragon in a big room. You also see that beyond the room is another hallway.
What do you do, fight the dragon or sneak past and walk into the hallway?""")
    dragon_decision = input("Enter D for dragon or H for hallway: ").upper()
    return dragon_decision

# Unacceptable Answer Function
def wrong_answer():
    print("""Well, it seems that you did not enter a choice!
So let's just say you did not make a decision at all. You go nowhere. A dragon eventually
comes and eats you. GAME OVER """)
    


# Title Screen
print("<00>"*20)
print("""
 _____   ___  _   _ _____                              
/  __ \ / _ \| | | |  ___|                             
| /  \// /_\ \ | | | |__                               
| |    |  _  | | | |  __|                              
| \__/\| | | \ \_/ / |___                              
 \____/\_| |_/\___/\____/                              
                                                       
                                                       
  ___ ______ _   _ _____ _   _ _____ _   _______ _____ 
 / _ \|  _  \ | | |  ___| \ | |_  __| | | | ___ \  ___|
/ /_\ \ | | | | | | |__ |  \| | | | | | | | |_/ / |__  
| ___ | | | | | | |  __|| . ` | | | | | | |    /|  __| 
| | | | |/ /\ \_/ / |___| |\  | | | | |_| | |\ \| |___ 
\_| |_/___/  \___/\____/\_| \_/ \_/  \___/\_| \_\____/ 
                                                       
                                                       """)
print("<00>"*20)

# Intro
print("""You are a very poor boy exploring a forest. You were sent by your mama
to collect branches for wood. You find a cliff face with a hole in it. It is a
cave. You see a bright light coming from inside of it. It is a golden, magical
light.

You wonder if this could help you become rich. You are a brave boy, and you
walk towards the cave and into it...

""")
while play_again == True:
    # First choice
    print("You see the cave split into two right when you enter it. Do you walk down the left or the right cave?")
    cave_choice = input("Enter R for right or L for left: ").upper()
    if cave_choice == "L" or cave_choice == "LEFT":
        # Left cave
        river_choice = left_cave()
        if river_choice == "B" or river_choice == "BOAT":
            # Boat choice
            print("""You hop in the boat. But you land on the side, and the
    boat tips over on top of you. Because you cannot surface (as it is on top of you),
    you drown and die.""")
            break
        elif river_choice == "W" or river_choice == "WALK":
            # Walking choice
            print("""You start walking along the river bank. There are a lot of spikes on the ground. You are
    trying to evade them as you step. But you trip over one and fall on some others... You die.""")
            break
        elif river_choice == "S" or river_choice == "SWIM":
            print("You dive in the water and start swimming. The water is unexpectedly warm.")
            if "key" in items:
                print("You already picked up a key, so you find nothing at the end!")
            else:
                print("You swim to the end of the river and find a key. You pick it up.")
                items.append("key")
            print("The path ahead leads back to the opening of the cave.")
        else:
            # Unacceptable answer
            wrong_answer()
            break
    elif cave_choice == "R" or cave_choice == "RIGHT":
        # Right cave
        hole_or_torch = right_cave()
        if hole_or_torch == "T" or hole_or_torch == "TORCH":
            print(""""You walk down the long corridor to the torch. When you finally reach the torch,
    you find out that it is a lot bigger than it seems. The stick attatched to the wall is a giant log,
    and it is high above your head. The flame is very hot and very large. It also seems to be magical.
    It reaches down and touches you. You were burnt by the torch's enchanted flame!""")
            break
        elif hole_or_torch == "H" or hole_or_torch == "HOLE":
            dragon_decision = hole()
            if dragon_decision == "D" or dragon_decision == "DRAGON":
                print("You punch the dragon. Your hand bounces back and hits you in the face.")
                print("You have been knocked out.")
                print("The dragon looks down and eats you. GAME OVER")
                break
            elif dragon_decision == "H" or dragon_decision == "HALLWAY":
                print("""You sneak past the dragon. It does not notice you. You walk into the dark hallway. At the end of it, you
    discover a treasure chest. It is locked.""")
                if "key" in items:
                    print("You use your key to open the chest! In it, you find a bunch of coins! You win!")
                    break
                else:
                    print("You can't open the chest because you need a key. You move forward. The path ahead snakes back to the opening of the cave.")
            else:
                wrong_answer()
                break
        else:
            wrong_answer()
            break
    else:
        # Unacceptable answer
        wrong_answer()
        break
print("Thank you for playing!")
    


