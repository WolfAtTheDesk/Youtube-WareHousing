import os
import googleapiclient
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

scopes = ["https://www.googleapis.com/auth/youtube.readonly"] # Only access data from the API
api_key = os.getenv('API_KEY')  #Load key from secret

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key) # Establishing connection to Youtube's Data V3 API


# Method to get details of a channel using an ID, returns dictionary of details.
def get_channel_details(channel_id):
    ch_data = []
    response = youtube.channels().list(part = 'snippet,contentDetails,statistics',id= channel_id).execute()

    for i in range(len(response['items'])):
        data = dict(Channel_id   = channel_id,
                    Channel_name = response['items'][i]['snippet']['title'],
                    Playlist_id  = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'],
                    Subscribers  = response['items'][i]['statistics']['subscriberCount'],
                    Views        = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    Description  = response['items'][i]['snippet']['description'],
                    Country      = response['items'][i]['snippet'].get('country')
                    )
        ch_data.append(data)
    return ch_data

# Method to get videos of a channel using its id, returns list of video ids.
def get_channel_videos(channel_id):
    video_ids = []
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    next_page_token = None
    count = 0
    while True and len(video_ids) < 20:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()

        for i in range(len(res['items'])):
            video_ids.append(res['items'][i]['snippet']['resourceId']['videoId'])
        next_page_token = res.get('nextPageToken')
        count += 1

        if next_page_token is None: #no next page, exit while.
            break
    return video_ids

# Method to get details of a video using its id, returns a dictionary of details
def get_video_details(video_ids):
    video_stats = []

    for i in range(0, len(video_ids), 50):
        response = youtube.videos().list(
                                        part="snippet,contentDetails,statistics",
                                        id=','.join(video_ids[i:i+50])).execute()
        for video in response['items']:
            video_details = dict(Channel_name  = video['snippet']['channelTitle'],
                                Channel_id     = video['snippet']['channelId'],
                                Video_id       = video['id'],
                                Title          = video['snippet']['title'],
                                Tags           = video['snippet'].get('tags'),
                                Thumbnail      = video['snippet']['thumbnails']['default']['url'],
                                Description    = video['snippet']['description'],
                                Published_date = video['snippet']['publishedAt'],
                                Duration       = video['contentDetails']['duration'],
                                Views          = video['statistics']['viewCount'],
                                Likes          = video['statistics'].get('likeCount'),
                                Comments       = video['statistics'].get('commentCount'),
                                Favorite_count = video['statistics']['favoriteCount'],
                                Definition     = video['contentDetails']['definition'],
                                Caption_status = video['contentDetails']['caption']
                               )
            video_stats.append(video_details)
    return video_stats


# Method to get comments of a video using its id, returns a list of comments
def get_comment_details(video_id):
    comment_data = []
    try:
        next_page_token = None
        count = 0
        while True and len(comment_data) < 5:
            response = youtube.commentThreads().list(part     = "snippet,replies",
                                                    videoId   = video_id,
                                                    maxResults= 20,
                                                    pageToken = next_page_token).execute()
            for comment in response['items']:
                data = dict(Comment_id          = comment['id'],
                            Video_id            = comment['snippet']['videoId'],
                            Comment_text        = comment['snippet']['topLevelComment']['snippet']['textDisplay'],
                            Comment_author      = comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                            Comment_posted_date = comment['snippet']['topLevelComment']['snippet']['publishedAt'],
                            Like_count          = comment['snippet']['topLevelComment']['snippet']['likeCount'],
                            Reply_count         = comment['snippet']['totalReplyCount']
                           )
                comment_data.append(data)
            next_page_token = response.get('nextPageToken')
            count += 1
            if next_page_token is None:
                break
    except:
        print("Failed")
        pass
    return comment_data
