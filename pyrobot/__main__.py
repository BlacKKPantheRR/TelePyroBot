from pyrobot import app, LOGGER
import asyncio
import time

loop = asyncio.get_event_loop()
BOT_RUNTIME = 0

async def get_runtime():
    return BOT_RUNTIME

async def start_bot():
    await app.start()

if __name__ == '__main__':
    BOT_RUNTIME = int(time.time())
    LOGGER.info("TelePyroBot based on Pyrogram started Successfully! Hello User.")
    app.run()
    #loop.run_until_complete(start_bot())
