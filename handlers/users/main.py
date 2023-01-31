from aiogram import types
from loader import dp, db, bot
from keyboards.inline.inline_button import turlari,inline_markup,type_cobalt,type_damas,damas_colour,cobalt_colour,malibu_colour,type_malibu,type_equinox,colour_equinox,type_tahoe,orqaga_news,avto_info,sotuv_damas,sotuvdagilar,type_lacetti,colour_lacetti,type_tracker,colour_tracker
import os
from keyboards.default.defoult_markup import asosiy_menyu

# from aiogram.utils.deep_linking import get_start_link, decode_payload
# from aiogram import types

# # хендлер для создания ссылок
# @dp.message_handler(commands=["ref"])
# async def get_ref(message: types.Message):
#   link = await get_start_link(str(f"https://t.me/for_testing_py_bot?start={message.from_user.id}"), encode=True)
#   # result: 'https://t.me/MyBot?start='
#   ## после знака = будет закодированный никнейм юзера, который создал реф ссылку, вместо него можно вставить и его id 
#   await message.answer(f"Sizning referal havolanggiz: {link}")

@dp.message_handler(text="🔃 Ботни қайта ишга тушириш",state="*")
async def bot_qayta_ishla(message: types.Message):
    await message.answer("Сиз асосий менюдасиз")
    await message.answer("<b>UzAuto</b> ботга хуш келибсиз, керакли бўлимни танланг👇",parse_mode='HTML',reply_markup=inline_markup)

@dp.callback_query_handler(text="avto_narxi")
async def avto_narxi(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)

@dp.callback_query_handler(text = "orqaga")
async def orqaga(call: types.CallbackQuery):
    await call.message.edit_text("'UzAuto' ботга хуш келибсиз, керакли бўлимни танланг👇",reply_markup=inline_markup)



