# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

# Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game
from random import choice
from ColorText import color
print("""
Welcome to RPS game
You can start playing by typing your chance of rock, paper, scissors (or r, p, s)
if you want to exit, just type 'exit'
if you want to play again from zero, just type 'again'
""")
states = ['r', 'p', 's']
c_wins, u_wins = 0, 0
Shaper = {"r": "💎︁",
          "p": "📜︁",
          "s": "✀︁"}

while True:
    inp = input("> ").lower()[0]
    c_choice = choice(states)
    if inp == 'e':
        print('Thank you for playing with us!')
        break
    
    elif inp == 'a': 
        c_wins, u_wins = 0, 0
        print("Restarted!")
        continue

    elif (inp == 'r' and c_choice == 'p'
    ) or (inp == 'p' and c_choice == 's'
    ) or (inp == 's' and c_choice == 'r'): c_wins += 1

    elif (inp == 'r' and c_choice == 's'
    ) or (inp == 'p' and c_choice == 'r'
    ) or (inp == 's' and c_choice == 'p'): u_wins += 1

    else: continue

    print(f' User Wins: {color(50, 250, 50, u_wins)} \n Computer Wins: {color(250, 50, 50, c_wins)} \n You {Shaper[inp]}  vs {Shaper[c_choice]}  Computer')


# TIPs: 
# Lots of conditions
# fStrings are useful
# Importing your own modules
# How to keep your application going
# Hash Table!
