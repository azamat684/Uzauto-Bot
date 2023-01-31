from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💲 Автомобил нархлари",callback_data='avto_narxi')],
    [InlineKeyboardButton(text="ℹ️ сотувда борлиги тўғрисида малумот",callback_data='sotuvdagi_moshinalar')],
    [InlineKeyboardButton(text="🆕 Сўнги янгиликлар",callback_data='yangiliklar')],
    [InlineKeyboardButton(text="🚘 Автомобил информатсияцси",callback_data='info')]
])


turlari = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="DAMAS (83,904,000 сўм дан)",callback_data='DAMAS')],
    [InlineKeyboardButton(text="COBALT (124,295,000 сўм дан)",callback_data='COBALT')],
    [InlineKeyboardButton(text="MALIBU-2 (394,900,000 сўм дан)",callback_data='MALIBU')],
    [InlineKeyboardButton(text="EQUINOX (389,000,000 сўм дан)",callback_data='EQUINOX')],
    [InlineKeyboardButton(text="TAHOE (947,500,000 сўм дан)",callback_data='TAHOE')],
    [InlineKeyboardButton(text="LACETTI (128,284,000 сўм дан)",callback_data='LACETTI')],
    [InlineKeyboardButton(text="TRACKER 2 (209,000,000 сўм дан)",callback_data='TRACKER')],
    [InlineKeyboardButton(text="ONIX (152,996,000 сўм дан)",callback_data='ONIX')],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga')]
])

type_damas=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="D2 STYLE",callback_data="d2style")],
    [InlineKeyboardButton(text="D3 PLUS",callback_data="d3plus")],
    [InlineKeyboardButton(text="D3 STYLE",callback_data="d3style")],
    [InlineKeyboardButton(text="LB2 PLUS",callback_data="lb2plus")],
    [InlineKeyboardButton(text="LB3 PLUS",callback_data="lb3plus")],
    [InlineKeyboardButton(text="LB3 STYLE",callback_data="lb3style")],  
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_2')] 
])
damas_colour = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Summit White",callback_data="colour_white")],
    [InlineKeyboardButton(text="Artemis Gray",callback_data="colour_gray")],
    [InlineKeyboardButton(text='Blue',callback_data='colour_blue')],
    [InlineKeyboardButton(text="Smoke Beige",callback_data="colour_beige")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_3'),InlineKeyboardButton(text="🏠 Бош меню",callback_data="menyu")]
])


type_cobalt=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="GX/14ATB",callback_data="gx14")],
    [InlineKeyboardButton(text="GX-STYLE AT",callback_data="gxstyle")],
    [InlineKeyboardButton(text="GX-OPTIMA AT",callback_data="gxoptima")],
    [InlineKeyboardButton(text="GX/16ATB",callback_data="gx16")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_4')]
])

cobalt_colour = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Summit White",callback_data="white")],
    [InlineKeyboardButton(text="BLACK MET.KETTLE METALLIC",callback_data="black")],
    [InlineKeyboardButton(text='Blue',callback_data='blue')],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_5'),InlineKeyboardButton(text="🏠 Бош меню",callback_data="menyu")]
])

type_malibu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="MALBDB2TL(LTZ)UVB",callback_data='malbd')],
    [InlineKeyboardButton(text="MALBDB2TL (2 ПОЗИЦИЯ,ТУРБО)",callback_data='malbd2')],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_6')]
])
malibu_colour = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Summit White",callback_data="malibu_white")],
    [InlineKeyboardButton(text="BLACK MET.KETTLE METALLIC",callback_data="malibu_black")],
    [InlineKeyboardButton(text='Swichblade Silver',callback_data='malibu_silver')],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_7'),InlineKeyboardButton(text="🏠 Бош меню",callback_data="menyu")]
])

type_equinox = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="EQUINOX-AT 1LT FWD MH",callback_data="equinox_1fwd")],
    [InlineKeyboardButton(text="EQUINOX-AT 1LT AWD MH",callback_data="equinox_1awd")],
    [InlineKeyboardButton(text="EQUINOX-AT3LT AWD MH",callback_data="equinox_3awd")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_8')]
])

