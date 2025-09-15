import random

computer_input = random.choice(["Rock", "Paper", "Scissor"])
points = 0

while True:
    user_input= input("Enter Rock, Paper or Scissor, press Q to Quit:  ").capitalize()
    if user_input == "Q":
        break

    if user_input == computer_input:
        print(f"User picked {user_input.upper()} and computer picked {computer_input.upper()}")
        print(f"Draw, You now have {points} points!")
    elif user_input == "Rock":
        if computer_input == "Scissor":
            points += 1
            print(f"User picked {user_input.upper()} and computer picked {computer_input.upper()}")
            print(f"User wins! You now have {points} points!")
        else :
            points -= 1
            print(f"User picked {user_input.upper()} and computer picked {computer_input.upper()}")
            print(f"Computer wins! You now have {points} points!")
    elif user_input == "Scissor":
        if computer_input == "Paper":
            points += 1
            print(f"User picked {user_input.upper()} and computer picked {computer_input.upper()}")
            print(f"User wins! You now have {points} points!")
        else :
            points -= 1
            print(f"User picked {user_input.upper()} and computer picked {computer_input.upper()}")
            print(f"Computer wins! You now have {points} points!")
    elif user_input == "Paper":
        if computer_input == "Rock":
            points += 1
            print(f"User picked {user_input.upper()} and computer picked {computer_input.upper()}")
            print(f"User wins! You now have {points} points!")
        else:
            points -= 1
            print(f"User picked {user_input.upper()} and computer picked {computer_input.upper()}")
            print(f"Computer wins! You now have {points} points!")
    else:
        print("Invalid input, choose from Rock, Paper, Scissor")

print("Thank you for playing! You have {} points!".format(points))