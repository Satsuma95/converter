from aiogram import Dispatcher, types
from cfg import bot
from buttons.inline_user import *


async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'привет')

async def _return(message: types.Message):
    await bot.send_message(message.chat.id, 'привет дружище')

def reg_h_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start','return'])
    dp.register_message_handler(start, content_types=["video"])
   



