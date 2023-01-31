import logging
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import CHANNELS
from aiogram import types
from loader import bot
from utils.misc.subscription import check


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ["/start"]:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data in ["check_subs"]:
                return
        else:
            return
        logging.info(user)

        result = str()
        final_status = True

        for channel in CHANNELS:
            status = await check(user_id=user, channel=channel)
            final_status *= status
            channel = await bot.get_chat(chat_id=channel)
            if not status:
                invite_link = await channel.export_invite_link()
                result += f"❌ <a href='{invite_link}'><b>{channel.title}</b></a>\n"
        
        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True)
            raise CancelHandler()