colour_equinox = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="BLACK MET.KETTLE METALLIC",callback_data='equinox_black')],
    [InlineKeyboardButton(text="Satin Steel Gray Met+2",callback_data='equinox_gray')],
    [InlineKeyboardButton(text="Summit White",callback_data='equinox_white')],
    [InlineKeyboardButton(text="THE DRAKE MET-2",callback_data='equinox_drake')],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_9'),InlineKeyboardButton(text="🏠 Бош меню",callback_data="menyu")]
])  

type_tahoe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="TAHOE-2 RST",callback_data="tahoe_2")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_10')]
])

type_lacetti=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="L-OPTIMA AT",callback_data='l_optima_at')],
    [InlineKeyboardButton(text="L-COMFORT PLUS",callback_data='l_comfort')],
    [InlineKeyboardButton(text="L-ELEGENT/AT PLUS",callback_data='l_elegenta')],
    [InlineKeyboardButton(text="L-STYLE MT",callback_data='l_style_mt')],
    [InlineKeyboardButton(text="L-STYLE AT",callback_data='l_style_at')],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_11')]
])


colour_lacetti = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="BLACK MET. KETTLE METALLIC",callback_data="lacetti_black")],
    [InlineKeyboardButton(text="Summit White",callback_data="lacetti_white")],
    [InlineKeyboardButton(text="Light Blue",callback_data="lacetti_blue")],
    [InlineKeyboardButton(text=" Red - E or Not",callback_data="lacetti_red")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_12'),InlineKeyboardButton(text="🏠 Бош меню",callback_data="menyu")]
])


type_tracker = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "TRACKER-2 TRK LS",callback_data="tracker_trk")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_13')]
])

colour_tracker = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="BLACK MET. KETTLE METALLIC",callback_data="tracker_black")],
    [InlineKeyboardButton(text="Summit White",callback_data="tracker_white")],
    [InlineKeyboardButton(text="Red - E or Not",callback_data="tracker_red")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_14'),InlineKeyboardButton(text="🏠 Бош меню",callback_data="menyu")]

])

# orqaga_add= InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_11')]
# ])


orqaga_news= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_news')]
])

#SOTUVDAGI MOSHINALAR QISMI
sotuvdagilar = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=("DAMAS (навбатда 74107 дона)"),callback_data="damas_sotuv")],
    [InlineKeyboardButton(text=("COBALT (навбатда 54939 дона)"),callback_data="cobalt_sotuv")],
    [InlineKeyboardButton(text=("MALIBU-2 (навбатда 16 дона)"),callback_data="malibu_sotuv")],
    [InlineKeyboardButton(text=("EQUINOX (навбатда 18 дона)"),callback_data="equinox_sotuv")],
    [InlineKeyboardButton(text=("TAHOE (навбатда 25 дона)"),callback_data="tahoe_sotuv")],
    [InlineKeyboardButton(text=("LACETTI (навбатда 3314 дона)"),callback_data="lacetti_sotuv")],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_sotuv')]
])

sotuv_damas = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_sotuv_2'),InlineKeyboardButton(text="🏠 Бош меню",callback_data="menyu")]
])

#AVTO INFO QISMI BUTTONLAR
avto_info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="DAMAS",callback_data="damas_info")],
    [InlineKeyboardButton(text="COBALT",callback_data="cobalt_info")],
    [InlineKeyboardButton(text="MALIBU-2",callback_data="malibu_info")],
    [InlineKeyboardButton(text="TAHOE",callback_data='tahoe_info')],
    [InlineKeyboardButton(text="EQUINOX",callback_data="equinox_info")],
    [InlineKeyboardButton(text="TRACKER 2",callback_data='tracker_info')],
    [InlineKeyboardButton(text="⬅️ Орқага",callback_data='orqaga_info')]
])

