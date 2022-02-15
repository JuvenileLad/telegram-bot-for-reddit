from pyrogram import filters
from pyrogram.types.bots_and_keyboards import callback_query
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
import time, asyncio, tzlocal
from .utils.db_handler import wholeDB, subDB, list_db, update_channel
from .utils.reddit_handler import *
from .client import bot, DELAY, BOTOWNER
from apscheduler.schedulers.asyncio import AsyncIOScheduler

@bot.on_message(filters.command("start"))
async def start(_, message):
    text = f"A Telegram bot for getting new submission from subreddits.\nMade By: @{BOTOWNER}"
    btn = [[InlineKeyboardButton("help", callback_data="help"),InlineKeyboardButton("Source 🚀", url="https://github.com/JuvenileLad/telegram-bot-for-reddit")]]
    await bot.send_message(message.chat.id, text, disable_web_page_preview = True, reply_markup = InlineKeyboardMarkup(btn))

@bot.on_callback_query("help")
@bot.on_message(filters.command("help")) # needs to change
async def help(_, cb: callback_query):
    text = "To get started, use the following commands:\n\n"
    text += "`/add subreddit_name` - to add a new subreddit\n\n"
    text += "`/rm subreddit_name` - to remove a subreddit\n\n"
    text += "`/channel channel_ID` - to change the default channel.\n\n"
    text += "/list - to get a list of all the subreddits\n\n"
    text += "/ping - to check ping\n\n"
    text += "/id - to get channel ID. Use this command in the channel.\n\n"
    await bot.send_message(cb.chat.id, text, disable_web_page_preview = True)

@bot.on_message(filters.command("ping"))
async def ping(_, message):
    start = time.time() 
    p = await message.reply_text("Pong!")
    end = time.time()
    await p.edit_text(f"Pong!\n__{round((end-start)*1000)}ms__") # round to nearest millisecond    
    await asyncio.sleep(5)
    await message.delete()
    await p.delete()

@bot.on_message(filters.command("add"))
async def add(_, message):
    user_id = message.from_user.id # user id
    m = message_formatter(message)
    subreddit = await Check_sub(m)
    if subreddit:
        feed = subDB(user_id, subreddit)
        sub_dict = await get_data(subreddit, ['id'])
        text = feed.add_sub(subreddit, sub_dict)
        await message.reply_text(text, disable_web_page_preview = True)
    else:
        await message.reply_text("Invalid subreddit!")

@bot.on_message(filters.command("rm"))
async def remove(_, message):
    user_id = message.from_user.id # user id
    m = message_formatter(message)

    subreddit = await Check_sub(m)
    if subreddit: # if valid subreddit
        feed = subDB(user_id, subreddit)
        text = feed.remove_sub(subreddit)
        await message.reply_text(text)

@bot.on_message(filters.command("list"))
async def list(_, message):
    user_id = message.from_user.id # user id
    try:
        subs_list = list_db(user_id)
        text = f"{subs_list[0]}\nTotal: {subs_list[1]}"
    except:
        text = "No subreddits added yet!"
    await message.reply_text(text)

@bot.on_message(filters.command("channel"))
async def change_channel(_, message):
    user_id = message.from_user.id # user id
    m = message_formatter(message)
    reply = update_channel(user_id, m)
    await message.reply_text(reply)

@bot.on_message(filters.command("id"))
async def channel_id(_, message):
    id = message.chat.id
    await message.reply_text(f"Your channel ID is: {id}")

async def updater():
    print('Started Updating')
    subs_list = wholeDB()
    await update_subs(subs_list)

scheduler = AsyncIOScheduler(timezone=str(tzlocal.get_localzone()))
scheduler.add_job(updater, "interval", seconds=DELAY)
scheduler.start()

def message_formatter(message):
    m = message.text.split(" ")
    m.pop(0)
    m = " ".join(m)
    return m
