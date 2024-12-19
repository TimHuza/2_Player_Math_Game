from time import sleep
import random


def math():
    operators = ["+", "-", "*"]
    min_value = 1
    max_value = 12

    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    operator = random.choice(operators)

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    question = f"What is {num1} {operator} {num2} = "
    return question, answer


def load_players():
    player1 = input("Hello, enter your name: ")
    player2 = input("Hello, enter your name: ")

    while True:
        ready1 = input(f"{player1}, press 'y' when you are ready: ")
        ready2 = input(f"{player2}, press 'y' when you are ready: ")

        if ready1.lower() == "y" and ready2.lower() == "y":
            print("Okay. Before you start we print you what the rules are.")
            break
        else:
            print("Not Valid! Both players must press 'y' to continue..")

    return player1, player2

question, answer = math()
player1, player2 = load_players()


print("Rules will show up in 5 seconds!")

sleep(5)

print("\nWelcome to the Math Game!")
print("You will have 10 math questions.")
print("For each correct answer, you get 1 point.")
print("Whoever answers more correctly wins!")
print("When you're ready, press 'y' to start. There will be a 3-second countdown.")
print("Good luck!\n")

player1_ready = input(f"{player1} are you ready? (y/n) ")

if player1_ready.lower() == "y":
    player1_score = 0

    print("The game starts in...")
    for i in range(1, 4):
        print(i)
        sleep(1)
    
    for i in range(1, 11):  # 10 rounds for each player
        question, answer = math()
        while True:  # Input validation loop
            try:
                player1_answer = int(input(f"Question {i}: {question}"))
                break  # Exit loop if valid input
            except ValueError:
                print("Invalid input! Please enter a number.")

        if player1_answer == answer:
            print("Correct! ✅")
            player1_score += 1
        else:
            print(f"Incorrect! ❌")

    print(f"\n{player1}, your total score is {player1_score} out of 10.\n")

player2_ready = input(f"{player2} your turn! Are you ready? (y/n) ")

if player2_ready.lower() == "y":
    player2_score = 0

    print("The game starts in...")
    for i in range(1, 4):
        print(i)
        sleep(1)
    
    for i in range(1, 11):  # 10 rounds for each player
        question, answer = math()
        while True:  # Input validation loop
            try:
                player2_answer = int(input(f"Question {i}: {question}"))
                break  # Exit loop if valid input
            except ValueError:
                print("Invalid input! Please enter a number.")

        if player2_answer == answer:
            print("Correct! ✅")
            player2_score += 1
        else:
            print(f"Incorrect! ❌")

    print(f"\n{player2}, your total score is {player2_score} out of 10.\n")

print("\nThe winning results will be shown in 5-10 seconds.\n")

sleep(6.3)

if player1_score > player2_score:
    print(f"{player1} wins. 🏆")
elif player2_score > player1_score:
    print(f"{player2} wins. 🏆")
else:
    print("That's a tie. 🤝")

print("Thank you for joining us, see you😉.")