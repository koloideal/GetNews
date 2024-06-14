from aiogram import types
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database_func.get_send_users import get_send_users
from database_func.send_user_to_database import send_user_to_database


async def config_rout(message: types.Message) -> None:

    await send_user_to_database(message)

    send_users_data = await get_send_users()
    send_users_id = [int(x['id']) for x in send_users_data]

    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    if message.chat.id in send_users_id:

        builder.add(InlineKeyboardButton(text='Disabled Tags', callback_data='disabled_tags'),
                    InlineKeyboardButton(text='Mailing:  ON ✅', callback_data='is_mailing_ON'))

    else:

        builder.add(InlineKeyboardButton(text='Disabled Tags', callback_data='disabled_tags'),
                    InlineKeyboardButton(text='Mailing:  OFF ❌', callback_data='is_mailing_OFF'))

    await message.answer('Here you can manage mailing lists and disabled tags', reply_markup=builder.as_markup())
