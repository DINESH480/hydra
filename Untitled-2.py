import random
choices = ['rock', 'paper', 'scissors']
user = input("Choose rock/paper/scissors: ").lower()
bot = random.choice(choices)
print(f"You: {user} | Bot: {bot}")
if user == bot:
    print("Draw")
elif (user == 'rock' and bot == 'scissors') or \
     (user == 'paper' and bot == 'rock') or \
     (user == 'scissors' and bot == 'paper'):
    print("You win!")
else:
    print("You lose!")
