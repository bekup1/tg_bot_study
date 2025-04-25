from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command 
from aiogram.types import Message
from pprint import pprint

bot_token: str = '7395547960:AAGSpAKgd-9XWsXX42BTRCpJil5nR8YM2Tk'

bot = Bot(token=bot_token)
dp = Dispatcher()

@dp.message()
async def send_answer(message: Message):
    # Выводим полную структуру сообщения в консоль
    pprint(message.model_dump())
    
    # Создаем человекочитаемое сообщение
    response_text = (
        f"📩 Получено сообщение:\n"
        f"├ ID: {message.message_id}\n"
        f"├ От: {message.from_user.full_name} (@{message.from_user.username})\n"
        f"├ Текст: {message.text}\n"
        f"└ Дата: {message.date.strftime('%d.%m.%Y %H:%M:%S')}"
    )
    
    # Отправляем форматированный ответ
    await message.reply(text=response_text)
    
if __name__ == '__main__':
    dp.run_polling(bot)