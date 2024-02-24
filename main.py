import youtube_get_methods as yt
import mongoDB_methods     as mdb
import sql_methods         as sql
import misc

from st_on_hover_tabs import on_hover_tabs
import streamlit as st

#-----------------------------Methods------------------------------------------#
#Method to check if inputed channel_ids fetch a channel
def check_channel(channel_id):
    try:
        channel_details = yt.get_channel_details(channel_id)
        return channel_details
    except:
        st.write(f'Invalid data, unable to extract')

#method to extract and upload data to the datalake
def upload_to_mongo(channel_id):

    if channel_id == ['']:
        st.write(f'No Data to upload')
    else:
        with st.spinner('Uploading to db..'):
            channel_details = yt.get_channel_details(channel_id)
            video_ids     = yt.get_channel_videos(channel_id)
            video_details = yt.get_video_details(video_ids)
            comment_details  = []
            for id in video_ids:
                single = yt.get_comment_details(str(video_ids[0]))
                comment_details += single

            mdb.insert_into_mdb(channel_details,video_details,comment_details)
            st.success("Upload to MongoDB successful!")

#---------------------------Streamlit Setup------------------------------------#
st.set_page_config(
                    layout="wide",
                    menu_items={'About': "[My Github Link!](https://github.com/WolfAtTheDesk)"})

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard',
                                  'Extraction',
                                  'Migrate',
                                  'Data Overview'],
                         iconName=['info',
                                   'browser_updated',
                                   'swap_vert',
                                   'analytics'],
                         default_choice=0)


#--------------------------------Pages-----------------------------------------#
if tabs =='Dashboard':
    st.title(":rainbow[Youtube Data Warehousing]")
    st.divider()

    st.header(":red[What is this?]")
    st.markdown(misc.about_text)

    st.header(":green[How to use this tool]")
    st.write(misc.how_to_text)
    st.header(":violet[How it works:]")
    st.write("Overall, this approach involves building a simple UI with Streamlit, retrieving data from the YouTube API, storing it in a MongoDB data lake, migrating it to a SQL data warehouse, querying the data warehouse with SQL, and displaying the data in the Streamlit app.")

    # str1 = st.text_input("test")
    # if st.button('Test'):
    #     st.write(sql.insert_into_videos("styropyro"))

elif tabs == 'Extraction':

    st.write("### Enter YouTube Channel_ID below :")
    channel_ids = st.text_input(" Channel page > Click on About > Click on more > Share > Copy ID").split(',')

    #st.write(channel_ids)
    if channel_ids and st.button("Check channels"):
        channel_details = []
        for channel_id in channel_ids:
            channel_id = channel_id.strip()
            print(channel_id)
            channel_details += check_channel(channel_id)
        st.write(f'#### Following channels found')
        st.table(channel_details)

    if st.button("Upload to MongoDB"):
        for channel_id in channel_ids:
            channel_id = channel_id.strip()
            upload_to_mongo(channel_id)


elif tabs =='Migrate':
    st.markdown("#   ")
    st.markdown("### Select a channel to begin Transformation to SQL")
    ch_names = mdb.channel_names()
    user_input = st.selectbox("Select channel",options= ch_names)
    if st.button("Submit"):
        #try:
        sql.insert_into_videos(user_input)
        sql.insert_into_channels(user_input)
        sql.insert_into_comments(user_input)
        st.success("Migration to MySQL Successful.")
        #except:
        #    st.error("Error encountered. Entries may already be present.")

# VIEW PAGE
elif tabs == 'Data Overview':
    st.write("## :orange[Select any question to get Insights]")
    questions = st.selectbox('Questions',misc.questions)

    if questions == 'What are the names of all the videos and their corresponding channels?':
        st.write("### :violet[Number of videos in each channel :]")
        st.write(sql.videos_by_channels())

    elif questions == 'Which channels have the most number of videos, and how many videos do they have?':
        st.write("### :violet[Channels with most Videos :]")
        st.write(sql.videos_max_channels())


    elif questions == 'What are the top 10 most viewed videos and their respective channels?':

        st.write("### :violet[Most viewed videos :]")
        st.write(sql.views_max_videos())

    elif questions == 'How many comments were made on each video, and what are their corresponding video names?':

        st.write("### :violet[Comments :]")
        st.write(sql.comment_by_video())

    elif questions == 'Which videos have the highest number of likes, and what are their corresponding channel names?':

        st.write(sql.likes_max_videos())
        st.write("### :violet[Most liked videos :]")


    elif questions == 'What is the total number of likes and dislikes for each video, and what are their corresponding video names?':
        st.write("### :violet[Total likes in videos :]")
        st.write(sql.likes_total_videos())

    elif questions == 'What is the total number of views for each channel, and what are their corresponding channel names?':

        st.write("### :violet[Total views per channel :]")
        st.write(sql.views_total_channels())

    elif questions == 'What are the names of all the channels that have published videos in the year 2022?':
        st.write("### :violet[Channels that published in the year 2022 :]")
        st.write(sql.published_in_year())

    elif questions == 'What is the average duration of all videos in each channel, and what are their corresponding channel names?':

        st.write("### :violet[Avg video duration for channels :]")
        st.write(sql.duration_average_channel())


    elif questions == 'Which videos have the highest number of comments, and what are their corresponding channel names?':

        st.write("### :violet[Videos with most comments :]")
        st.write(sql.videos_max_comments())
