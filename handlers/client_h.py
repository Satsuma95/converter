from aiogram import Dispatcher, types
from cfg import bot
from buttons.inline_user import *


async def start(message: types.Message):
    buttons = zakrutochki()
    await bot.send_message(message.chat.id, 'привет',reply_markup=buttons)



async def _return(message: types.Message):
    await bot.send_message(message.chat.id, 'привет дружище')

async def mp4(call: types.CallbackQuery):
    print(call)
def reg_h_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(_return, content_types=["video"])
    dp.register_callback_query_handler(mp4,lambda x: x.data == "mp4")
   



