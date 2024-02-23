import mongoDB_methods as mdb

import mysql.connector as sql

#CONNECTING WITH MYSQL DATABASE
# mydb = sql.connect(host="127.0.0.1",
#                    user="root",
#                    password="root",
#                    database= "youtube"
#                   )
# mycursor = mydb.cursor(buffered=True)

def insert_into_channels(channel_name):

                query = """INSERT INTO channels VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""

                for i in mdb.channel_table.find({"Channel_name" : channel_name},{'_id' : 0}):
                    print(i.values())
                    mycursor.execute(query,tuple(i.values()))
                mydb.commit()

def insert_into_videos(user_inp):
        collections1 = mdb.video_table
        query1 = """INSERT INTO videos VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        for i in collections1.find({"Channel_name" : user_inp},{'_id' : 0}):
            result_3 = (
                i["Channel_name"],
                i["Channel_id"],
                i["Video_id"],
                i["Title"],
                i["Description"],
                i["Published_date"],
                i["Duration"],
                i["Views"],
                i["Likes"],
                i["Comments"],
                i["Favorite_count"],
                i["Definition"])
            print(result_3)
            mycursor.execute(query1, t)
            mydb.commit()

def insert_into_comments(user_inp):
        collections1 = mdb.video_table
        collections2 = mdb.comment_table
        query2 = """INSERT INTO comments VALUES(%s,%s,%s,%s,%s,%s,%s)"""

        for vid in collections1.find({"Channel_name" : user_inp},{'_id' : 0}):
            for i in collections2.find({'Video_id': vid['Video_id']},{'_id' : 0}):
                mycursor.execute(query2,tuple(i.values()))
                mydb.commit()
