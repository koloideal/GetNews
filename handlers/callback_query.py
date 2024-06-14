from aiogram import types
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database_func.add_send_user import add_send_user
from database_func.del_send_user import del_send_user
from database_func.get_disabled_tags_user import get_disabled_tags_user
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database_func.del_all_tags import del_all_tags_user


class WaitDisabledTags(StatesGroup):

    wait_add_tag = State()
    wait_del_tag = State()


async def callback_query_rout_for_is_mailing(callback: types.CallbackQuery):
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    match callback.data:

        case 'is_mailing_OFF':

            await add_send_user(callback.message)

            builder.add(InlineKeyboardButton(text='Disabled Tags', callback_data='disabled_tags'),
                        InlineKeyboardButton(text='Mailing:  ON ✅', callback_data='is_mailing_ON'))

            await callback.message.edit_reply_markup(reply_markup=builder.as_markup())

        case 'is_mailing_ON':

            await del_send_user(callback.message)

            builder.add(InlineKeyboardButton(text='Disabled Tags', callback_data='disabled_tags'),
                        InlineKeyboardButton(text='Mailing:  OFF ❌', callback_data='is_mailing_OFF'))

            await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


async def callback_query_rout_for_disabled_tags(callback: types.CallbackQuery):

    disabled_tags = await get_disabled_tags_user(callback.message.chat.id)

    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text='Add Tag/Tags', callback_data='add_tag'),
                InlineKeyboardButton(text='Delete Tag', callback_data='delete_tag'),
                InlineKeyboardButton(text='Delete All Tags', callback_data='delete_all_tag'))

    text = f'Your disabled tag(s): {disabled_tags if disabled_tags else 'No Such'}'

    await callback.message.answer(text=text, reply_markup=builder.as_markup())


async def callback_query_rout_for_add_or_delete_tags(callback: types.CallbackQuery, state: FSMContext):

    action = callback.data

    match action:

        case 'add_tag':

            await callback.message.answer('Enter the tag without quotes in the "example" format if there is one, '
                                          'if you want to add several tags, then enter them without quotes in the '
                                          '"example1 example2 example3" format')

            await state.set_state(WaitDisabledTags.wait_add_tag)

        case 'delete_tag':

            tags = await get_disabled_tags_user(callback.message.chat.id)

            await callback.message.answer('Enter the disabled tag to delete without quotes, now your disabled tags are:'
                                          f' {tags}')

            await state.set_state(WaitDisabledTags.wait_del_tag)

        case 'delete_all_tag':

            await del_all_tags_user(callback.message)

            await callback.message.answer('All disabled tags have been successfully deleted')
