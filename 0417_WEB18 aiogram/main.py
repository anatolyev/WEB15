import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

# Bot token can be obtained via https://t.me/BotFather
from config import BOT_TOKEN

reply_keyboard = [[KeyboardButton(text='/address'), KeyboardButton(text='/phone')],
                  [KeyboardButton(text='/site'), KeyboardButton(text='/work_time')],
                  [KeyboardButton(text='/stop')],
                  ]
markup = ReplyKeyboardMarkup(keyboard=reply_keyboard,
                             resize_keyboard=True,
                             one_time_keyboard=False)



# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await message.reply("Привет", reply_markup=markup)

@dp.message(Command('stop'))
async def start(message: Message):
    await message.reply("Пока", reply_markup=ReplyKeyboardRemove())

@dp.message(Command('phone'))
async def start(message: Message):
    await message.reply("Телефон: 123-45-67")

@dp.message(Command('help'))
async def start(message: Message):
    await message.reply("Тут будет описание или помощь")

@dp.message(Command('address'))
async def start(message: Message):
    await message.reply("Адрес организации")

@dp.message(Command('site'))
async def start(message: Message):
    await message.reply("Сайт организации")

@dp.message(Command('work_time'))
async def start(message: Message):
    await message.reply("Рабочее время: бесконечно")

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем логирование
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, stream=sys.stdout
    )
    asyncio.run(main())