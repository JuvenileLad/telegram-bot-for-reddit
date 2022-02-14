import configparser, asyncpraw, pymongo
from pyrogram import Client

config = configparser.ConfigParser()
config.read('config.ini')

SESSION = config['pyrogram']['session_name']
API_HASH = config['pyrogram']['api_hash']
API_ID = config['pyrogram']['api_id']
BOT_TOKEN = config['pyrogram']['bot_token']
BOTOWNER = config['pyrogram']['bot_owner']
OWNERURL = f"https://t.me/{BOTOWNER}"

CLIENT_ID = config['reddit']['client_id']
SECRET = config['reddit']['secret']

MONGODB = config['CONFIG']['url']

USERAGENT = f"{config['pyrogram']['bot_name']}/{config['pyrogram']['bot_version']}:by /u/{config['reddit']['reddit_username']}"
DELAY = int(config['CONFIG']['delay'])
LIMITPERUSER = int(config['CONFIG']['limitperuser'])
MAXUSERS = int(config['CONFIG']['maxusers'])
USEREXCEPTION = [int(i) for i in config['CONFIG']['userException'].split()]


client = pymongo.MongoClient(host=MONGODB)
mydb = client["RedditDB"]
myColl = mydb["UserCollection"]

reddit = asyncpraw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET,
    user_agent= {USERAGENT})

bot = Client(
	SESSION,
	bot_token= BOT_TOKEN,
	api_hash= API_HASH,
	api_id= API_ID)

