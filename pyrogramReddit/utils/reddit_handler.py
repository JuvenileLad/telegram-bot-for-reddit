from dis import dis
from ..client import myColl, reddit, bot
import traceback

async def Check_sub(subreddit):
    is_valid = await reddit.subreddit(subreddit)
    try: # valid subreddit if submissions exist
        async for submission in is_valid.new(limit=1):
            break  # break if submissions exist
        return is_valid # valid subreddit
    except: # invalid subreddit if no submissions exist
        return False

async def get_data(subreddit, requirements):
    data = {} 
    async for submission in subreddit.new(limit=1): # get latest submission
        submission = vars(submission) #convert to dictionary
        for r in requirements: # get required data
            data[r] = submission[r] # add data to dictionary
    return data

async def update_subs(subs_list):
    for i in subs_list:
        updated_subs = []
        submission_obj = []
        index = 0
        for j in i['subs']:
            subreddit = await reddit.subreddit(j['subreddit'])
            async for submission in subreddit.new(limit=1):
                if submission.id != j['last_post']:
                    print(f" > new post in {j['subreddit']}")
                    i['subs'][index]['last_post'] = submission.id
                    mongo_query = {"_id": i['_id']}
                    mongo_set = {"$set": i}
                    myColl.update_one(mongo_query, mongo_set)
                    submission_obj.append(submission)
            index += 1
        updated_subs.append(i['channel'])
        updated_subs.append(submission_obj)
        await tg_post(updated_subs)

async def tg_post(updated_subs):
    channel_id = updated_subs[0]
    subs = updated_subs[1]
    for i in subs:
        print(f"\n{i.title}")
        sub_dict = (vars(i))

        preview = True if 'preview' in sub_dict.keys() else False
        media_metadata = True if 'media_metadata' in sub_dict.keys() else False
        
        caption = f"[{sub_dict['subreddit_name_prefixed']}](https://www.reddit.com/{sub_dict['permalink']}): **{sub_dict['title']}**"
        caption += f"{sub_dict['selftext_html']}" if sub_dict['selftext'] else f"\n"
        
        if len(sub_dict['selftext']) > 4096:
            sub_dict['selftext'] = sub_dict['selftext_html'][:3000] + '...'
        try:
            if not preview and not media_metadata:
                await bot.send_message(channel_id, caption, disable_web_page_preview=True)
            elif preview:
                image = sub_dict['preview']['images'][0]['source']['url']
                await bot.send_photo(chat_id=channel_id, photo=image, caption=caption, disable_web_page_preview=True)
            elif media_metadata:
                for md in sub_dict['media_metadata']:
                    image = sub_dict['media_metadata'][md]['s']['u']
                await bot.send_photo(chat_id=channel_id, photo=image, caption=caption, disable_web_page_preview=True)
        except:
            traceback.print_exc()
