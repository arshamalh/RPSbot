from telegram import InlineKeyboardMarkup, InlineKeyboardButton
# mainKeyboard = ReplyKeyboardMarkup(
#         keyboard=[
#             ["Restart"], ["Leaderboard"]
#         ])

PlayingKeyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Rock 💎", callback_data='r'),
             InlineKeyboardButton("Paper 📜", callback_data='p'),
             InlineKeyboardButton("Scissor ✂️", callback_data='s')],
            [InlineKeyboardButton("Restart 🔄", callback_data='a')]
        ])