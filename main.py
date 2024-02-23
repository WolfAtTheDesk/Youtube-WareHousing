import youtube_get_methods as yt
import mongoDB_methods     as mdb
import sql_methods         as sql

from st_on_hover_tabs import on_hover_tabs
import streamlit as st


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



if tabs =='Dashboard':
    st.title(":rainbow[Youtube Data Warehousing]")
    st.divider()

    st.header(":red[What is this?]")
    st.markdown("""The developed tool is a powerful yet user-friendly Streamlit application designed for accessing and analyzing data from multiple YouTube channels effortlessly. With this tool, users can input a YouTube channel ID and retrieve a comprehensive range of relevant data, including channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, and comments for each video, all seamlessly integrated using the Google API.

Moreover, the tool offers the functionality to store this data efficiently in a MongoDB database, serving as a versatile data lake for future analysis and reference. Users can easily collect data from up to 10 different YouTube channels and store them in the data lake with a simple click of a button, streamlining the data collection process.

Additionally, the tool provides an intuitive option to select a specific channel and migrate its data from the data lake to a SQL database, organizing the information into structured tables for enhanced manageability and query capabilities.

Furthermore, users can leverage the search functionality within the SQL database, offering various search options and the ability to join tables to retrieve comprehensive channel details, empowering users with the insights they need for in-depth analysis and decision-making.

In summary, this Streamlit application serves as a versatile and efficient solution for accessing, storing, and analyzing YouTube channel data, offering a seamless experience for users seeking valuable insights from their favorite channels.""")

    st.header(":green[How to use this tool]")
    st.write("""To effectively utilize the features of this Streamlit application for accessing and analyzing YouTube channel data, follow these step-by-step instructions:

1. **Retrieve the Youtube IDs**
   - Navigate to the URL of the channels
   - Click on About
   - Click on more > channel id
2. **Input YouTube Channel ID:**
   - On the main page of the application, you'll find a designated input field to enter the YouTube channel ID of interest.
   - Locate the YouTube channel ID by visiting the desired YouTube channel and extracting it from the URL or using other methods provided by YouTube's API documentation.

3. **Retrieve Channel Data:**
   - After entering the YouTube channel ID, click on the "Retrieve Data" button to initiate the process of fetching relevant data from the specified channel.
   - The retrieved data will include the channel name, subscribers count, total video count, playlist ID, video ID, likes, dislikes, and comments for each video.

4. **Storage Options:**
   - Once the data is retrieved, you have the option to store it in a MongoDB database as a data lake by clicking on the corresponding button.
   - You can collect data for up to 10 different YouTube channels and store them in the data lake by repeating the process for each channel and clicking on the storage button.

5. **Migration to SQL Database:**
   - If you wish to migrate the data from the data lake to a SQL database, select the desired channel name from the list provided.
   - Click on the "Migrate to SQL Database" button to transfer the data to the SQL database as structured tables.

6. **Search and Retrieval from SQL Database:**
   - Utilize the search functionality within the SQL database to retrieve specific data based on different search options.
   - You can join tables to get comprehensive channel details and insights, enhancing the depth of your analysis.

7. **Exploring Additional Features:**
   - Explore any additional features or options provided by the application, such as filtering options, visualization tools, or export functionalities, depending on the application's design.

8. **Feedback and Support:**
   - If you encounter any issues or have suggestions for improvement, feel free to provide feedback to the application developers for further enhancement.

By following these instructions, you can effectively use the Streamlit application to access, store, and analyze data from multiple YouTube channels with ease and efficiency.""")

    st.header(":violet[How it works:]")
    st.write("Overall, this approach involves building a simple UI with Streamlit, retrieving data from the YouTube API, storing it in a MongoDB data lake, migrating it to a SQL data warehouse, querying the data warehouse with SQL, and displaying the data in the Streamlit app.")

    if st.button("check"):
        mdb.insert_into_mdb(channel_details,video_details,comment_details)
        st.success("Upload to MongoDB successful !!")


elif tabs == 'Extraction':

    st.markdown("#    ")
    st.write("### Enter YouTube Channel_ID below :")
    channel_id = st.text_input(" Channel page > Click on About >Click on more > Channel id").split(',')
    st.write(channel_id)
    if channel_id and st.button("Check channels"):
        try:
            channel_details = yt.get_channel_details(channel_id)
            st.write(f'#### Extracted data from :green["{channel_details[0]["Channel_name"]}"] channel')
            st.table(channel_details)
        except:
            st.write(f'Invalid data, unable to extract')

    if st.button("Upload to MongoDB"):
        if channel_id == ['']:
            st.write(f'No Data to upload')
        else:
            with st.spinner('Uploading to db..'):
                print(channel_id)
                channel_details = yt.get_channel_details(channel_id)
                print(channel_details[0])
                video_ids     = yt.get_channel_videos(channel_id)
                print(video_ids[0])
                video_details = yt.get_video_details(video_ids)
                print(video_details[0])
                comment_details  = []
                # for id in video_ids:
                single = yt.get_comment_details(str(video_ids[0]))
                comment_details += single
                print("uploading to mongo")
                mdb.insert_into_mdb(channel_details,video_details,comment_details)
                st.success("Upload to MongoDB successful !!")

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
elif tabs == 'Data Overview':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))