@dp.callback_query_handler(text = "DAMAS")
async def orqaga(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхатдан танланг \n\n1. D2 STYLE   (86,971,000 сўм)\n2. D3 PLUS  (86,031,000 сўм)\n3. D3 STYLE (86,397,000 сўм)\n4. LB2 PLUS  (87,446,000 сўм)\n5. LB3 PLUS (84,910,000 сўм)\n6. LB3 STYLE  (85,124,000 сўм)\n7. D11 PLUS (ГРУЗОВОЙ) (83,904,000 сўм)\n8. D11 STYLE  (ГРУЗОВОЙ) (84,309,000 сўм)\n9. D2 PLUS (86,605,000 сўм)\n10. LB2 STYLE (87,660,000 сўм)",reply_markup=type_damas)

@dp.callback_query_handler(text = "d2style")
async def damas_d2style(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo="https://avtotexxizmat.uz/uploads/car-color/KK/KK/Kp/1635146425.png",caption="🕹 Позиция: D2 STYLE  \n💵 Нарх: 86,971,000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Summit White",reply_markup=damas_colour)

@dp.callback_query_handler(text="colour_gray")
async def gray(call: types.CallbackQuery):
    media_photo_1 = types.InputMediaPhoto(media="https://ibb.co/stFzPwR",caption="🕹 Позиция: D2 STYLE  \n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Artemis Gray")
    await call.message.edit_media(media=media_photo_1,reply_markup=damas_colour)

@dp.callback_query_handler(text="colour_white")
async def gray(call: types.CallbackQuery):
    media_photo_2 = types.InputMediaPhoto(media=("https://ibb.co/1mwWQ3n"),caption="🕹 Позиция: D2 STYLE  \n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Summit White")
    await call.message.edit_media(media=media_photo_2,reply_markup=damas_colour)

@dp.callback_query_handler(text = "colour_blue")
async def blue(call: types.CallbackQuery):
    media_photo_3 = types.InputMediaPhoto(media="https://ibb.co/qYPxqCq",caption="🕹 Позиция: D2 STYLE  \n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Blue")
    await call.message.edit_media(media=media_photo_3,reply_markup=damas_colour)
    
@dp.callback_query_handler(text = "colour_beige")
async def colour_bige(call: types.CallbackQuery):
    media_phot_4 = types.InputMediaPhoto(media="https://ibb.co/k5n2xGX",caption="🕹 Позиция: D2 STYLE  \n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги:  Smoke Beige")
    await call.message.edit_media(media=media_phot_4,reply_markup=damas_colour)    
    
    
@dp.callback_query_handler(text = "orqaga_2")
async def orqaga_2(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)
   
@dp.callback_query_handler(text = "orqaga_3")
async def orqaga_2(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Комплектасияни рўйхатдан танланг \n\n1. D2 STYLE   (86,971,000 сўм)\n2. D3 PLUS  (86,031,000 сўм)\n3. D3 STYLE (86,397,000 сўм)\n4. LB2 PLUS  (87,446,000 сўм)\n5. LB3 PLUS (84,910,000 сўм)\n6. LB3 STYLE  (85,124,000 сўм)\n7. D11 PLUS (ГРУЗОВОЙ) (83,904,000 сўм)\n8. D11 STYLE  (ГРУЗОВОЙ) (84,309,000 сўм)\n9. D2 PLUS (86,605,000 сўм)\n10. LB2 STYLE (87,660,000 сўм)",reply_markup=type_damas)

@dp.callback_query_handler(text = "COBALT")
async def orqaga(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхатдан танланг \n\n1.  GX/14ATB (124,295,000 сўм)\n2.  GX-STYLE AT (128,645,000 сўм)\n3.  GX-OPTIMA AT (127,145,000 сўм)\n4. GX/16ATB (4 ПОЗИЦИЯ МЕСТНОЙ КОМПЛЕКТАЦИИ) (125,795,000 сўм)",reply_markup=type_cobalt)
    


@dp.callback_query_handler(text = "gx14")
async def cobalt_gx14(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo="https://avtotexxizmat.uz/uploads/car-color/KK/KK/Kq/1635152522.png",caption="🕹 Позиция:  GX/14ATB\n💵 Нарх: 124,295,000 сўм\n🛢 100 км га сарфи: 8.5/9.0 L.\n🐎 Қуввати: 106 л.с. При 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Summit White",reply_markup=cobalt_colour)

@dp.callback_query_handler(text = "white")
async def damas_d2style(call:types.CallbackQuery):
    media_photo_4 = types.InputMediaPhoto(media="https://ibb.co/xMtMVMC",caption="🕹 Позиция:  GX/14ATB\n💵 Нарх: 124,295,000 сўм\n🛢 100 км га сарфи: 8.5/9.0 L.\n🐎 Қуввати: 106 л.с. При 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Summit White")
    await call.message.edit_media(media=media_photo_4,reply_markup=cobalt_colour)

@dp.callback_query_handler(text = "black")
async def damas_d2style1(call:types.CallbackQuery):
    media_photo_5 = types.InputMediaPhoto(media="https://ibb.co/KNh2KvV",caption="🕹 Позиция:  GX/14ATB\n💵 Нарх: 124,295,000 сўм\n🛢 100 км га сарфи: 8.5/9.0 L.\n🐎 Қуввати: 106 л.с. При 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Black")
    await call.message.edit_media(media=media_photo_5,reply_markup=cobalt_colour)
    
@dp.callback_query_handler(text = "blue")
async def damas_d2style1(call:types.CallbackQuery):
    media_photo_6 = types.InputMediaPhoto(media="https://ibb.co/xMg7CQg",caption="🕹 Позиция:  GX/14ATB\n💵 Нарх: 124,295,000 сўм\n🛢 100 км га сарфи: 8.5/9.0 L.\n🐎 Қуввати: 106 л.с. При 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Blue")
    await call.message.edit_media(media=media_photo_6,reply_markup=cobalt_colour)
    
@dp.callback_query_handler(text = "orqaga_4")
async def orqaga_2(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)

@dp.callback_query_handler(text = "orqaga_5")
async def oqaga_3(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Комплектасияни рўйхатдан танланг \n\n1.  GX/14ATB (124,295,000 сўм)\n2.  GX-STYLE AT (128,645,000 сўм)\n3.  GX-OPTIMA AT (127,145,000 сўм)\n4. GX/16ATB (4 ПОЗИЦИЯ МЕСТНОЙ КОМПЛЕКТАЦИИ) (125,795,000 сўм)",reply_markup=type_cobalt)

@dp.callback_query_handler(text="menyu")
async def manyu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Сиз асосий менюдасиз")
    await call.message.answer("'UzAuto' ботга хуш келибсиз, керакли бўлимни танланг👇",reply_markup=inline_markup)

@dp.callback_query_handler(text="MALIBU")
async def orqaga(call: types.CallbackQuery):
    await call.message.edit_text("Комплектасияни рўйхатдан танланг \n\n1. MALBDB2TL(LTZ) UVB (405,900,000 сўм)\n2. MALBDB2TL (2 ПОЗИЦИЯ, ТУРБО) (394,900,000 сўм)",reply_markup=type_malibu)

@dp.callback_query_handler(text="malbd")
async def malbd(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo="https://avtotexxizmat.uz/uploads/car-color/KK/KK/K8/1635153626.png",caption="🕹 Позиция: MALBDB2TL(LTZ) UVB\n💵 Нарх: 405,900,000.000 сўм\n🛢 100 км га сарфи: 8,5 л/100 км\n🐎 Қуввати: 253 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Summit white",reply_markup=malibu_colour)
    

@dp.callback_query_handler(text="malibu_white")
async def malibu_white(call: types.CallbackQuery):
    media_photo_7 = types.InputMediaPhoto(media="https://ibb.co/5YW1NnP",caption="🕹 Позиция: MALBDB2TL(LTZ) UVB\n💵 Нарх: 405,900,000.000 сўм\n🛢 100 км га сарфи: 8,5 л/100 км\n🐎 Қуввати: 253 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Summit white")
    await call.message.edit_media(media=media_photo_7,reply_markup=malibu_colour)
    
@dp.callback_query_handler(text="malibu_black")
async def malibu_black(call: types.CallbackQuery):
    media_photo_7 = types.InputMediaPhoto(media="https://ibb.co/ZLv2chm",caption="🕹 Позиция: MALBDB2TL(LTZ) UVB\n💵 Нарх: 405,900,000.000 сўм\n🛢 100 км га сарфи: 8,5 л/100 км\n🐎 Қуввати: 253 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: BLACK MET. KETTLE METALLIC")
    await call.message.edit_media(media=media_photo_7,reply_markup=malibu_colour)
    
@dp.callback_query_handler(text="malibu_silver")
async def malibu_silver(call: types.CallbackQuery):
    media_photo_7 = types.InputMediaPhoto(media="https://ibb.co/k68PJ8b",caption="🕹 Позиция: MALBDB2TL(LTZ) UVB\n💵 Нарх: 405,900,000.000 сўм\n🛢 100 км га сарфи: 8,5 л/100 км\n🐎 Қуввати: 253 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Swichblade Silver")
    await call.message.edit_media(media=media_photo_7,reply_markup=malibu_colour)
@dp.callback_query_handler(text = "orqaga_6")
async def orqaga_4(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)
   
@dp.callback_query_handler(text="orqaga_7")
async def orqaga_5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Комплектасияни рўйхатдан танланг \n\n1. MALBDB2TL(LTZ) UVB (405,900,000 сўм)\n2. MALBDB2TL (2 ПОЗИЦИЯ, ТУРБО) (394,900,000 сўм)",reply_markup=type_malibu)

@dp.callback_query_handler(text = "EQUINOX")
async def orqaga(call: types.CallbackQuery):
    await call.message.edit_text("Комплектасияни рўйхатдан танланг \n\n1. EQUINOX - AT 1LT FWD MH (389,000,000 сўм)\n2. EQUINOX - AT 1LT AWD MH (420,000,000 сўм)\n3. EQUINOX - AT 3LT AWD MH (450,000,000 сўм)",reply_markup=type_equinox)

@dp.callback_query_handler(text="equinox_1fwd")
async def equinox_dsa(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo="https://ibb.co/YPsww42",caption="🕹 Позиция: EQUINOX - AT 1LT FWD MH\n💵 Нарх: 389,000,000 сўм\n🛢 100 км га сарфи: 7,3 л/100 км\n🐎 Қуввати: 236 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 9 AT\n🎨 Ранги: BLACK MET. KETTLE METALLIC",reply_markup=colour_equinox)


@dp.callback_query_handler(text="equinox_black")
async def equinox_black(call: types.CallbackQuery):
    media_photo_8 = types.InputMediaPhoto(media="https://avtotexxizmat.uz/uploads/car-color/KK/KK/ho/1635155545.png",caption="🕹 Позиция: EQUINOX - AT 1LT FWD MH\n💵 Нарх: 389,000,000 сўм\n🛢 100 км га сарфи: 7,3 л/100 км\n🐎 Қуввати: 236 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 9 AT\n🎨 Ранги: BLACK MET. KETTLE METALLIC")
    await call.message.edit_media(media=media_photo_8,reply_markup=colour_equinox)


@dp.callback_query_handler(text="equinox_gray")
async def equinox_black(call: types.CallbackQuery):
    media_photo_9 = types.InputMediaPhoto(media="https://ibb.co/fXX55cx",caption="🕹 Позиция: EQUINOX - AT 1LT FWD MH\n💵 Нарх: 389,000,000 сўм\n🛢 100 км га сарфи: 7,3 л/100 км\n🐎 Қуввати: 236 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 9 AT\n🎨 Ранги: Satin Steel Gray Met-2")
    await call.message.edit_media(media=media_photo_9,reply_markup=colour_equinox)
    
@dp.callback_query_handler(text="equinox_white")
async def equinox_black(call: types.CallbackQuery):
    media_photo_10= types.InputMediaPhoto(media="https://ibb.co/yPm29qK",caption="🕹 Позиция: EQUINOX - AT 1LT FWD MH\n💵 Нарх: 389,000,000 сўм\n🛢 100 км га сарфи: 7,3 л/100 км\n🐎 Қуввати: 236 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 9 AT\n🎨 Ранги:  Summit White")
    await call.message.edit_media(media=media_photo_10,reply_markup=colour_equinox)

@dp.callback_query_handler(text="equinox_drake")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media="https://ibb.co/d6G9n8J",caption="🕹 Позиция: EQUINOX - AT 1LT FWD MH\n💵 Нарх: 389,000,000 сўм\n🛢 100 км га сарфи: 7,3 л/100 км\n🐎 Қуввати: 236 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 9 AT\n🎨 Ранги:  Summit White")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_equinox)
@dp.callback_query_handler(text = "orqaga_8")
async def oqaga_3(call: types.CallbackQuery):
    await call.message.edit_text(text="Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)
    

@dp.callback_query_handler(text = "orqaga_9")
async def orqaga(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Комплектасияни рўйхатдан танланг \n\n1. EQUINOX - AT 1LT FWD MH (389,000,000 сўм)\n2. EQUINOX - AT 1LT AWD MH (420,000,000 сўм)\n3. EQUINOX - AT 3LT AWD MH (450,000,000 сўм)",reply_markup=type_equinox)
   
@dp.callback_query_handler(text = "TAHOE")
async def orqaga(call: types.CallbackQuery):
    await call.message.edit_text("Комплектасияни рўйхатдан танланг \n\n1. TAHOE-2 RST (947,500,000 сўм)",reply_markup=type_tahoe)

@dp.callback_query_handler(text = "orqaga_10")
async def oqaga_3(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)
# @dp.callback_query_handler(text = "orqaga_11")
# async def oqaga_3(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Комплектасияни рўйхатдан танланг \n\n1. TAHOE-2 RST (947,500,000 сўм)",reply_markup=type_tahoe)



@dp.callback_query_handler(text="LACETTI")
async def lacetti(call: types.CallbackQuery):
    await call.message.edit_text("Комплектасияни рўйхатдан танланг \n\n1. L-COMFORT PLUS (128,284,000 сўм)\n2. L-ELEGANT/AT PLUS (153,506,000 сўм)\n3. L-STYLE MT (131,134,000 сўм)\n4. L-STYLE AT (156,356,000 сўм)\n5. L-OPTIMA AT (153,101,000 сўм)",reply_markup=type_lacetti)

@dp.callback_query_handler(text="l_optima_at")
async def l_optima_lacetti(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo="https://avtotexxizmat.uz/uploads/car-color/KK/KK/K0/1635153004.png",caption="🕹 Позиция:<b> L-OPTIMA AT</b>\n\n💵 Нарх: <b>153,101,000 сўм</b>\n🛢 100 км га сарфи: <b>7.5/9.5 L.</b>\n🐎 Қуввати:<b>107 л.с. при 5800 об/мин</b>\n⚙️ Трансмиссия: <b>6 AT</b>\n🎨 Ранги: <b>BLACK MET. KETTLE METALLIC</b>",parse_mode='HTML',reply_markup=colour_lacetti)
    

@dp.callback_query_handler(text="lacetti_black")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media="https://ibb.co/FVyFVBY",caption="🕹 Позиция: L-OPTIMA AT\n💵 Нарх: 153,101,000 сўм\n🛢 100 км га сарфи: 7.5/9.5 L.\n🐎 Қуввати: 107 л.с. при 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: BLACK MET. KETTLE METALLIC")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_lacetti)

@dp.callback_query_handler(text="lacetti_white")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media="https://ibb.co/1z1pfGS",caption="🕹 Позиция: L-OPTIMA AT\n💵 Нарх: 153,101,000 сўм\n🛢 100 км га сарфи: 7.5/9.5 L.\n🐎 Қуввати: 107 л.с. при 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Summit White")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_lacetti)

