from core import checker
from Keyboards import PlayingKeyboard

def ButtonHandler(update, ctx):
    query = update.callback_query
    uid = update.effective_chat.id
    query.answer()
    if 'started' not in ctx.user_data: 
        ctx.bot.send_message(chat_id=uid, text="You haven't /start ed the bot yet!")
        return
    if query.data == 'c':
        ctx.bot.delete_message(chat_id=uid, 
                               message_id=ctx.user_data['last_msg_id'])
    else:
        text = checker(query.data, ctx.user_data['win_rate'])
        ctx.user_data['last_msg_id'] = query.message.message_id
        if text != ctx.user_data['last_msg_txt']:
            query.edit_message_text(text=text, reply_markup=PlayingKeyboard)
            ctx.user_data['last_msg_txt'] = text