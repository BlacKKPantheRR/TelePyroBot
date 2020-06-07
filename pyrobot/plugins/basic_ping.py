"""Basic Commands"""

import time
import os
from pyrogram import Client, Filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.utils.cust_p_filters import sudo_filter
from pyrobot.utils.extract_user import extract_user

# -- Constants -- #
ALIVE = "`I'm Alive :3`"
HELP = "CAADAgAD6AkAAowucAABsFGHedLEzeUWBA"
REPO = ("User / Bot is available on GitHub:\n"
        "https://github.com/SkuzzyxD/TelePyroBot")
# -- Constants End -- #


@Client.on_message(Filters.command(["alive", "start"], COMMAND_HAND_LER) & sudo_filter)
async def check_alive(client, message):
    try:
        await message.edit_text(ALIVE)
    except:
        await message.reply_text(ALIVE)


@Client.on_message(Filters.command("help", COMMAND_HAND_LER) & sudo_filter)
async def help_me(client, message):
    await message.reply_sticker(HELP)


@Client.on_message(Filters.command("ping", COMMAND_HAND_LER) & sudo_filter)
async def ping(client, message):
    start_t = time.time()
    try:
        rm = await message.edit("Pinging...")
    except:
        rm = await message.reply_text("Pinging...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n`{time_taken_s:.3f}` ms")


@Client.on_message(Filters.command("repo", COMMAND_HAND_LER) & sudo_filter)
async def repo(client, message):
    try:
        await message.edit(REPO)
    except:
        await message.reply_text(REPO)

@Client.on_message(Filters.command("id", COMMAND_HAND_LER) & sudo_filter)
async def get_id(client, message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message
        if rep.audio:
            file_id = rep.audio.file_id
        elif rep.document:
            file_id = rep.document.file_id
        elif rep.photo:
            file_id = rep.photo.file_id
        elif rep.sticker:
            file_id = rep.sticker.file_id
        elif rep.video:
            file_id = rep.video.file_id
        elif rep.animation:
            file_id = rep.animation.file_id
        elif rep.voice:
            file_id = rep.voice.file_id
        elif rep.video_note:
            file_id = rep.video_note.file_id
        elif rep.contact:
            file_id = rep.contact.file_id
        elif rep.location:
            file_id = rep.location.file_id
        elif rep.venue:
            file_id = rep.venue.file_id
        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        try:
            await message.edit("This User's ID: `{}`".format(user_id))
        except:
            await message.reply_text("This User's ID: `{}`".format(user_id))
    elif file_id:
        try:
            await message.edit("This File's ID: `{}`".format(file_id))
        except:
            await message.reply_text("This File's ID: `{}`".format(file_id))
    else:
        try:
            await message.edit("This Chat's ID:\n`{}`".format(message.chat.id))
        except:
            await message.reply_text("This Chat's ID:\n`{}`".format(message.chat.id))


@Client.on_message(Filters.command(["whois", "info"], COMMAND_HAND_LER) & sudo_filter)
async def who_is(client, message):
    """ extract user information """
    status_message = await message.reply_text(
        "Finding user...."
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        user_id = from_user_id
        if not str(user_id).startswith("@"):
            user_id = int(user_id)
        from_user = await client.get_users(user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        await status_message.edit("No valid user_id / message specified")
    else:
        msg = ""
        msg += f"ID: <code>{from_user.id}</code>\n"
        msg += f"First Name: <a href='tg://user?id={from_user.id}'>"
        msg += from_user.first_name
        msg += "</a>\n"
        msg += f"Last Name: {from_user.last_name}\n"
        msg += f"DC ID: <code>{from_user.dc_id}</code>\n"
        await message.reply_text(
                text=msg,
                quote=True,
                parse_mode="html",
                disable_notification=True)
        await status_message.delete()


@Client.on_message(Filters.command("json", COMMAND_HAND_LER) & sudo_filter)
async def jsonify(client, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message

    try:
        await message.reply_text(f"<code>{the_real_message}</code>")
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("json.text")