@dp.callback_query_handler(text="lacetti_blue")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media="https://ibb.co/BVTsVQ6",caption="🕹 Позиция: L-OPTIMA AT\n💵 Нарх: 153,101,000 сўм\n🛢 100 км га сарфи: 7.5/9.5 L.\n🐎 Қуввати: 107 л.с. при 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Light Blue")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_lacetti)
    
@dp.callback_query_handler(text="lacetti_red")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media="https://ibb.co/k6JQmWm",caption="🕹 Позиция: L-OPTIMA AT\n💵 Нарх: 153,101,000 сўм\n🛢 100 км га сарфи: 7.5/9.5 L.\n🐎 Қуввати: 107 л.с. при 5800 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Red - E or Not")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_lacetti)

@dp.callback_query_handler(text="orqaga_11")
async def orqaga_11(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)
    
@dp.callback_query_handler(text="orqaga_12")
async def orqaga_11(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Комплектасияни рўйхатдан танланг \n\n1. L-COMFORT PLUS (128,284,000 сўм)\n2. L-ELEGANT/AT PLUS (153,506,000 сўм)\n3. L-STYLE MT (131,134,000 сўм)\n4. L-STYLE AT (156,356,000 сўм)\n5. L-OPTIMA AT (153,101,000 сўм)",reply_markup=type_lacetti)
        
@dp.callback_query_handler(text='TRACKER')
async def tracker(call: types.CallbackQuery):
    await call.message.edit_text("Комплектасияни рўйхатдан танланг \n\n1. TRACKER-2 TRK LS (211,454,880 сўм)\n2. TRACKER-2 TRK LTZ (231,196,000 сўм)\n3. TRACKER-2 TRK PREMIER (251,142,080 сўм)",reply_markup=type_tracker)


@dp.callback_query_handler(text="tracker_trk")
async def tracker_trk(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo="https://avtotexxizmat.uz/uploads/car-color/KK/KK/KN/1635155209.png",caption="🕹 Позиция: TRACKER-2 TRK LS\n💵 Нарх: 211,454,880 сўм\n🛢 100 км га сарфи: 6,9л/100 км\n🐎 Қуввати: 140 при 6200 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: BLACK MET. KETTLE METALLIC",reply_markup=colour_tracker)

@dp.callback_query_handler(text="tracker_black")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media="https://ibb.co/PcKySCF",caption="🕹 Позиция: TRACKER-2 TRK LS\n💵 Нарх: 211,454,880 сўм\n🛢 100 км га сарфи: 6,9л/100 км\n🐎 Қуввати: 140 при 6200 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: BLACK MET. KETTLE METALLIC")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_tracker)


