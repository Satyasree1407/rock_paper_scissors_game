 import random

choices = ["rock", "paper", "scissors"]

print("🪨 Rock ✋ Paper ✂️ Scissors Game!")
user = input("Enter your choice (rock/paper/scissors): ").lower().strip()
if user not in choices:
    print("Invalid choice. Use rock, paper or scissors.")
    exit()

comp = random.choice(choices)
print("Computer chose:", comp)

if user == comp:
    print("It's a tie!")
elif (user == "rock" and comp == "scissors") or \
     (user == "paper" and comp == "rock") or \
     (user == "scissors" and comp == "paper"):
    print("🎉 You win!")
else:
    print("😢 You lose!")
 Rock ✋ Paper ✂️ Scissors Game!
Enter your choice (rock/paper/scissors): rock
Computer chose: rock
It's a tie!

=== Code Execution Successful ===