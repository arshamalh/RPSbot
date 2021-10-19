Shaper = {"r": "💎︁",
          "p": "📜︁",
          "s": "✂️"}

# Logic
def checker2p(pl1_choice:str, pl2_choice:str, win_rate:dict) -> str:
    pl1 = pl1_choice.lower()[0]
    pl2 = pl2_choice.lower()[0]

    if pl1 == pl2: pass

    elif (pl1 == 'r' and pl2 == 's'
    ) or (pl1 == 'p' and pl2 == 'r'
    ) or (pl1 == 's' and pl2 == 'p'): win_rate['pl1'] += 1

    elif (pl1 == 'r' and pl2 == 'p'
    ) or (pl1 == 'p' and pl2 == 's'
    ) or (pl1 == 's' and pl2 == 'r'): win_rate['pl2'] += 1

    return (f'You: {win_rate["pl1"]}'
            f'\nOpponent: {win_rate["pl2"]} '
            f'\n You {Shaper[pl1]}  vs {Shaper[pl2]}  Opponent')
