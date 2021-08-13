from decouple import config
from pastebin import PastebinAPI, PastebinError
from telethon import Button, TelegramClient, events


class ENV:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e", cast=str)
    BOT_TOKEN = config("BOT_TOKEN", cast=str)
    PASTEBIN_API_KEY = config("PASTEBIN_API_KEY", cast=str)
    PRIVATE_PASTE = config("PRIVATE_PASTE", default="NO", cast=str)
    PASTE_EXPIRY = config("PASTE_EXPIRY", default="1D", cast=str)


try:
    Client = TelegramClient(None, api_id=ENV.API_ID, api_hash=ENV.API_HASH).start(
        bot_token=ENV.BOT_TOKEN
    )
except Exception as ex:
    print(str(type(ex)) + ": " + str(ex))
    exit()


def paste_it(paste_code, paste_name=None, paste_format=None):
    private_paste = ENV.PRIVATE_PASTE.upper() if ENV.PRIVATE_PASTE else None
    paste_expiry = ENV.PASTE_EXPIRY.upper() if ENV.PASTE_EXPIRY else None
    if private_paste:
        if private_paste == "YES":
            paste_private = "private"
        elif private_paste == "NO":
            paste_private = "public"
        else:
            paste_private = None
    if paste_expiry not in ["N", "10M", "1H", "1D", "1M"]:
        paste_expiry = None
    return PastebinAPI().paste(
        api_dev_key=ENV.PASTEBIN_API_KEY,
        api_paste_code=paste_code,
        paste_name=paste_name,
        paste_format=paste_format,
        paste_private=paste_private,
        paste_expire_date=paste_expiry,
    )


@Client.on(
    events.NewMessage(
        pattern="/start$",
        func=lambda e: e.is_private and not e.fwd_from and not e.via_bot_id,
    ),
)
async def starter(event):
    await event.reply(
        "**Welcome to PasteBin-Bot.**\n\n"
        + "**How to use?**\n"
        + "Send me readable file or some message and reply `/paste` to it and I will paste it on PasteBin.com\n\n"
        + "**Extras:-**\n"
        + "** • For custom name:** `/paste name`.\n"
        + "** • For custom name and highlights:** `/paste name format`.\n"
        + "** • For highlights:** `/paste None format`.",
        buttons=[
            [
                Button.url("Creator", url="t.me/buddhhu"),
                Button.url("Source", url="https://t.me/Botsrealm/13"),
            ],
            [Button.url("Formats", url="https://telegra.ph/Highlights-08-04")],
        ],
        link_preview=False,
    )


@Client.on(
    events.NewMessage(
        pattern="^/paste ?(.*)",
        func=lambda e: e.is_private,
    ),
)
async def dustbin(event):
    input = event.pattern_match.group(1)
    paste_name = None
    paste_format = None
    replied_msg = await event.get_reply_message()
    if not replied_msg:
        return await event.reply("Reply to some message/readable file.")
    if input:
        try:
            data = input.split()
            paste_name = data[0]
            paste_format = data[1]
        except IndexError:
            pass
    if paste_name == "None":
        paste_name = None
    msg = await replied_msg.reply("**Pasting on PasteBin...**")
    if replied_msg.document:
        if replied_msg.file.size > 500*1024:
            return await msg.edit("Maximum file size should be **500KB**")
        file = await replied_msg.download_media()
        try:
            with open(file, "r") as file_content:
                paste_code = file_content.read()
        except BaseException:
            return await msg.edit("I'm not able to read that file :(")
    else:
        paste_code = replied_msg.text
    try:
        url = paste_it(paste_code, paste_name, paste_format)
    except PastebinError:
        return await msg.edit("Something went wrong :(")
    await msg.edit(url, link_preview=False)


print("~" * 15 + " Bot Started " + "~" * 15)
Client.run_until_disconnected()
