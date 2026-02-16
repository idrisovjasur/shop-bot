from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import logging
import asyncio
from key import phone_keyboard, computer_keyboard, computer_caption, inline_key
from data import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
###
class RegisterStates(StatesGroup):
    name = State()
    phone = State()
    computer = State()

# @dp.message()
# async def debug(message: Message):
#     print("CHAT_ID:", message.chat.id)
#     print("TYPE:", message.chat.type)


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await message.answer(
        'Input Your Name: '
    )
    await state.set_state(RegisterStates.name)

@router.message(RegisterStates.name)
async def register_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data({
        'name': name
    })
    await message.answer(
        'Send Your Phone Number: ', reply_markup=phone_keyboard
    )
    await state.set_state(RegisterStates.phone)

@router.message(RegisterStates.phone)
async def register_phone(message: Message, state: FSMContext):
    if message.text:
        await message.answer('Knopkani bos mashinik!!')
    else:
        phone = message.contact.phone_number
        await state.update_data({
            'phone': phone
        })
        await message.answer(
            'Choose Th Product', reply_markup=computer_keyboard
        )
        await state.set_state(RegisterStates.computer)

@router.message(RegisterStates.computer)
async def register_computer(message: Message, state: FSMContext):
    photo = 'AgACAgIAAxkBAAMaaY6vBqA3SYIKdr67HBixb3g5iQgAAq0QaxvvRHhIvhtJbKu1yZ0BAAMCAAN4AAM6BA'
    await message.answer_photo(
        photo=photo,caption=computer_caption, reply_markup=inline_key(1)
    )
    await state.update_data(a = 1)
    await state.set_state(RegisterStates.computer)

@router.callback_query(RegisterStates.computer)
async def callback_computer_register(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    a = int(data.get('a'))
    if call.data == '+':
        a+=1
        await state.update_data(a = a)
        await call.message.edit_reply_markup(reply_markup=inline_key(a))
    elif call.data == '-' and a > 1:
        a-=1
        await state.update_data(a=a)
        await call.message.edit_reply_markup(reply_markup=inline_key(a))
    elif call.data == '-' and a <= 1:
        await call.answer(text='Error', show_alert=True)
    elif call.data == 'buy':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        computer = data.get('a')
        await call.message.answer(
            'Buyurtma qabul qilindi!'
        )
        text = f"""
            Name: {name}
            Phone: {phone}
            Computer: {computer} ta
        """
        group_id = -1003836403035
        await bot.send_message(
            group_id,text=text
        )
    await call.answer()
    await state.set_state(RegisterStates.computer)




async def main():
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())




