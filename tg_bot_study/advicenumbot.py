from aiogram import F, Bot, Dispatcher
from aiogram.filters import Filter ,Command
from aiogram.types import Message
from aiohttp import ClientSession
from random import *


bot_token:str = '7395547960:AAGSpAKgd-9XWsXX42BTRCpJil5nR8YM2Tk'

bot = Bot(token = bot_token)
dp = Dispatcher()

num:int =  randint(1,100)
print(num)
