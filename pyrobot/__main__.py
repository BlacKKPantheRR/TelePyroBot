from pyrobot import PyroBotCMD
import asyncio

loop = asyncio.get_event_loop()

async def start_bot():
    await PyroBotCMD.start()

if __name__ == '__main__':
    LOGGER.info(f"TelePyroBot based on Pyrogram started Successfully! Hello User.")
    loop.run_until_complete(start_bot())
