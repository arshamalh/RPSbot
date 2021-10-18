from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from Titles import titles as t
MainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [t['play_with_pc'], t['play_with_human']],
        [t['restart'], t['leaderboard']]
    ])

PlayingKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Rock 💎", callback_data='r'),
         InlineKeyboardButton("Paper 📜", callback_data='p'),
         InlineKeyboardButton("Scissor ✂️", callback_data='s')],
    ])

CancelKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Cancel ❌", callback_data='c')],
    ])
    