import time
import asyncio
from aiogram import F,Router, types
from aiogram.utils.markdown import hide_link
from aiogram.types import Message, ChatPermissions
from aiogram.filters import CommandStart,Command
import app_1.keyboard as kb
from app.fff import ID
from app.ff import GROUP_ID
from datetime import datetime, timedelta
from collections import defaultdict

router = Router()

# Словари для хранения информации о пользователях
user_messages_count = defaultdict(int)
user_muted_status = defaultdict(bool)

MUTE_DURATION = 120  # Длительность мута в секундах
MESSAGE_LIMIT = 3   # Лимит сообщений
warning_sent = defaultdict(bool)
#----------------------------------------------------------------------------------------------------------------------#


@router.message(CommandStart())
async def link(message:Message):
    user_name = message.from_user.full_name
    await message.bot.send_message(GROUP_ID,f"Пользователь {user_name} (@{message.from_user.username}) написал команду /start.")

    await message.answer(
                             'ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ‼️\n\n'
                             'Если ответ на ваш вопрос содержится в этой <a href="https://t.me/RomaDollar1/455"> ПУБЛИКАЦИИ</a> - вопрос будет проигнорирован.\n'
                             'Писать только по существу. Любой спам, смайлики, оскорбления, угрозы - вы будете заблокированы!',reply_markup=kb.main)
    time.sleep(2)
    await message.answer('🚀Напиши <b>"Прими в команду"</b> и начни зарабатывать сегодня! ')

@router.message(Command('privacy'))
async def privacy(message:Message):
    user_name = message.from_user.full_name
    await message.bot.send_message(GROUP_ID,f"Пользователь {user_name} (@{message.from_user.username}) написал команду /privacy.")
    await message.answer(f'{hide_link('https://telegra.ph/Politika-Konfidencialnosti-02-14-10')}'
                          f'Политика конфиденциальности')



#----------------------------------------------------------------------------------------------------------------------#


@router.message(F.text == 'Прими в команду')
async def cmd_start(message:Message):
    time.sleep(3)
    await message.answer('⏳ Пожалуйста ожидайте ~15 - 30 минут... Постараюсь ответить как можно быстрее! 🤝')
    time.sleep(4)
    await message.answer('💡Привет, твой путь к успеху начинается здесь!💰\n'
'Готов к новым возможностям? Мы научим тебя зарабатывать с нуля! 💼 Просто следуй инструкциям ниже и получай доход! 👇')
    time.sleep(2)
    await message.answer('🔼<b>3 ПРОСТЫХ ШАГА</b> 🔼\n'

f'1. 👉 <a href="https://bit.ly/4aZtLdp">Зарегистрируйся</a> {hide_link('https://bit.ly/4aZtLdp')}!📉\n'
'2. 👉 Пополни счёт от $10!💰\n'
'3. 👉 Напиши мне номер счёта ID!\n\n'
'Старая регистрация НЕ НУЖНА')
    time.sleep(2)
    await message.answer('Наши отзывы здесь\n'
                         f'{hide_link('https://t.me/RomaMoney2')}''<a href="https://t.me/RomaMoney2">📉Отзывы Трейдеров!</a>✍️')
    time.sleep(2)
    await message.answer(text=ID)
    time.sleep(1)
    await message.answer_photo(
                               'https://i.ibb.co/546d3k2/id.jpg')
    time.sleep(1)
    await message.answer('Отправьте свой ID нового аккаунта Pocket Option.\n'
                         '🔑 ВАЖНО❗️ Вводить ID нужно только цифрами - без букв❗️\n')






#----------------------------------------------------------------------------------------------------------------------#

@router.message(F.text == '📜 Политика конфиденциальности')
async def os(message:Message):
     await message.answer(f'{hide_link('https://telegra.ph/Politika-Konfidencialnosti-02-14-10')}'
                          f'Политика конфиденциальности')



#----------------------------------------------------------------------------------------------------------------------#
@router.message()
async def track_messages(message: types.Message):
    user_id = message.from_user.id

    # Если пользователь замучен, не реагируем на его сообщения
    if user_muted_status[user_id]:
        return

    user_messages_count[user_id] += 1

    # Проверяем, отправил ли пользователь слишком много сообщений
    if user_messages_count[user_id] > MESSAGE_LIMIT:
        if not warning_sent[user_id]:
            await message.answer("Предупреждение: Пожалуйста, не отправляйте слишком много сообщений.")
            warning_sent[user_id] = True
        else:
            # Мутим пользователя, если он продолжает отправлять много сообщений
            await message.answer("Вы были замучены за чрезмерное количество сообщений.")
            user_muted_status[user_id] = True
            user_messages_count[user_id] = 0  # Сбрасываем счетчик сообщений

            # Снятие мута после заданного времени
            await asyncio.sleep(MUTE_DURATION)
            user_muted_status[user_id] = False
            warning_sent[user_id] = False
            await message.answer("Вы больше не замучены и можете писать снова.")



