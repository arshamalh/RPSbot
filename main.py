from dotenv import load_dotenv, dotenv_values as denv
from telegram.ext import (Updater, Filters, 
                          CommandHandler, 
                          MessageHandler, 
                          CallbackQueryHandler)

from utiles.Keyboards import CancelKeyboard, PlayingKeyboard, MainKeyboard
from utiles.Titles import titles as t
from handlers import TextChoiceHandler, ButtonHandler
from core import matched_opponents, opponents

load_dotenv()

# Commands
def start(update, ctx):
    ctx.user_data['win_rate'] = {'c_wins':0, 'u_wins': 0, 'pl1':0, 'pl2': 0}
    ctx.user_data['last_msg_txt'] = "/start"
    ctx.user_data['last_msg_id'] = update.message.message_id
    ctx.user_data['started'] = True
    ctx.user_data['matched'] = False
    ctx.bot.send_message(chat_id=update.effective_chat.id, 
    text=("Welcome to RPS game"
        "\nClick on play and choose your chance of Rock, Paper, Scissor"
    ), reply_markup=MainKeyboard)

# Handlers
def MainHandler(update, ctx):
    uid = update.effective_chat.id
    msg = update.message.text
    if 'started' not in ctx.user_data: 
        ctx.bot.send_message(chat_id=uid, text="You haven't /start ed the bot yet!")
        return
    if msg == t['play_with_pc']:
        ctx.bot.send_message(chat_id=uid, text='User Wins: 0 \nComputer Wins: 0', reply_markup=PlayingKeyboard)
    elif msg == t['play_with_human']:
        ctx.user_data['matched'] = True
        if len(opponents):
            ctx.bot.delete_message(chat_id=uid, 
                                   message_id=ctx.user_data['last_msg_id'])
            matched_opponents[uid] = { 'choice': None, 'opp': opponents.pop(0) }
            ctx.bot.send_message(chat_id=uid, text='You: 0 \nOpponent: 0', reply_markup=PlayingKeyboard)
        else:
            opponents.append(uid)
            msg = ctx.bot.send_sticker(chat_id=uid, sticker='CAACAgIAAxkBAAIBNWFsyHc6GFVW1mOBA_vMsKwPVUhFAAJLAgACVp29CmJQRdBQ-nGcIQQ', reply_markup=CancelKeyboard)
            ctx.user_data['last_msg_id'] = msg.message_id
    elif msg == t['restart']:
        ctx.user_data['win_rate'] = {'c_wins':0, 'u_wins': 0, 'pl1':0, 'pl2': 0}
        ctx.bot.send_message(chat_id=uid, text='Restarted!')
    elif msg == t['leaderboard']:
        pass


# Bot settings
BotToken = denv()['BotToken']
Bot = Updater(token=BotToken, use_context=True)

# Add handlers
dispatcher = Bot.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(ButtonHandler))
dispatcher.add_handler(MessageHandler(Filters.regex(r'(?!Pl|Re)(^[rpsRPS])'), TextChoiceHandler))
dispatcher.add_handler(MessageHandler(Filters.text, MainHandler))
# dispatcher.add_handler(MessageHandler(Filters.sticker, GetSticker))

# Start & Stop
Bot.start_polling()
Bot.idle() # to stop the bot with ctrl + c or custom signals
