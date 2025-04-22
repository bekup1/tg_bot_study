from aiogram import Bot, Dispatcher
from aiogram.filters import Command 
from aiogram.types import Message

bot_token:str = '7718458852:AAEXau4ud0EvDmHa6jXC5z-vtG1ynGzmyZ0'

bot = Bot(token=bot_token)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start_commad(message: Message):
    await message.answer('Hi bro.Welcome to russia.We a will create a great company.Now lets joking')

@dp.message(Command(commands=['help']))
async def process_help_command(message:Message):
    await message.answer('Help yourself')

@dp.message()
async def send_echo(message:Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)

