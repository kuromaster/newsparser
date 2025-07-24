from aiogram import Router
from aiogram import types

from aiogram.filters.command import Command

# from libs.gpt_lib import gpt_answer
# from aiogram.fsm.context import FSMContext


router = Router()


@router.channel_post(Command("getid"))
async def rt_getid(message: types.Message):
    id = message.chat.id
    await message.reply(f"Telegram id: <code>{id}</code>")
