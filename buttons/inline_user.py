from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
def zakrutochki():
    spisok = InlineKeyboardMarkup()
    a = InlineKeyboardButton("jpg->png",callback_data="jpg")
    b = InlineKeyboardButton("png->jpg",callback_data="png")
    c = InlineKeyboardButton("mp3->mp4",callback_data="mp3")
    d = InlineKeyboardButton("mp4->mp3",callback_data="mp4")
    spisok.add(a,b,c,d)
    return spisok