@dp.callback_query_handler(text="tracker_white")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media='https://ibb.co/hKwM0Yz',caption="🕹 Позиция: TRACKER-2 TRK LS\n💵 Нарх: 211,454,880 сўм\n🛢 100 км га сарфи: 6,9л/100 км\n🐎 Қуввати: 140 при 6200 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Summit White")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_tracker)


@dp.callback_query_handler(text="tracker_red")
async def equinox_black(call: types.CallbackQuery):
    media_photo_11 = types.InputMediaPhoto(media='https://ibb.co/vJgkjkB',caption="🕹 Позиция: TRACKER-2 TRK LS\n💵 Нарх: 211,454,880 сўм\n🛢 100 км га сарфи: 6,9л/100 км\n🐎 Қуввати: 140 при 6200 об/мин\n⚙️ Трансмиссия: 6 AT\n🎨 Ранги: Red - E or Not")
    await call.message.edit_media(media=media_photo_11,reply_markup=colour_tracker)
    
@dp.callback_query_handler(text="orqaga_13")
async def orqaga_11(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=turlari)
    
    
@dp.callback_query_handler(text="orqaga_14")
async def orqaga_11(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Комплектасияни рўйхатдан танланг \n\n1. TRACKER-2 TRK LS (211,454,880 сўм)\n2. TRACKER-2 TRK LTZ (231,196,000 сўм)\n3. TRACKER-2 TRK PREMIER (251,142,080 сўм)",reply_markup=type_tracker)    

@dp.callback_query_handler(lambda call: call.data in ["gxstyle","gxoptima","gx16","d3plus","d3style","lb2plus","lb3plus","lb3style","equinox_1awd",'equinox_3awd','tahoe_2','l_comfort','l_elegenta','l_style_mt','l_style_at','ONIX',"malbd2",'damas_info','cobalt_info','malibu_info','tahoe_info','equinox_info','tracker_info']) 
async def al_cars(call: types.CallbackQuery):
    await call.answer("❌ Ҳали бу автомобил тури бўйича менда информатсия йўқ!")   
    
    
###########################################    
    
@dp.callback_query_handler(text="yangiliklar")
async def news(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://ibb.co/XYjLXft",caption="⚡️Айни вақтда Чевролет Оних автомобилининг қуйидаги комплектацияларига буюртма бериш мумкин ҚҚС билан хисобланган нархлар:\n\n1,2 МТ Соддалаштирилган комплектация*– 110 000 000 сўм \n1ЛС 1,2 МТ – 152 996 000 сўм \n1ЛТ 1,2 МТ – 159 160 000 сўм \n3ЛТ 1.2 МТ – 163 254 000 сўм \nЛТЗ 1,2 Турбо АТ – 189 957 000 сўм")
    await call.message.answer_photo(photo="https://ibb.co/z2txm7F",caption="⚡️Машхур BYD Ўзбекистонда электрокарлар ишлаб чиқаради\n\n⚡️Машхур BYD Ўзбекистонда электрокарлар ишлаб чиқаради\n\nХитойнинг BYD компанияси ва Ўзавтосаноат (UzAvto) акциядорлик жамияти Ўзбекистонда электрокар ишлаб чиқариш бўйича қўшма корхона ташкил этиш тўғрисида келишув имзолабди.\n\nПс: Ишқилиб BYD хам айниб кетмаса бўлди монополларни таъсири остида, сифатли рақобатбардош мошиналар кутиб қоламиз")
    await call.message.answer_photo(photo="https://ibb.co/BgsQvLW",caption="«Автомобиллар учун шартнома тузиш вақтинча тўхтатилди» - UzAuto Motors\n\nUzAuto Motors бугундан шартнома бериш, автомобилларни топшириш ва тўловларни амалга оширишни вақтинча тўхтатди Бу ҳолат 4-5 кун давом этиши мумкинлиги айтилмоқда.")
    await call.message.answer_photo(photo="https://ibb.co/sVMHP84",caption="⚡️ Ўзбекистонда феврал ойидан дунёга машҳур BYD электромобиллари сотила бошлайди\n\nДунёдаги энг йирик электромобил ишлаб чиқарувчи BYD бир ойдан сўнг – февралда сотувни бошлайди.  Нархлар ишлаб чиқарувчидан кафолат ва хизмат кўрсатиш билан бошқа автосалонларга қараганда қулайроқ бўлади.")
    await call.message.answer_photo(photo="https://ibb.co/m6GW6nQ",caption="⚡️'УзАутоМоторс' ҚҚС пасайтирилиши муносабати билан харидорларга пулнинг бир қисмини (автомобил нархининг 2,6 фоизи) қайтаради.\n\nҚҚС пасайтирилиши муносабати билан УзАуто Моторс 2022-йилда шартнома имзолаган харидорларга автомобил нархининг 2,6 фоизини қайтариб беради ва автомобил 2023-йилда олиниши ёки аллақачон олиниши керак. Масалан, Оних учун тўлаганлар тахминан 5 миллионни қайтариб олинг, Гентра учун - 4 миллион ва ҳоказо.",reply_markup=orqaga_news)
    
@dp.callback_query_handler(text = "orqaga_news")
async def oqaga_news(call: types.CallbackQuery):
    await call.message.answer("Сиз асосий менюдасиз")
    await call.message.answer("'UzAuto' ботга хуш келибсиз, керакли бўлимни танланг👇",reply_markup=inline_markup)


#SOTUVDAGI AVTOMOBILLAR QISMI
@dp.callback_query_handler(text="sotuvdagi_moshinalar")
async def sotuvdagi_cars(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=sotuvdagilar)

@dp.callback_query_handler(text="damas_sotuv")
async def damas_sotuv(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхати\n\n1) D2 STYLE  🆓 сотувда бор: 0\n🔄 навбатда: 59130\n\n2) D3 PLUS \n🆓 сотувда бор: 0\n🔄 навбатда: 0\n\n3) D3 STYLE\n🆓 сотувда бор: 0\n🔄 навбатда: 258\n\n4) LB2 PLUS \n🆓 сотувда бор: 0\n🔄 навбатда: 11975\n\n5) LB3 PLUS\n🆓 сотувда бор: 0\n🔄 навбатда: 1142\n\n6) LB3 STYLE \n🆓 сотувда бор: 0\n🔄 навбатда: 0\n\n7) D11 PLUS (ГРУЗОВОЙ)\n🆓 сотувда бор: 0\n🔄 навбатда: 121\n\n8) D11 STYLE  (ГРУЗОВОЙ)\n🆓 сотувда бор: 0\n🔄 навбатда: 182\n\n9) LB2 STYLE\n🆓 сотувда бор: 0\n🔄 навбатда: 951\n\n10) D2 PLUS\n🆓 сотувда бор: 1\n🔄 навбатда: 348",reply_markup=sotuv_damas)

