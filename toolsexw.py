import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types

#Telegram bot token
API_TOKEN = ''

#
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



#main menu
info = KeyboardButton('ℹ️ Информация о компании')
price = KeyboardButton('💲 Прайс лист')
callback = KeyboardButton('☎️Обратная связь')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(info).add(price).add(callback)

#infocat menu buttons
inf = KeyboardButton('О компании')
view = KeyboardButton('Нас смотрят')
backToMain = KeyboardButton('В главное меню')
infoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(inf).add(view).add(backToMain)

#Price
sixty = KeyboardButton('60 показов  в день')
fourty_five = KeyboardButton('45 показов  в день')
thirty = KeyboardButton('30 показов  в день')
backToMain = KeyboardButton('В главное меню')
price_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(sixty).add(fourty_five).add(thirty).add(backToMain)

