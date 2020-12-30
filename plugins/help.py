from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url
 For any other help contact with admin  @aftabuddin_ahmed "
    await message.reply_text(helptxt)
