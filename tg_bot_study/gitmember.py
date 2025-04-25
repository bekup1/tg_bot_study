from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command 
from aiogram.types import Message
from aiohttp import ClientSession

api_url = 'https://yesno.wtf/api'
bot_token:str = ''

bot = Bot(token=bot_token)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start_commad(message: Message):
    await message.answer('Hi bro.Welcome to russia.We a will create a great company.Now lets joking')

@dp.message(Command(commands=['help']))
async def process_help_command(message:Message):
    await message.answer('Help yourself')

@dp.message(Command(commands=['setting']))
async def process_help_command(message:Message):
    await message.answer('No setting')

@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)    

@dp.message(F.sticker)    
async def send_sticker_echo(message:Message):
    await message.reply_sticker(message.sticker.file_id)

@dp.message()
async def send_answer(message: Message):
    if '?' in message.text:
        async with ClientSession() as session:
            async with session.get(api_url) as resp:
                if resp.status == 200:
                    api_get = await resp.json()
                    im = api_get['image']
                    await message.answer_animation(im)
                else:
                    await message.answer("Ошибка загрузки картинки 😢")
    else: 
        await message.reply(text=message.text)
if __name__ == '__main__':
    dp.run_polling(bot)

