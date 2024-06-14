from aiogram import types
from database_func.del_tag_user import del_tags_user
from aiogram.fsm.context import FSMContext
from database_func.get_disabled_tags_user import get_disabled_tags_user


async def del_tag_rout(message: types.Message, state: FSMContext):

    is_or_not_is = await del_tags_user(message)

    tags = await get_disabled_tags_user(message.chat.id)

    if not is_or_not_is:

        await message.answer(f'Successfully, your disabled tags are now: {tags}')

        await state.clear()

    else:

        await message.answer(f'There is no such tag, check the case, your disabled tags are now: {tags}')

        await state.clear()
