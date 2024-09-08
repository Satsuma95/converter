from aiogram import Dispatcher, types
from cfg import bot


async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'hello ;)')


def reg_h_admin(dp: Dispatcher):
    dp.register_message_handler(start, commands=['example'])
