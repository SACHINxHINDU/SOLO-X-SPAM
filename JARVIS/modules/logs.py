import asyncio
import heroku3
from pymongo import MongoClient
from config import X1, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError



# Logs command handler
@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(ANNIE):
    if ANNIE.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await ANNIE.reply(
                "First Set These Vars In Heroku: `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await ANNIE.reply(
                "Make Sure Your Heroku API Key & App Name Are Configured Correctly In Heroku."
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await ANNIE.reply(f"__Fetching Logs...__")

        with open("JARVISlogs.txt", "w") as logfile:
            logfile.write("⚡ JARVISBOTS ⚡ [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end - start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(ANNIE.chat_id, "JARVISlogs.txt", caption=f"⚡ **JARVIS BOTS LOGS** ⚡\n  » **Time Taken:** `{ms} seconds`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"An Exception Occurred!\n\n**ERROR:** {str(e)}")

    elif ANNIE.sender_id in SUDO_USERS:
        await ANNIE.reply("» BSDK..ISKO SIRF OWNER USE KR SKTA HAI...")
