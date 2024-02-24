import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

mongoPassword = os.getenv('MONGO_PASSWORD')  #Load key from secret

client = pymongo.MongoClient(f"mongodb+srv://warwolf:{mongoPassword}@cluster0.gis05ag.mongodb.net/")
db = client.Youtube_Data


channel_table = db.channels
video_table   = db.videos
comment_table = db.comments

#channel_table.create_index([("Channel_id", 1)], unique=True)
#video_table.create_index([("Video_id", 1)], unique=True)
#comment_table.create_index([("Comment_id", 1)], unique=True)


def insert_into_mdb(channel_details,video_details,comment_details):
    try:
        channel_table.insert_many(channel_details,ordered= False)
        video_table.insert_many(video_details,ordered= False)
        comment_table.insert_many(comment_details,ordered= False)
    except:
        print(f"DuplicateKeyError")
def channel_names():
    ch_name = []
    for i in db.channels.find():
        ch_name.append(i['Channel_name'])
    return ch_name
