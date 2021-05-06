import datetime
import pymongo
from pymongo import MongoClient
import bcrypt
import humanize

class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        inserted = self.Posts.insert({"username": data.username, "content": data.content, "date_added": datetime.datetime.now()})
        return True

    def get_all_posts(self):
        all_posts = self.Posts.find().sort("date_added", -1)
        new_posts = []
        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            post["timestamp"] = humanize.naturaltime(datetime.datetime.now()-post["date_added"])
            new_posts.append(post)

        return new_posts

