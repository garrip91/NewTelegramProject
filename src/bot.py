from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import environ

env = environ.Env(
    # set casting, default value
    ADMIN=(int, 0)
)

environ.Env.read_env()


bot = Bot(token=env('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler(commands=['end'])
async def process_start_command(message: types.Message):
    await message.reply("Ну всё, так всё!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)