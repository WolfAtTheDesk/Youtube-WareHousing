# YouTube Channel Data Analyzer

YouTube Channel Data Analyzer is a Streamlit application designed to access, store, and analyze data from multiple YouTube channels seamlessly. With this tool, users can retrieve essential information such as channel name, subscribers count, total video count, playlist ID, video ID, likes, dislikes, and comments for each video, and store them efficiently in a MongoDB database or migrate them to a SQL database for structured analysis.

## Features

- Retrieve data from YouTube channels using Google API.
- Store data in a MongoDB database as a data lake.
- Collect data from up to 10 different YouTube channels.
- Migrate data from MongoDB to a SQL database.
- Search and retrieve data from the SQL database using various search options.

## How to Use

1. **Input YouTube Channel ID:** Enter the YouTube channel ID of interest into the designated input field.
2. **Retrieve Data:** Click on the "Retrieve Data" button to fetch relevant data from the specified YouTube channel.
3. **Storage Options:**
   - Store data in MongoDB: Click on the corresponding button to store the retrieved data in a MongoDB database.
   - Collect data for multiple channels: Repeat the process for up to 10 different YouTube channels.
4. **Migration to SQL Database:**
   - Select a channel from the list and click on the "Migrate to SQL Database" button to transfer data from MongoDB to a SQL database.
5. **Search and Retrieval from SQL Database:**
   - Utilize the search functionality within the SQL database to retrieve specific data based on different search options.
   - Join tables to get comprehensive channel details and insights.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/WolfAtTheDesk/Youtube-WareHousing.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   ```
   streamlit run main.py
   ```

## Feedback and Contributions

If you encounter any issues, have suggestions for improvement, or would like to contribute to the project, please feel free to open an issue or submit a pull request on GitHub.

## Preview Video
[Youtube link](https://www.youtube.com/watch?v=UrOyuWZmA54)
