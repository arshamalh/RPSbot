from time import sleep
from core import checker
from utiles.Keyboards import PlayingKeyboard

def TextChoiceHandler(update, ctx):
    uid = update.effective_chat.id
    if 'started' not in ctx.user_data: 
        ctx.bot.send_message(chat_id=uid, text="You haven't /start ed the bot yet!")
        return
    msg = update.message
    text = checker(msg.text, ctx.user_data['win_rate'])
    if ctx.user_data['last_msg_id']:
        if text != ctx.user_data['last_msg_txt']:
            ctx.bot.edit_message_text(chat_id=uid, 
                                    message_id=ctx.user_data['last_msg_id'], 
                                    text=text, reply_markup=PlayingKeyboard)
            ctx.user_data['last_msg_txt'] = text
    else:
        ctx.bot.send_message(chat_id=uid, text=text, reply_markup=PlayingKeyboard)
        ctx.user_data['last_msg_id'] = msg.message_id
    
    sleep(3)
    ctx.bot.delete_message(chat_id=uid, message_id=msg.message_id)