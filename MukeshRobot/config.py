
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "" # integer value, dont use ""
    API_HASH = ""
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6560999758 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "SUpp0rT_GC_BoT"  # Your own group for support, do not add the @
    START_IMG = ""
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://LAZYYY:hnTnX7ancmXh7weQ@cluster0.td3nu69.mongodb.net/"
    # RECOMMENDED
    DATABASE_URL = "postgres://ogftbmez:Op1T1dOoD1FM_xe7aBZzEHAPZqqwM_C0@rosie.db.elephantsql.com/ogftbmez"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "D0ZCZ67KL8OTL0PY"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5LB4TAKPEKZ0"  # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [6560999758]  # User id of sudo users
    DEV_USERS = [6560999758]  # User id of dev users
    DEMONS = [6560999758]  # User id of support users
    TIGERS = [6560999758]  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True