import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5199501380:AAEUED2ksyLBA34IsMEdS4P2PF1uo506g_s'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start or /help command
    """
    await message.reply("Привет!\nЭто Википедия бот!\nЧто вы ищете?")


@dp.message_handler(commands="summary")
async def wiki(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        response=wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer('No info')\

@dp.message_handler(commands="page")
async def wiki(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        response=wikipedia.page(message.text)
        await message.answer(response)
    except:
        await message.answer('No info')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)