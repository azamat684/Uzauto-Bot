from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from data.config import CHANNELS

# for channel in CHANNELS:
#     chat = await bot.get_chat(channel)
#     invite_link = await chat.export_invite_link()
#     check_button = InlineKeyboardMarkup(row_width=1,inline_keyboard=[[InlineKeyboardButton(text=f"{channel}",url=f"")]])
#     check_button.insert(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs"))
check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs")
    ]]
)
