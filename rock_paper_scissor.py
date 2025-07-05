import random

options=('rock','paper','scissor')
running =True

while running:
    player =None
    computer= random.choice(options)

    while player not in options:
        player=input("Enter a choice (rock🧱, paper📃, scisssors✂ ):")

        print(f"player: {player}")
        print(f"computer: {computer}")

        if player== computer:
            print("It's a tie!")
        elif player == 'rock' and computer == 'scissor':
            print("You win")
        elif player == 'paper' and computer == 'rock':
            print("you win")
        elif player == 'scissor' and computer == 'paper':
            print("you win")
        else:
            print("you loose!")
        
        if not input("play again? (y/n): ").lower()=='y':
            running=False
print("Thanks for playing!")