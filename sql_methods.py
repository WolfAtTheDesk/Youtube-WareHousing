import mongoDB_methods as mdb
import pandas as pd
import mysql.connector as sql
import re

mydb = sql.connect(host="127.0.0.1",
                   user="root",
                   password="root",
                   database= "youtube"
                  )
mycursor = mydb.cursor(buffered=True)

def insert_into_channels(channel_name):
        query = """INSERT INTO Channels VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        for i in mdb.channel_table.find({"Channel_name" : channel_name},{'_id' : 0}):
            result_3 = (
                i["Channel_id"],
                i["Channel_name"],
                i["Playlist_id"],
                int(i["Subscribers"]),
                int(i["Views"]),
                int(i["Total_videos"]),
                i["Description"],
                i["Country"])
            print(result_3)
            try:
                mycursor.execute(query,tuple(result_3))
            except:
                print("CHANNEL MIGRATION FAIL")
            mydb.commit()

def insert_into_videos(user_inp):
        collections1 = mdb.video_table
        query1 = """INSERT INTO Videos VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        for i in collections1.find({"Channel_name" : user_inp},{'_id' : 0}):
            print(i)
            result_3 = (
                i["Channel_name"],
                i["Channel_id"],
                i["Video_id"],
                i["Title"],
                i["Description"],
                i["Published_date"],
                durtion_to_int(i["Duration"]),
                int(i["Views"]),
                int(i["Likes"]),
                int(i["Comments"]),
                int(i["Favorite_count"]),
                i["Definition"])
            print(result_3)
            try:
                mycursor.execute(query1, result_3)
            except:
                pass
            mydb.commit()
#            return result_3

def insert_into_comments(user_inp):
        collections1 = mdb.video_table
        collections2 = mdb.comment_table
        query2 = """INSERT INTO Comments VALUES(%s,%s,%s,%s,%s,%s,%s)"""

        for vid in collections1.find({"Channel_name" : user_inp},{'_id' : 0}):
            for i in collections2.find({'Video_id': vid['Video_id']},{'_id' : 0}):
                try:
                    mycursor.execute(query2,tuple(i.values()))
                except:
                    print("COMMENT FAIL")
                    pass
                mydb.commit()

def videos_by_channels():
    mycursor.execute("""SELECT Title AS Video_Title, Channel_name
                        FROM Videos
                        ORDER BY  Channel_name""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def videos_max_channels():
    mycursor.execute("""SELECT    Channel_name, Total_videos AS Total_Videos
                        FROM Channels
                        ORDER BY Total_videos DESC""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def views_max_videos():
    mycursor.execute("""SELECT    Channel_name, Title AS Video_Title, Views
                        FROM Videos
                        ORDER BY Views DESC
                        LIMIT 10""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def comment_by_video():
    mycursor.execute("""SELECT a.Video_id AS Video_id, a.Title AS Video_Title, b.Total_Comments
                        FROM Videos AS a
                        LEFT JOIN (SELECT Video_id,COUNT(Comment_id) AS Total_Comments
                        FROM Comments GROUP BY Video_id) AS b
                        ON a.Video_id = b.Video_id
                        ORDER BY b.Total_Comments DESC""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def likes_max_videos():
    mycursor.execute("""SELECT    Channel_name,Title AS Title,likes AS Likes_Count
                        FROM Videos
                        ORDER BY likes DESC
                        LIMIT 10""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def likes_total_videos():
    mycursor.execute("""SELECT Title AS Title, likes AS Likes_Count
                        FROM Videos
                        ORDER BY likes DESC""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def views_total_channels():
        mycursor.execute("""SELECT Channel_name, Views
                            FROM Channels
                            ORDER BY Views DESC""")
        df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
        return df

def published_in_year():
    mycursor.execute("""SELECT    Channel_name
                        FROM Videos
                        WHERE Published_date LIKE '2022%'
                        GROUP BY  Channel_name
                        ORDER BY  Channel_name""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def duration_average_channel():
    mycursor.execute("""SELECT    Channel_name,
                        AVG(Duration)/60 AS "Average_Video_Duration (mins)"
                        FROM Videos
                        GROUP BY  Channel_name
                        ORDER BY AVG(Duration)/60 DESC""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def videos_max_comments():
    mycursor.execute("""SELECT    Channel_name,Video_id AS Video_ID,Comments AS Comments
                        FROM Videos
                        ORDER BY Comments DESC
                        LIMIT 10""")
    df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return df

def durtion_to_int(str):
    numbers = [int(x) for x in re.findall(r'\d+', str)]
    count = 0
    duration = 0
    for i in numbers[-1::-1]:
        duration += (60**count) * i
        count +=1
        print(i, duration, count)
    return duration
