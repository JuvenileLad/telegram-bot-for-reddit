# Telegram Bot for Reddit
**A Telegram bot for getting new submission from subreddits.**


Made using <a href='https://docs.pyrogram.org'>pyrogram</a>, this bot can store subreddits that the user wants and can upload new submissions in that subreddit to the user's PM or in the channel specified by the user. This bot can make surfing Reddit easier for those who are more active on Telegram.
###### Uses the following python libraries: 
- [pyrogram (Telegram)](https://github.com/pyrogram/pyrogram)
- [pymongo (MongoDB)](https://pymongo.readthedocs.io/en/stable/)
- [asyncpraw (Reddit)](https://asyncpraw.readthedocs.io/en/stable/)
- [apscheduler](https://apscheduler.readthedocs.io/en/3.x/)

```
➤ KANG AT YOUR OWN RISK: Your Telegram/Reddit account may get in case of API abuse.
➤ I AM NOT RESPONSIBLE IF YOUR ACCOUNT GETS BANNED.
➤ I AM NOT RESPONSIBLE FOR ANY IMPROPER USE OF THIS BOT.
```


#### Table of contents :
<ol>
	<li> <a href="#features">FEATURES</a>
	<li> <a href="#install">INSTALLATION</a>
		<ol>
			<li> <a href="#preq">PREQUISITES</a><li> <a href="#config">CONFIGURATION</a>
		</ol>
	<li> <a href="#issues">ISSUES</a>
	<li> <a href="#contribute">CONTRIBUTE</a>
</ol>

## <div id="features">FEATURES & USAGE</div>
##### Following are the features:
- Get Image as well as Text submission from subreddits.
- Choose a custom channel for uploading new submissions.
- Limit the number of users that can use the bot.
- Limit the number of subreddits a user can add.
- Add users as Admins which will not have any limitations on number of subreddits.

##### Following are the commands and their usage:
- `/start`: to start the bot and receive a start message.
- `/help`: to get the help message.
- `/ping`: to check ping.
- `/add Python` : add a subreddit using the `/add` command and replace `Python` with the exact username of the subreddit, without `r/`.
- `/list`: view all the added subreddits as a list.
- `/rm Python`: remove a subreddit using the `/rm` command followed by name of the subreddit.
- `channel -100112381`: change the channel where the bot uploads new submissions. Defaults to the user's PM.<br>
- `/id`: to be used in a channel to get the channel ID.

**IMPORTANT:**
*Do this before using the channel command.Following these steps is important even if you already have the channel ID:*<br>➤ Add the bot in the channel.<br>➤ Make the bot admin.<br>➤ Use the `/id` command in the channel to get the channel's ID.
*(This is so that the bot can interact with the channel*)


## <div id="install">INSTALLATION</div>

### <div id="preq">Prequisites</div>
*Clone the repository*
```
git clone https://github.com/JuvenileLad/telegram-reddit-bot.git && cd telegram-reddit-bot
```
*Install the required python libraries*
```
pip3 install -U -r requirements.txt
```

*Obtain all the required API keys*

1) Telegram
	- Go to https://my.telegram.org/auth
	- Follow [this](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) guide to obtain Telegram API hash & API key
	- Obtain the bot token from https://t.me/BotFather
	<BR>
2) Reddit
	- Make sure to go through [this](https://www.reddit.com/wiki/api)
	- [Make a reddit app](https://old.reddit.com/prefs/apps/)
		- choose `script` as application type
		- write link to you telegram account in redirect uri.
	- [Read the terms and register](https://docs.google.com/a/reddit.com/forms/d/1ao_gme8e_xfZ41q4QymFqg5HD29HggOD8I9-MFTG7So/viewform)
	<br>
3) MongoDB
	- Follow [this guide](https://telegra.ph/How-to-get-MongoDB-URL-02-04)
	<br>
	
### <div id="config">Configuration</div>
*do not add quotes(" ") symbol in any value*
	
- in `session_name` enter whatever you want as session name in telegram
- in `bot_name` enter the username of the telegram bot.
- enter the MongoDB URL in `url`. Can also be set to localhost.
- set `delay` as the number of seconds to wait between checking for new submissions
- `maxusers` is the max number of users that will be able to use the bot
-  `limitPerUser` is max number of subreddits that a user will be able to add
-  `userException` are telegram user IDs which will granted exception from `limitPerUser`. Each value has to be separated by a space.
- most other variables are self explanatory
- the `config.ini` file already consists of sample values, you just have to replace them.

#### Now run the bot by using:
	python3 -m pyrogramReddit


## <div id="contribute">CONTRIBUTE</div>
I am a beginner programmer and still unaware of the best possible programming conventions that could be used to improve the code. I've tried my best to point out potential performance/aesthetic issues with the code but I would appreciate advice that could help improve the program.
So if you have any advice or recommendation that could help improve the code, please make a [new issue](https://github.com/JuvenileLad/telegram-bot-for-reddit/issues/new/choose).

**Contact me on Telegram [@Juvenile_Lad](https://t.me/yellow_flash_of_kanpur)**