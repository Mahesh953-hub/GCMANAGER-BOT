import requests
from telegram import Update
from telegram.ext import CallbackContext

from MukeshRobot import dispatcher
from MukeshRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    truth = requests.get(f"https://api.truthordarebot.xyz/v1/truth").json()["question"]
    update.effective_message.reply_text(truth)


def dare(update: Update, context: CallbackContext):
    dare = requests.get(f"https://api.truthordarebot.xyz/v1/dare").json()["question"]
    update.effective_message.reply_text(dare)
#def wyr(update: Update, context: CallbackContext):
#    truth = requests.get(f"https://api.truthordarebot.xyz/v1/wyr").json()["question"]
#    update.effective_message.reply_text(wyr)

#def nhie(update: Update, context: CallbackContext):
#    truth = requests.get(f"https://api.truthordarebot.xyz/v1/nhie").json()["question"]
#    update.effective_message.reply_text(nhie)
#def paranoia(update: Update, context: CallbackContext):
#    truth = requests.get(f"https://api.truthordarebot.xyz/v1/paranoia").json()["question"]
#    update.effective_message.reply_text(paranoia)

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)
#WYR_HANDLER = DisableAbleCommandHandler("wyr", wyr, run_async=True)
#NHIE_HANDLER = DisableAbleCommandHandler("nhie", nhie, run_async=True)
#PARANIOA_HANDLER = DisableAbleCommandHandler("paranoia", paranoia, run_async=True)
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
#dispatcher.add_handler(WYR_HANDLER)

#dispatcher.add_handler(NHIE_HANDLER)
#dispatcher.add_handler(PARANIOA_HANDLER)


__help__ = """
*ᴛʀᴜᴛʜ & ᴅᴀʀᴇ*
 ❍ /truth  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
 ❍ /dare  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.

[𓆩｡</𝙌> ｡𓆪 ] (f"tg://user?id={OWNER_ID}")
"""
__mod_name__ = "ᴛ-ᴅ"
