import praw
import time

# Your Reddit API credentials and user agent
client_id='qP3lYR-Zm0LRh4cNOXyxeQ'
client_secret='AUHUGLnesig4ZmYleIZ9gbwLRzDSAQ'
username='GlitteringBet6504'
password='Testing@1999'
user_agent='re-Bot by GlitteringBet6504'

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Function to comment on Earth-related posts in a subreddit
def comment_on_earth_posts(subreddit_name, comment_text):
    subreddit = reddit.subreddit(subreddit_name)
    print(comment_text)
    print("I am here 2")
    # Define keywords to identify Earth-related posts
    keywords = ['earth', 'planet', 'nature', 'landscape']

    for submission in subreddit.new(limit=3):  # Adjust the limit as needed
        post_title = submission.title.lower()
        print("I am here 3")
        if any(keyword in post_title for keyword in keywords):
            try:
                print("I am here 4")
                submission.reply(comment_text)
                print("I am here")
                print(f'Commented on Earth-related post in {subreddit_name}: {submission.title}')
                time.sleep(2)  # Sleep for a few seconds to avoid rate limits
            except Exception as e:
                print(f'Error: {e}')

# Read subreddit names from the data.txt file and comment on Earth-related posts
with open('data.txt', 'r') as file:
    data = file.read().split('\n\n')

for entry in data:
    lines = entry.split('\n')
    if len(lines) < 4:
        continue  # Skip incomplete entries
    subreddit_name = lines[0].replace('Subreddit: ', '').strip()
    print(f'comments text{subreddit_name}')
    comment_text = "Looks amazing!"  # Your comment text here
    comment_on_earth_posts(subreddit_name, comment_text)

# Function to search for subreddits based on a provided query
def search_subreddits(query, limit=5):
    try:
        subreddits = list(reddit.subreddits.search(query, limit=limit))
        for subreddit in subreddits:
            print(subreddit.display_name,subreddit_name)
    except praw.exceptions.PRAWException as e:
        print(f'Error: {e}')

# Read data from the file and extract the search queries
with open('data.txt', 'r') as file:
    data = file.read().split('\n\n')

for entry in data:
    lines = entry.split('\n')
    if len(lines) < 4:
        continue  # Skip incomplete entries
    search_query = lines[3].replace('Search Query: ', '').strip()
    subreddit_name=lines[0].replace('Subreddit: ','').strip()
    # Perform subreddit search for each search query
    search_subreddits(search_query)

# Sleep to avoid rate limits
time.sleep(10)
