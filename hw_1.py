from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging

TOKEN1 = config("TOKEN1")
bot = Bot(TOKEN1)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Добро пожаловать на викторину! {message.from_user.full_name}")


@dp.message_handler(commands=['mem'])
async def mem(message:types.Message):
    photo = open("media_1.jpeg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open("media_1.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(commands=['quiz1'])
async def quiz_1(message: types.Message):
    question = "Какая самая маленькая планета в нашей Солнечной системе?: "
    answers = ["Земля", 'Венера', 'Марс', 'Меркурий']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        open_period=10,
                        reply_markup=markup
                        )

@dp.message_handler(commands=['quiz2'])
async def quiz_2(message: types.Message):
    question = "Сколько букв в русском алфавите?: "
    answers = ['31', '32', '33', '34']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,
                        reply_markup=markup1
                        )

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.isdigit():
        a = int(message.text)
        await message.answer(a ** 2)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)