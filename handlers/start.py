from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandObject
from aiogram.types import Message
from loader import bot
router = Router()

@router.message(Command("start"))
async def start(message:Message,command: CommandObject):
    await message.answer(f'Привет, {message.from_user.full_name}!\n\nЭто бот для игры в кости и прочие игры в телеграм. Чтобы начать просто отправь один из эмодзи: 🎲, 🎯, 🏀, ⚽, 🎰, 🎳')