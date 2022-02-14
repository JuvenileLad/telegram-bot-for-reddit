from .reddit_handler import *
from ..client import myColl, LIMITPERUSER, MAXUSERS, USEREXCEPTION, OWNERURL

def LimitCheck(user_id, type):
    if user_id in USEREXCEPTION:
            return True
    if type == 'user':
        existingUsers = myColl.count_documents({})
        if existingUsers+1 > MAXUSERS:
            return False
        return True
    elif type == 'subs':
        subLength = len(myColl.find_one({"_id": user_id})['subs'])
        if subLength+1 > LIMITPERUSER:
            return False
        return True


def user_in_DB(dict_toCheck):
    d = myColl.find_one({"_id": dict_toCheck['_id']})
    if d != None:
        return True
    return False

def sub_in_DB(subreddit, user_id):
    d = myColl.find_one({"_id": user_id})
    for i in d['subs']:
        if i['subreddit'].lower() == (subreddit.display_name).lower():
            return True
    return False

def list_db(user_id):
    ls = ''''''
    a = myColl.find_one({"_id": user_id})['subs']
    for n in a:
        ls = ls+n['subreddit']+'\n'
    return [ls, len(a)]

def wholeDB():
    db = myColl.find()
    return db

def update_channel(user_id, new_channel):
    for i in myColl.find({"_id": user_id}):
        i['channel'] = new_channel
        myColl.update_one({"_id": user_id}, {"$set": i})
        reply = f"Channel updated to {new_channel}. (Make sure I am admin in that channel)"
        return reply
    reply = "Please add a subreddit first!"
    return reply

class subDB():
    def __init__(self, user_id, subreddit) -> None:
        self.user = user_id  # telegram user id
        # check if user exists in DB
        # if yes, assign entry to user_exists
        self.user_entry = user_in_DB({"_id": self.user})
        # if user exists, check if sub exists
        self.subs = sub_in_DB(subreddit, self.user) if self.user_entry else False

    def add_sub(self, subreddit, sub_dict):
        if self.subs:
            return "Subreddit already added!"
        if self.user_entry and not self.subs: # user exists and sub does not exist
            if LimitCheck(self.user, 'subs'): # check if user can add more subs
                new_sub = {'subreddit': (subreddit.display_name).lower(),
                        'last_post': sub_dict['id']}
                mongo_query = {"_id": self.user}
                mongo_set = {"$push": {"subs": new_sub}}
                myColl.update_one(mongo_query, mongo_set)
            else:
                return f"Sorry, you can't add more subreddits. Please contact my [creator]({OWNERURL}) to add more subreddits." # reply message
        else:
            if LimitCheck(self.user, 'user'):
                subs = [{"subreddit": (subreddit.display_name).lower(),
                        "last_post": sub_dict["id"]}]
                dict_toAdd = {"_id": self.user, "channel": self.user, "subs": subs}
                myColl.insert_one(dict_toAdd)
            else:
                return f"Sorry, I can't add more users. Please contact my [owner]({OWNERURL}) to add more users."
        return f"r/{subreddit.display_name} Added Successfully!"

    def remove_sub(self, subreddit):
        if not self.subs:
            return "Subreddit not found!"
        mongo_query = {"_id": self.user}
        mongo_pull = {"$pull": {"subs": {"subreddit": (subreddit.display_name).lower()}}}
        myColl.update_one(mongo_query, mongo_pull)
        return "r/{} Removed Successfully!".format(subreddit.display_name)
