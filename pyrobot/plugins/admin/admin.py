import asyncio
from pyrogram import Client, Filters
from pyrobot import COMMAND_HAND_LER, PyroBotCMD
from pyrobot.helper_functions.cust_p_filters import sudo_filter
from pyrobot.helper_functions.extract_user import extract_user
from pyrobot.helper_functions.admin_check import admin_check

@PyroBotCMD.on_message(Filters.command("promote", COMMAND_HAND_LER) & sudo_filter)
async def promote_usr(client, message):
    rm = await message.reply_text("`Trying to Promote User.. Hang on!! ⏳`", parse_mode="md")
    is_admin = await admin_check(message)

    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)
    chat_id = message.chat.id
    if user_id and chat_id:
        try:
            await client.promote_chat_member(chat_id, user_id,
                                            can_change_info=False,
                                            can_delete_messages=True,
                                            can_restrict_members=True,
                                            can_invite_users=True,
                                            can_pin_messages=True)
            await asyncio.sleep(2)
            await rm.edit(f"`👑 Promoted` [{user_first_name}](tg://user?id={user_id}) `Successfully...`", parse_mode="md")
        except Exception as ef:
            await rm.edit(
                text="`something went wrong`\n\n"
                f"**ERROR:** `{ef}`", parse_mode="md")


@PyroBotCMD.on_message(Filters.command("demote", COMMAND_HAND_LER) & sudo_filter)
async def demote_usr(client, message):
    rm = await message.reply_text("`Trying to Demote User.. Hang on!! ⏳`", parse_mode="md")
    is_admin = await admin_check(message)

    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)
    chat_id = message.chat.i

    if user_id and chat_id:
        try:
            await client.promote_chat_member(chat_id, user_id,
                                            can_change_info=False,
                                            can_delete_messages=False,
                                            can_restrict_members=False,
                                            can_invite_users=False,
                                            can_pin_messages=False)
            await asyncio.sleep(2)
            await rm.edit(f"`Demoted` [{user_first_name}](tg://user?id={user_id}) `Successfully...`", parse_mode="md")
        except Exception as ef:
            await rm.edit(
                text="`something went wrong`\n\n"
                f"**ERROR:** `{ef}`", parse_mode="md")