@dp.callback_query_handler(text="cobalt_sotuv")
async def damas_sotuv(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхати\n\n1)  GX/14ATB\n🆓 сотувда бор: 0\n🔄 навбатда: 0\n\n2)  GX-STYLE AT\n🆓 сотувда бор: 0\n🔄 навбатда: 43027\n\n3)  GX-OPTIMA AT\n🆓 сотувда бор: 8\n🔄 навбатда: 11912",reply_markup=sotuv_damas)

@dp.callback_query_handler(text="cobalt_sotuv")
async def damas_sotuv(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхати\n\n1)  GX/14ATB\n🆓 сотувда бор: 0\n🔄 навбатда: 0\n\n2)  GX-STYLE AT\n🆓 сотувда бор: 0\n🔄 навбатда: 43027\n\n3)  GX-OPTIMA AT\n🆓 сотувда бор: 8\n🔄 навбатда: 11912",reply_markup=sotuv_damas)

@dp.callback_query_handler(text="malibu_sotuv")
async def damas_sotuv(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхати\n\n1) MALBDB2TL (2 ПОЗИЦИЯ, ТУРБО)\n🆓 сотувда бор: 3\n🔄 навбатда: 56\n\n2) MALBDB2TL(LTZ) UVB\n🆓 сотувда бор: 13\n🔄 навбатда: 759",reply_markup=sotuv_damas)
    
