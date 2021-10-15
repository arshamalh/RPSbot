from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice

# Bot settings
BotToken = "1987640815:AAEdOu-w47RcYRCFoTQognLmg6QKZDvkgPA"
updater = Updater(token=BotToken, use_context=True)
dispatcher = updater.dispatcher

# Core settings
states = ['r', 'p', 's']
Shaper = {"r": "💎︁",
        "p": "📜︁",
        "s": "✀︁"}
win_rates = {}

def start(update, context):
    win_rates[update.effective_chat.id] = {"c_wins": 0, "u_wins": 0}
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text=("Welcome to RPS game"
            "\nYou can start playing by typing your chance of rock, paper, scissors (or r, p, s)"
            "\nif you want to exit, just type 'exit'"
            "\nif you want to play again from zero, just type 'again'"))

def inputer(update, context):
    text = checker(update.effective_chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def checker(uid, text):
    inp = text.lower()[0]
    c_choice = choice(states)
    if inp == 'e':
        win_rates[uid] = {"c_wins": 0, "u_wins": 0}
        return 'Thank you for playing with us!\nYou can /start again anytime you want!'
    
    elif inp == 'a': 
        win_rates[uid] = {"c_wins": 0, "u_wins": 0}
        return "Restarted!"

    elif (inp == 'r' and c_choice == 'p'
    ) or (inp == 'p' and c_choice == 's'
    ) or (inp == 's' and c_choice == 'r'): win_rates[uid]["c_wins"] += 1

    elif (inp == 'r' and c_choice == 's'
    ) or (inp == 'p' and c_choice == 'r'
    ) or (inp == 's' and c_choice == 'p'): win_rates[uid]["u_wins"] += 1

    else: pass

    return f' User Wins: {win_rates[uid]["u_wins"]} \n Computer Wins: {win_rates[uid]["c_wins"]} \n You {Shaper[inp]}  vs {Shaper[c_choice]}  Computer'

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, inputer))

updater.start_polling()



