from aiogram import types
from database_func.add_tags_user import update_tags_user
from aiogram.fsm.context import FSMContext
from database_func.get_disabled_tags_user import get_disabled_tags_user


async def add_tag_rout(message: types.Message, state: FSMContext):

    await update_tags_user(message)

    tags = await get_disabled_tags_user(message.chat.id)

    await message.answer(f'Successfully, your disabled tags are now: {tags}')

    await state.clear()
