from cfg import dp
from aiogram import executor
from handlers.client_h import reg_h_client
from handlers.admin_h import reg_h_admin

reg_h_client(dp)
reg_h_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


"""
1. При отправке видео - бот отвечает "привет", а должен "привет ,дружище". Пофиксить ;)
2. Найти дополнительные варианты с конвертером, по типу:
из мов в мп3
из мов в мп4
из пнг в джпег
из джпег в пнг
и другие) просото оставить их в "помойке"😁
"""