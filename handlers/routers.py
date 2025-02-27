from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from handlers.routers_for_all.rout_help import button_to_help_rout
from handlers.routers_for_all.rout_start import start_rout
from handlers.routers_for_admin.add_admin_rout import add_admin_rout
from handlers.routers_for_admin.del_admin_rout import del_admin_rout
from handlers.routers_for_admin.ban_user_rout import ban_user_rout
from handlers.routers_for_admin.unban_user_rout import unban_user_rout
from handlers.routers_for_admin.wait_username_add_admin import (
    get_username_for_add_admin_rout,
)
from handlers.routers_for_admin.wait_username_del_admin import (
    get_username_for_del_admin_rout,
)
from handlers.routers_for_admin.wait_username_ban_user import (
    get_username_for_ban_user_rout,
)
from handlers.routers_for_admin.wait_username_unban_user import (
    get_username_for_unban_user_rout,
)
from handlers.routers_for_admin.get_logs_rout import get_logs_rout
from handlers.routers_for_admin.get_bd_with_admins import get_admin_bd_rout
from handlers.routers_for_admin.get_bd_with_users import get_users_bd_rout
from handlers.routers_for_admin.get_bd_with_ban_users import get_ban_users_bd_rout
from handlers.routers_for_admin.drop_data import drop_data_rout
from handlers.routers_for_all.rout_start import AdminState
from handlers.routers_for_all.rout_config import config_rout
from handlers.callback_query import (
    callback_query_rout_for_is_mailing,
    callback_query_rout_for_disabled_tags,
)
from handlers.callback_query import (
    callback_query_rout_for_add_or_delete_tags,
    WaitDisabledTags,
)
from handlers.routers_for_all.rout_add_tag import add_tag_rout
from handlers.routers_for_all.rout_del_tag import del_tag_rout

router: Router = Router()


@router.message(Command("start"))
async def start_routing(message: types.Message) -> None:
    await start_rout(message)


@router.message(Command("help"))
async def help_routing(message: types.Message) -> None:
    await button_to_help_rout(message)


@router.message(Command("add_admin"))
async def add_admin_routing(message: types.Message, state: FSMContext) -> None:
    await add_admin_rout(message, state)


@router.message(Command("del_admin"))
async def del_admin_routing(message: types.Message, state: FSMContext) -> None:
    await del_admin_rout(message, state)


@router.message(Command("ban_user"))
async def ban_user_routing(message: types.Message, state: FSMContext) -> None:
    await ban_user_rout(message, state)


@router.message(Command("unban_user"))
async def unban_user_routing(message: types.Message, state: FSMContext) -> None:
    await unban_user_rout(message, state)


@router.message(Command("get_logs"))
async def get_logs_routing(message: types.Message) -> None:
    await get_logs_rout(message)


@router.message(Command("get_admins_bd"))
async def get_admin_bd_routing(message: types.Message) -> None:
    await get_admin_bd_rout(message)


@router.message(Command("get_users_bd"))
async def get_users_bd_routing(message: types.Message) -> None:
    await get_users_bd_rout(message)


@router.message(Command("get_ban_users_bd"))
async def get_ban_users_bd_routing(message: types.Message) -> None:
    await get_ban_users_bd_rout(message)


@router.message(Command("config"))
async def config_routing(message: types.Message) -> None:
    await config_rout(message)


@router.message(F.text == "drop data")
async def drop_data_routing(message: types.Message) -> None:
    await drop_data_rout(message)


@router.message(AdminState.waiting_for_add_admin)
async def get_username_for_add_admin(message: types.Message, state: FSMContext) -> None:
    await get_username_for_add_admin_rout(message, state)


@router.message(AdminState.waiting_for_del_admin)
async def get_username_for_del_admin(message: types.Message, state: FSMContext) -> None:
    await get_username_for_del_admin_rout(message, state)


@router.message(AdminState.waiting_for_ban_user)
async def get_username_for_ban_user(message: types.Message, state: FSMContext) -> None:
    await get_username_for_ban_user_rout(message, state)


@router.message(AdminState.waiting_for_unban_user)
async def get_username_for_unban_user(
    message: types.Message, state: FSMContext
) -> None:
    await get_username_for_unban_user_rout(message, state)


@router.callback_query(F.data.startswith("is_mailing"))
async def callback_query_routing_for_is_mailing(
    callback_query: types.CallbackQuery,
) -> None:
    await callback_query_rout_for_is_mailing(callback_query)


@router.callback_query(F.data == "disabled_tags")
async def callback_query_routing_for_disabled_tags(
    callback_query: types.CallbackQuery,
) -> None:
    await callback_query_rout_for_disabled_tags(callback_query)


@router.callback_query(F.data.endswith("tag"))
async def callback_query_routing_for_add_or_delete_tags(
    callback_query: types.CallbackQuery, state: FSMContext
) -> None:
    await callback_query_rout_for_add_or_delete_tags(callback_query, state)


@router.message(WaitDisabledTags.wait_add_tag)
async def add_tag_routing(message: types.Message, state: FSMContext) -> None:
    await add_tag_rout(message, state)


@router.message(WaitDisabledTags.wait_del_tag)
async def del_tag_routing(message: types.Message, state: FSMContext) -> None:
    await del_tag_rout(message, state)


@router.message()
async def unknown_command(message: types.Message) -> None:
    await message.answer("Unknown command, enter /help")
