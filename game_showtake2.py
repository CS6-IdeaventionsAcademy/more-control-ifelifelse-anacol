#Alexander
#11/28/2017
#Game show thing
import random
import time
play_again = "Y"
doors = [1,2,3,4]
while play_again == "Y":
    print("Welcome to the spectacular game show that has too long of a name and we don't know why i should really stop making this so long!")
    prize_door = random.randint(1,4)
    chosen_door = int(input("Which door do you enter? (1, 2, 3, or 4) "))
    print("You enter door ", chosen_door, " and...")
    time.sleep(1)
    if chosen_door == prize_door:
        print("You just got a legendary Bernepug! You win!")
    elif chosen_door in doors:
        print("Aw, you just got a duck! Quack quack!")
    else:
        print("Aw, come on, that is NOT a door!")
    
    play_again = input("Would you like to play again? You can enter Y if you do, but otherwise, you will not! ").upper()
