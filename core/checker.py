from random import choice

# Core settings
states = ['r', 'p', 's']
Shaper = {"r": "💎︁",
          "p": "📜︁",
          "s": "✂️"}

# Logic
def checker(text:str, win_rate:dict) -> str:
    inp = text.lower()[0]
    c_choice = choice(states)
        
    if inp == c_choice: pass

    elif (inp == 'r' and c_choice == 'p'
    ) or (inp == 'p' and c_choice == 's'
    ) or (inp == 's' and c_choice == 'r'): win_rate['c_wins'] += 1

    elif (inp == 'r' and c_choice == 's'
    ) or (inp == 'p' and c_choice == 'r'
    ) or (inp == 's' and c_choice == 'p'): win_rate['u_wins'] += 1

    return (f'User Wins: {win_rate["u_wins"]}'
            f'\nComputer Wins: {win_rate["c_wins"]} '
            f'\n You {Shaper[inp]}  vs {Shaper[c_choice]}  Computer')