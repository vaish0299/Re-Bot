# Reddit Automation Script

This script is designed to automate various tasks on Reddit using the PRAW (Python Reddit API Wrapper) library. It can perform the following actions:

1. **Posting to Subreddits**: The script reads data from a file (`data.txt`) and posts content to specified subreddits. It supports both text and image posts.

2. **Upvoting Posts**: It can upvote the latest posts in the specified subreddits.

3. **Saving Earth-related Posts**: The script saves Earth-related posts in the specified subreddits based on predefined keywords.

4. **Searching for Subreddits**: It can search for subreddits based on user-defined search queries.

## Prerequisites

Before running the script, make sure you have:

- Reddit API credentials: You need to obtain a `client_id`, `client_secret`, `username`, `password`, and `user_agent` from Reddit for authentication. Replace the placeholders in the script with your credentials.

## Installation

To run this script, you need to have Python installed on your system. You also need to install the PRAW library if you haven't already. You can install PRAW using pip:

```bash 
pip install praw
```

## Usage

To use this script, follow these steps:

1. **Create a `data.txt` File**: Create a file named `data.txt` containing the tasks you want the script to perform. Each task should be separated by two blank lines. Here's an example format:

    ```
    Subreddit: your_subreddit
    Title: Your Post Title
    Content: Your Post Content
    Image: path_to_image.jpg
    Search Query: query_for_search

    Subreddit: another_subreddit
    Title: Another Post Title
    Content: Another Post Content
    Image: another_image.jpg
    Search Query: another_query
    ```

    - `Subreddit`: The subreddit where you want to perform the action.
    - `Title`: The title of the post (for posting tasks).
    - `Content`: The content of the post (for posting tasks).
    - `Image`: Path to the image file (for posting image tasks, optional).
    - `Search Query`: The query for subreddit search (for searching tasks, optional).

2. **Run the Script**: Open your terminal and run the script using the following command:

    ```bash
    python script_name.py
    ```

    Replace `script_name.py` with the name of the script file.

3. **Script Execution**: The script will read the tasks from `data.txt` and perform the specified actions for each task. These actions may include posting to subreddits, upvoting posts, saving Earth-related posts, or searching for subreddits based on your input.

4. **Notes on Rate Limits**: The script includes sleep periods to avoid rate limits imposed by Reddit. You can adjust these sleep durations in the script if needed.

5. **API Credentials**: Ensure that you have Reddit API credentials (client ID, client secret, username, password, and user agent) and replace the placeholders in the script with your actual credentials.


