from telegram.ext import (Updater, Filters, 
                          CommandHandler, 
                          MessageHandler, 
                          CallbackQueryHandler)

from Keyboards import PlayingKeyboard
from random import choice
from time import sleep

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

# Logic
def checker(uid, text):
    inp = text.lower()[0]
    c_choice = choice(states)
    if inp == 'a':
        win_rates[uid] = {'c_wins':0, 'u_wins': 0}
        return 'Restarted!'

    elif (inp == 'r' and c_choice == 'p'
    ) or (inp == 'p' and c_choice == 's'
    ) or (inp == 's' and c_choice == 'r'): win_rates[uid]['c_wins'] += 1

    elif (inp == 'r' and c_choice == 's'
    ) or (inp == 'p' and c_choice == 'r'
    ) or (inp == 's' and c_choice == 'p'): win_rates[uid]['u_wins'] += 1

    elif inp == c_choice: pass
    
    else: return "Wrong input! Please try again."

    return (f'User Wins: {win_rates[uid]["u_wins"]}'
            f'\nComputer Wins: {win_rates[uid]["c_wins"]} '
            f'\n You {Shaper[inp]}  vs {Shaper[c_choice]}  Computer')

# Commands
def start(update, ctx):
    win_rates[update.effective_chat.id] = {'c_wins':0, 'u_wins': 0}
    ctx.bot.send_message(chat_id=update.effective_chat.id, 
    text=("Welcome to RPS game"
        "\nYou can start playing by Choosing your chance of Rock, Paper, Scissor"
    ), reply_markup=PlayingKeyboard)

# Handlers
def inputHandler(update, ctx):
    chatID = update.effective_chat.id
    msg = update.message
    last_msg = ctx.user_data['last_message_id']
    text = checker(chatID, msg.text)
    if last_msg:
        ctx.bot.edit_message_text(chat_id=chatID, 
                                  message_id=last_msg, 
                                  text=text, reply_markup=PlayingKeyboard)
    else:
        ctx.bot.send_message(chat_id=chatID, text=text, reply_markup=PlayingKeyboard)
        last_msg = msg.message_id
    
    sleep(3)
    ctx.bot.delete_message(chat_id=chatID, message_id=msg.message_id)

def ButtonHandler(update, ctx):
    query = update.callback_query
    query.answer()
    text = checker(update.effective_chat.id, query.data)
    ctx.user_data['last_message_id'] = query.message.message_id
    query.edit_message_text(text=text, reply_markup=PlayingKeyboard)


# Add handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(ButtonHandler))
dispatcher.add_handler(MessageHandler(Filters.text, inputHandler))

# Start & Stop
Bot.start_polling()
Bot.idle() # to stop the bot with ctrl + c or custom signals
