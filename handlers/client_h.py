import os
import moviepy
from aiogram import Dispatcher, types
from cfg import bot
from buttons.inline_user import *
from moviepy.editor import *


async def start(message: types.Message):
    buttons = zakrutochki()
    await bot.send_message(message.chat.id, 'привет',reply_markup=buttons)



async def _return(message: types.Message):
    await bot.send_message(message.chat.id, 'привет дружище')
    await download_video(message)


async def mp4(call: types.CallbackQuery):
    print(call)
async def download_video(message: types.Message):
    file_id = message.video.file_id
    file = await bot.get_file(file_id)
    await bot.download_file(file.file_path, "video.mp4")
    video = VideoFileClip(r"video.mp4")
    video.audio.write_audiofile("movie_sound.mp3")
    await bot.send_audio(message.chat.id, open('movie_sound.mp3', 'rb'))
def reg_h_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(_return, content_types=["video"])
    dp.register_callback_query_handler(mp4,lambda x: x.data == "mp4")

   



