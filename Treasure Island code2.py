
print("Welcome to Treasure Island. Your mission is to find the treasure")
Choice1 = input('You\'are at Cross road, where you want to go? type "Left" or "Right"?.\n').lower()

if Choice1 == "left":
    Choice2 = input('You\' come to a lake. There is an island in the middle of the lake. Do you want to "wait" for a boat or "swim" across?.\n').lower()

    if Choice2 == "wait":
        Choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n').lower()
        
        if Choice3 == "yellow":
            print("You win!")
        elif Choice3 == "red":
            print("its room full of fire. game over")
        elif Choice3 == "blue":
            print("its room full of beast. game over")
        else:
            print("you choose the door that doesnt exists. Game over.")
    else:
        print("you have been attacked by crocodile. Game over.")
else:
    print("Game over.")