from aiogram import types
from handlers.routers_for_all.rout_start import AdminState
from aiogram.fsm.context import FSMContext
from handlers.routers_for_all.rout_start import creator_id


async def add_admin_rout(message: types.Message, state: FSMContext) -> None:
    user_id: int = message.from_user.id

    if user_id != creator_id:
        await message.answer("Unknown command, enter /help")

    else:
        await message.answer("Enter a username")

        await state.set_state(AdminState.waiting_for_add_admin)

    return
