from aiogram.types import Message


async def button_to_help_rout(message: Message) -> None:
    await message.answer(
        "<b><i>When the news is published on the ixbt portal, "
        "I will send you a short announcement and a link to this news</i></b>\n\n"
        "<b>You can configure the bot using the command /configure</b>\n\n"
        "<i><u>You can choose tags that will not be sent to you with news\n\n"
        "You can also unsubscribe from the mailing list</u></i>",
        parse_mode="HTML",
    )
