import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS,CHANNELS
from loader import dp, db, bot
from keyboards.inline.inline_button import inline_markup
from keyboards.default.defoult_markup import asosiy_menyu
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message,state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    # await message.answer(f"Salom, {message.from_user.full_name}!\nYangi e'lon berishni hohlaysizmi?", reply_markup=menu)
    # db.add_user(id=message.from_user.id,name=name)
    channels_format = str()
    markup = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"📌 <a href='{invite_link}'><b>{chat.title}</b></a>\n\n"
        markup.insert(InlineKeyboardButton(text=f"{chat.title}",url=invite_link))
        # check_button = InlineKeyboardMarkup(text="✅ Obunani tekshirish", callback_data="check_subs")
    markup.insert(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs"))
    
    # Foydalanuvchini bazaga qo'shamiz

    try:
        db.add_user(id=message.from_user.id,name=name)
        # await message.answer(f"Сиз асосий менюдасиз",reply_markup=asosiy_menyu)
        # await message.answer(f"'Uzauto' ботга хуш келибсиз, керакли бўлимни танланг👇",reply_markup=inline_markup)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        
        msg = f"🙎🏻‍♂️ <b>{message.from_user.full_name}</b> botga start bosdi\n📧 Username: @{message.from_user.username}\n🆔 ID: <code>{message.from_user.id}</code>\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')
        await message.answer(f"Xush kelibsiz {name}\nQuyidagi kanallarga obuna bo'ling: \n\n"
                         f"{channels_format}",
                         reply_markup=markup,
                         disable_web_page_preview=True)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"🙎🏻‍♂️ <b>{name}</b> botga oldin start bosgan\n📧 Username: @{message.from_user.username}\n🆔 ID: <code>{message.from_user.id}</code>")
        await message.answer(f"Xush kelibsiz {name}\nQuyidagi kanallarga obuna bo'ling: \n\n"
                         f"{channels_format}",
                         reply_markup=markup,
                         disable_web_page_preview=True,parse_mode='HTML')
        # await message.answer(f"Сиз асосий менюдасиз",reply_markup=asosiy_menyu)
        # await message.answer(f"'Uzauto' ботга хуш келибсиз, керакли бўлимни танланг👇",reply_markup=inline_markup)
        
