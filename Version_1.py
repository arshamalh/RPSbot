from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher
from random import choice

# Bot settings
BotToken = "1987640815:AAEdOu-w47RcYRCFoTQognLmg6QKZDvkgPA"
Bot = Updater(token=BotToken, use_context=True)
dispatcher = Bot.dispatcher

# Core settings
states = ['r', 'p', 's']
Shaper = {"r": "💎︁",
          "p": "📜︁",
          "s": "✀︁"}

win_rates = {}

# Commands definition
def start(update, ctx):
    win_rates[update.effective_chat.id] = {'c_wins':0, 'u_wins': 0}
    ctx.bot.send_message(chat_id=update.effective_chat.id, 
    text=("Welcome to RPS game"
        "\nYou can start playing by typing your chance of rock, paper, scissors (or r, p, s)"
        "\nif you want to exit, just type 'exit'"
        "\nif you want to play again from zero, just type 'again'"
    ))

def inputHandler(update, ctx):
    text = checker(update.effective_chat.id, update.message.text)
    ctx.bot.send_message(chat_id=update.effective_chat.id, text=text)

def checker(uid, text):
    inp = text.lower()[0]
    c_choice = choice(states)
    if inp == 'e':
        win_rates[uid] = {'c_wins':0, 'u_wins': 0}
        return 'Thank you for playing with us!'
    
    elif inp == 'a': 
        win_rates[uid] = {'c_wins':0, 'u_wins': 0}
        return "Restarted!"

    elif (inp == 'r' and c_choice == 'p'
    ) or (inp == 'p' and c_choice == 's'
    ) or (inp == 's' and c_choice == 'r'): win_rates[uid]['c_wins'] += 1

    elif (inp == 'r' and c_choice == 's'
    ) or (inp == 'p' and c_choice == 'r'
    ) or (inp == 's' and c_choice == 'p'): win_rates[uid]['u_wins'] += 1

    elif inp == c_choice: pass
    
    else: return "Wrong input! Please try again."

    return f'User Wins: {win_rates[uid]["u_wins"]} \nComputer Wins: {win_rates[uid]["c_wins"]} \n You {Shaper[inp]}  vs {Shaper[c_choice]}  Computer'

# Add handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, inputHandler))

# Start polling!
Bot.start_polling()