# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8709203843:AAEVufb25C8VVpgn4R-BqbXi157KrrxKzfQ")
APP_ID = int(os.environ.get("APP_ID", "33964882")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2b618df1eb69c19f08052490e0f9ee68") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003816675784")) #Your db channel Id
OWNER = os.environ.get("OWNER", "sewxiy") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "6908351235")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://20duddududdu1:20duddududdu1@cluster0.tq6n3ix.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "100"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/Cineplex_support_bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://t.me/ajkajauauiw/3")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://t.me/ajkajauauiw/3")
#--------------------------------------------
#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "softurl.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "65676573da083f670527098369bf4417fae2b457")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","https://t.me/howto_openlink/6")
#--------------------------------------------
HELP_TXT = "<b>ನಾನು  ಮೂವಿ ಕಳಿಸುವ Bot!\n\nನಿಮಗೆ ಯಾವುದೇ ಸಮಸ್ಯೆ ಇದ್ದರೆ ಸಂಪರ್ಕಿಸಿ | if you have any problem contact @Cineplex_support_bot</b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: @Cineplex_support_bot </blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\nನಾನು  ಮೂವಿ ಕಳಿಸುವ Bot!\nನೀವು ಇನ್ಸ್ಟಾಗ್ರಾಂನಲ್ಲಿ ನೋಡಿದ ಮೂವಿ ನಂಬರ್ ಕಳುಹಿಸಿ, ಮೂವಿ ತಕ್ಷಣ ಪಡೆಯಿರಿ 📩🎥\n\nI’m a movie bot!\nSend the movie number from Instagram and get it instantly</b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b>ಕೆಳಗಿರುವ 👇 ನಮ್ಮ ಚಾನೆಲ್‌ಗಳಿಗೆ ಸೇರಿ ನಂತರ ನೀವು ಇನ್ಸ್ಟಾಗ್ರಾಂನಲ್ಲಿ ನೋಡಿದ ಮೂವಿ ನಂಬರ್ ಕಳುಹಿಸಿ, ತಕ್ಷಣ ಮೂವಿ ಫೈಲ್ ಅನ್ನು  ಪಡೆಯಿರಿ\n\n<blockquote>Join our channels below 👇 then send the movie number you saw on Instagram, get the movie file instantly</b></blockquote>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /broadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
<b>›› /setfile :</b> store a single file or media group under a key
<b>›› /setfiles :</b> collect multiple files for a duration (default 60s)
<b>›› /listfile :</b> check all files
<b>›› /delfile :</b> Rᴇᴍᴏᴠᴇᴅ files
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b> </b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "Cineplex_support_bot")
UPI_ID = os.environ.get("UPI_ID", "Premium ತಾತ್ಕಾಲಿಕವಾಗಿ ಲಭ್ಯವಿಲ್ಲ")
QR_PIC = os.environ.get("QR_PIC", "https://telegra.ph/file/3e83c69804826b3cba066-16cffa90cd682570da.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"https://t.me/Cineplex_support_bot")
#--------------------------------------------
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "0 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "60 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "150 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "280 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "550 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
