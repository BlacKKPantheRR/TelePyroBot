"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
from pyrogram import Client, Filters
from pyrobot.__main__ import get_runtime
from pyrobot import COMMAND_HAND_LER, PyroBotCMD
from pyrobot.helper_functions.cust_p_filters import sudo_filter

# -- Constants -- #
ALIVE = "`I'm Alive :3`"
HELP = "CAADAgAD6AkAAowucAABsFGHedLEzeUWBA"
REPO = ("User / Bot is available on GitHub:\n"
        "https://github.com/SkuzzyxD/TelePyroBot")
# -- Constants End -- #


@PyroBotCMD.on_message(Filters.command(["alive", "start"], COMMAND_HAND_LER) & sudo_filter)
async def check_alive(_, message):
    a = await get_runtime()
    b = int(time.time())
    c = b - a
    month = c // 2678400
    days = c // 86400
    hours = c // 3600 % 24
    minutes = c // 60 % 60
    seconds = c % 60

    alivetext = ""
    if month:
        alivetext += "{} month, ".format(month)
    if days:
        alivetext += "{} days, ".format(days)
    if hours:
        alivetext += "{} hours, ".format(hours)
    if minutes:
        alivetext += "{} minutes, ".format(minutes)
    if seconds:
        alivetext += "{} seconds".format(seconds)

    TIME_ALIVE= f"\nBot was alive for `{alivetext}`"
    text = ALIVE + TIME_ALIVE
    await message.reply_text(text, parse_mode="md")


@PyroBotCMD.on_message(Filters.command("help", COMMAND_HAND_LER) & sudo_filter)
async def help_me(_, message):
    await message.reply_sticker(HELP)


@PyroBotCMD.on_message(Filters.command("ping", COMMAND_HAND_LER) & sudo_filter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pinging...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n`{time_taken_s:.3f}` ms", parse_mode="md")


@PyroBotCMD.on_message(Filters.command("repo", COMMAND_HAND_LER) & sudo_filter)
async def repo(_, message):
    await message.reply_text(REPO)
