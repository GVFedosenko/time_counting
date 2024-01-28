from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message):
    await message.answer(f"""
    Привет, этот бот предназначен для учета времени переработок и возможности тратить их
на отгулы или удаленную работу.
Для начала необходимо добавить свое ФИО + уже накопленные часы.
Сделать это можно командой:
/add_me""")

@dp.message()



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())