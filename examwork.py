import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from toolsexw import *



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
dp = Dispatcher(bot)

welcome_message=("Добро пожаловать!\nЭто бот рекламного агентства Lemon Media!\n"
                 "Он поможет вам ознакомиться с нашими ценами и нашей комапиней.")

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start or /help command
    """
    await message.reply(welcome_message, reply_markup=mainmenu)

@dp.message_handler(text = 'ℹ️ Информация о компании')
async def infocat(message: types.Message):
    await message.answer('Что выхотите просмотреть?', reply_markup=infoMenu)

@dp.message_handler(text = '💲 Прайс лист')
async def infocat(message: types.Message):
    await message.answer('Выберите количество просмотров в день:', reply_markup=price_menu)
@dp.message_handler(text = 'В главное меню')
async def backtomainmenu(message: types.Message):
    await message.answer('Какой раздел выберите?', reply_markup=mainmenu)

text=('Торговая марка Lemon Media предлагает свои услуги по размещению рекламы в сфере InDoor - рекламы.\n'
      'Наша компания начиная с 2018 года оказывала свои услуги таким крупным компаниям как “PEPSI”, '
      '“BLISS”, “Uztelecom” и другим компаниям которые ведут свою деятельность в нашей республике. ')
@dp.message_handler(text = 'О компании')
async def company_info(message: types.Message):
    await message.answer(text)

mon_info=('''Наша компания сотрудничает с такими сетями кафе, такими как 
"Evos", "Les Ailes", "Totus" и другими заведениями  по всей республике.
Мы размещаем рекламу на мониторах которые находятся в залах этих заведений. \n
Количество филиалов  по Республике - 56.\n Ежемесячная аудитория - более чем 1,5 млн.  человек. ''')
@dp.message_handler(text = 'Нас смотрят')
async def monit_info(message: types.Message):
    await message.answer(mon_info)

@dp.message_handler(text = '60 показов  в день')
async def sixtyt(message: types.Message):
    await message.answer(''' 60 показов в день.\nЧастота показов в рекламных  блоках -в каждом рекламном блоке по 2 раза.\n
Цена на размещение  при месячном пакете  (без скидки) - 19 000 000.\nПри долгосрочном договоре имеются скидки.''')

@dp.message_handler(text = '45 показов  в день')
async def f_ft(message: types.Message):
    await message.answer(''' 45 показов в день.\nЧастота показов в рекламных  блоках -в каждом рекламном блоке.\n
Цена на размещение  при месячном пакете  (без скидки) - 15 000 000.\nПри долгосрочном договоре имеются скидки.''')

@dp.message_handler(text = '30 показов  в день')
async def thirtyt(message: types.Message):
    await message.answer(''' 30 показов в день.\nЧастота показов в рекламных  блоках -в каждом 2м рекламном блоке.\n
Цена на размещение  при месячном пакете  (без скидки) - 11 000 000.\nПри долгосрочном договоре имеются скидки.''')

@dp.message_handler(text = '☎️Обратная связь')
async def monit_info(message: types.Message):
    await message.answer(''' По поводу сотрудничества или если у вас возникли вопросы звоните по номеру: +998 99 828-88-28. 
Так же можете написать на этот же номер по Telegram.''')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
