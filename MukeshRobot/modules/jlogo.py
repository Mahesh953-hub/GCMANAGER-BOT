import random,asyncio,requests,io,os
from pyrogram import filters
from PIL import Image, ImageDraw, ImageFont
from MukeshRobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT,pbot
from pyrogram.enums import ChatAction

LOGO_LINKS = [
    "https://te.legra.ph/file/7345fd37e2ed393b37643.jpg",
    "https://te.legra.ph/file/5ced2c3542ef0662fd6e2.jpg"
    
]


@pbot.on_message(filters.command("jlogo"))
async def jlogo(b,m):
    await b.send_chat_action(m.chat.id, ChatAction.UPLOAD_PHOTO)
    if len(m.command) < 2:
         return await m.reply_text(
            "**Example:**\n\n`/jlogo text`")
    
    pesan = await m.reply("**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ  ʟᴀᴛᴇsᴛ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ​...**")
    try:
        text = m.text.split(' ',1)[1]
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = "./MukeshRobot/resources/fonts/UrbanJungleDEMO.otf"
        randf=fnt
        font = ImageFont.truetype(randf, 120)
        w, h = draw.textsize(text, font=font)
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "mukesh.png"
        img.save(fname, "png")
        await m.reply_photo(
        fname,
            caption=f" ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ @{BOT_USERNAME}"
)
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await m.reply(f" #Error {e}, ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ @{SUPPORT_CHAT}")


__mod_name__ = "Jʟᴏɢᴏ"

__help__ = f"""
@{BOT_USERNAME} ᴄᴀɴ ᴄʀᴇᴀᴛᴇ sᴏᴍᴇ ʙᴇᴀᴜᴛɪғᴜʟ ᴀɴᴅ ᴀᴛᴛʀᴀᴄᴛɪᴠᴇ ᴊᴜɴɢʟᴇ ʟᴏɢᴏ ғᴏʀ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘɪᴄs.


❍ /jlogo (Text) *:* ᴄʀᴇᴀᴛᴇ ᴀ ʟᴏɢᴏ ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ᴠɪᴇᴡ.


[𓆩｡</𝙌> ｡𓆪 ] (f"tg://user?id={OWNER_ID}")

"""
