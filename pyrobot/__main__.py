from pyrobot import PyroBotCMD

async def start_bot():
    await PyroBotCMD.start()

if __name__ == '__main__':
    LOGGER.info(f"TelePyroBot based on Pyrogram started Successfully! Hello User.")
    start_bot()
