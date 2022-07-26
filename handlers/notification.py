import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text='Ok')


async def go_to_juma():
    await bot.send_message(chat_id=chat_id, text='Пора идти на Джума намаз!')


async def schedule():
    aioschedule.every().friday.at('13:30').do(go_to_juma)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)
