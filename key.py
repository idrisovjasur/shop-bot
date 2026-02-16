from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='☎️ Phone', request_contact=True)],
    ],
    resize_keyboard=True
)


computer_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Computer')]
    ], resize_keyboard=True

)

def inline_key(a):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='-', callback_data='-'),
             InlineKeyboardButton(text=f"{a}", callback_data=f"{a}"),
             InlineKeyboardButton(text=f"+", callback_data='+'),],
            [InlineKeyboardButton(text='Buy', callback_data='buy'),]
        ],

    )
    return keyboard


computer_caption = """
Экран
Размер
16 дюймов
Соотношение сторон
16:10
Разрешение
1920 × 1200, 142 ppi
Максимальная яркость
300 нит
"""