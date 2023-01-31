from aiogram import types
from utils.misc.subscription import check
from data.config import ADMINS, CHANNELS
from loader import dp, db, bot
from keyboards.inline.inline_button import inline_markup
from keyboards.inline.subscription import check_button

@dp.callback_query_handler(text="check_subs")
async def check_channel_member(call: types.CallbackQuery):
    user_id = call.from_user.id
    final_status = True
    result = ""
    for channel in CHANNELS:
        status = await check(user_id=user_id, channel=channel)
        channel = await bot.get_chat(channel)

        if status:
            final_status *= status
            invite_link = await channel.export_invite_link()
            result += f"✅ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lgansiz.\n\n"

        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n"
            await call.message.answer(text=result,disable_web_page_preview=True,reply_markup=check_button)

    if final_status:
        await call.message.delete()
        # await call.message.answer("Siz barcha kanallarga obuna bo'ldingiz. Botdan foydalanishingiz mumkin")
        await call.message.answer("<b>UzAuto</b> ботга хуш келибсиз, керакли бўлимни танланг👇",parse_mode='HTML',reply_markup=inline_markup)
    else:
        inline_markup_1 = types.InlineKeyboardMarkup(row_width=1)
        inline_markup_1.insert(types.InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs"))
        await call.message.edit_text(result, disable_web_page_preview=True, reply_markup=inline_markup_1)