from aiogram import Router
from aiogram import types

from aiogram.filters.command import Command

# from libs.gpt_lib import gpt_answer
# from aiogram.fsm.context import FSMContext


router = Router()


@router.channel_post(Command("getchid"))
async def rt_getchid(message: types.Message):
    chan_id = message.chat.id
    await message.reply(f"Channel id: <code>{chan_id}</code>")


@router.channel_post(Command("getid"))
async def rt_getid(message: types.Message):
    id = message.chat.id
    await message.reply(f"Channel id: <code>{id}</code>")


# @router.channel_post
# async def rt_test(message: types.Message):
#     await message.se