@dp.callback_query_handler(text="equinox_sotuv")
async def damas_sotuv(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхати\n\n1) EQUINOX - AT 1LT FWD MH\n🆓 сотувда бор: 1\n🔄 навбатда: 5\n\n2) EQUINOX - AT 1LT AWD MH\n🆓 сотувда бор: 7\n🔄 навбатда: 200\n\n3) EQUINOX - AT 3LT AWD MH\n🆓 сотувда бор: 10\n🔄 навбатда: 621",reply_markup=sotuv_damas)
    
@dp.callback_query_handler(text="tahoe_sotuv")
async def damas_sotuv(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхати\n\n1) TAHOE-2 RST\n🆓 сотувда бор: 0\n🔄 навбатда: 25",reply_markup=sotuv_damas)
    
@dp.callback_query_handler(text="lacetti_sotuv")
async def damas_sotuv(call: types.CallbackQuery):
    await call.message.edit_text(f"Комплектасияни рўйхати\n\n1) L-OPTIMA AT\n🆓 сотувда бор: 0\n🔄 навбатда: 3314",reply_markup=sotuv_damas)
#AVTO INFO QISMI
@dp.callback_query_handler(text="info")
async def avto_infosi(call: types.CallbackQuery):
    await call.message.edit_text("Автомобиллардан бирини танланг",reply_markup=avto_info)
    
@dp.callback_query_handler(text="orqaga_sotuv_2")
async def sss(call: types.CallbackQuery):
    await call.message.edit_text("Пастдаги рўйхатдан машинани танланг ⬇️",reply_markup=sotuvdagilar)

@dp.callback_query_handler(text="orqaga_sotuv")
async def sss(call: types.CallbackQuery):
    await call.message.edit_text("'UzAuto' ботга хуш келибсиз, керакли бўлимни танланг👇",reply_markup=inline_markup)

@dp.callback_query_handler(text="damas_info")
async def damas_info(call:types.CallbackQuery):
    await call.answer("❌ Bu funksiya hali qo'shilmadi ")



@dp.callback_query_handler(text="orqaga_info")
async def avto_infosi(call: types.CallbackQuery):
    await call.message.edit_text("'UzAuto' ботга хуш келибсиз, керакли бўлимни танланг👇",reply_markup=inline_markup)