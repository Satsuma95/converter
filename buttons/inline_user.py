from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
def zakrutochki():
    spisok = InlineKeyboardMarkup()
    a = InlineKeyboardButton("по скидке",callback_data="skidki")
    b = InlineKeyboardButton("профиль",callback_data="profile")
    spisok.add(a,b)
    return spisok