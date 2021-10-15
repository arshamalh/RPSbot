from telegram.ext import Updater
from telegram.ext import CommandHandler
BotToken = "1987640815:AAEdOu-w47RcYRCFoTQognLmg6QKZDvkgPA"
updater = Updater(token=BotToken, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()