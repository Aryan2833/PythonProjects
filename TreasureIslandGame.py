print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice_1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'.").lower()
if choice_1 == 'left':
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait to wait for a boat. Type 'swim' to swim across.").lower()
    if choice2 == 'wait':
       choice3 =  input("You arrive at the island unharmed. There is a house with 3 doors. One red, yellow and one blue. Which colour do you choose?").lower()
    if choice3 == 'red':
            print("It's a room full of fire. Game over.")
    elif choice3 == 'yellow':
            print("You found the treasure. You win!")
    elif choice3 == 'blue':
            print("You entered a room filled with beasts. Game over.")
    else:
        print("You got attacked by sharks. Game over.")
else:
    print("You fell into a hole. Game over")
