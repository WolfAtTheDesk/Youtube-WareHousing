questions = [
'What are the names of all the videos and their corresponding channels?',
'Which channels have the most number of videos, and how many videos do they have?',
'What are the top 10 most viewed videos and their respective channels?',
'How many comments were made on each video, and what are their corresponding video names?',
'Which videos have the highest number of likes, and what are their corresponding channel names?',
'What is the total number of likes and dislikes for each video, and what are their corresponding video names?',
'What is the total number of views for each channel, and what are their corresponding channel names?',
'What are the names of all the channels that have published videos in the year 2022?',
'What is the average duration of all videos in each channel, and what are their corresponding channel names?',
'Which videos have the highest number of comments, and what are their corresponding channel names?']

how_to_text = """To effectively utilize the features of this Streamlit application for accessing and analyzing YouTube channel data, follow these step-by-step instructions:

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

By following these instructions, you can effectively use the Streamlit application to access, store, and analyze data from multiple YouTube channels with ease and efficiency."""

about_text ="""The developed tool is a powerful yet user-friendly Streamlit application designed for accessing and analyzing data from multiple YouTube channels effortlessly. With this tool, users can input a YouTube channel ID and retrieve a comprehensive range of relevant data, including channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, and comments for each video, all seamlessly integrated using the Google API.

Moreover, the tool offers the functionality to store this data efficiently in a MongoDB database, serving as a versatile data lake for future analysis and reference. Users can easily collect data from up to 10 different YouTube channels and store them in the data lake with a simple click of a button, streamlining the data collection process.

Additionally, the tool provides an intuitive option to select a specific channel and migrate its data from the data lake to a SQL database, organizing the information into structured tables for enhanced manageability and query capabilities.

Furthermore, users can leverage the search functionality within the SQL database, offering various search options and the ability to join tables to retrieve comprehensive channel details, empowering users with the insights they need for in-depth analysis and decision-making.

In summary, this Streamlit application serves as a versatile and efficient solution for accessing, storing, and analyzing YouTube channel data, offering a seamless experience for users seeking valuable insights from their favorite channels."""
