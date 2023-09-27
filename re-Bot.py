import praw
import time

#Your Reddit API credentials and user agent
client_id='client_id'
client_secret='client_secret'
username='username'
password='password'
user_agent='user_agent'

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Function to post in a subreddit
def post_in_subreddit(subreddit_name, title, content, image_path=None):
    subreddit = reddit.subreddit(subreddit_name)

    # Check if the subreddit allows images and content is an image
    if subreddit.allow_images and image_path:
        try:
            with open(image_path, 'rb') as image_file:
                subreddit.submit_image(title=title, image_path=image_path, flair_id=None, send_replies=True)
            print(f'Posted in {subreddit_name}: {title}')
        except praw.exceptions.PRAWException as e:
            print(f'Error posting: {e}')
    # Check if the subreddit is text-only
    elif not image_path:
        if subreddit.subreddit_type == 'text':
            try:
                subreddit.submit(title=title, selftext=content)
                print(f'Posted in {subreddit_name}: {title}')
            except praw.exceptions.PRAWException as e:
                print(f'Error posting: {e}')
        else:
            print(f'Subreddit {subreddit_name} does not allow text (self) posts.')
    else:
        print(f'Subreddit {subreddit_name} does not allow the specified type of post.')


# Read data from the file and post to the specified subreddits
with open('data.txt', 'r') as file:
    data = file.read().split('\n\n')

for entry in data:
    lines = entry.split('\n')
    subreddit_name = lines[0].replace('Subreddit: ', '')
    title = lines[1].replace('Title: ', '')
    content = lines[2].replace('Content: ', '')
    image_path = None
    print(f'Lines in entry: {lines}')

    if 'Image:' in lines[3]:
        image_path = lines[3].replace('Image: ', '').strip()

    post_in_subreddit(subreddit_name, title, content, image_path)
    print(f'Posted in {subreddit_name}: {title}')

# Sleep to avoid rate limits
time.sleep(20)
print("\n")

# Function to upvote all posts in a subreddit
def upvote_all_posts_in_subreddit(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.new(limit=2):
        try:
            submission.upvote()
            print(f'Upvoted post in {subreddit_name}: {submission.title}')
            time.sleep(2)  # Sleep for a few seconds to avoid rate limits
        except praw.exceptions.PRAWException as e:
            print(f'Error: {e}')

# Read subreddit names from the data.txt file and upvote posts in those subreddits
with open('data.txt', 'r') as file:
    data = file.read().split('\n\n')

for entry in data:
    lines = entry.split('\n')
    if len(lines) < 4:
        continue  # Skip incomplete entries
    subreddit_name = lines[0].replace('Subreddit: ', '').strip()
    upvote_all_posts_in_subreddit(subreddit_name)  # Call the upvote function with the subreddit name
    print(f'Upvoted posts in {subreddit_name}')

print("\n")

# Function to save Earth-related posts in a subreddit
def save_earth_pics(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    # Define keywords to identify Earth-related posts
    keywords = ['earth', 'planet', 'nature', 'landscape']

    for submission in subreddit.new(limit=3):
        post_title = submission.title.lower()
        if any(keyword in post_title for keyword in keywords):
            try:
                submission.save()
                print(f'Saved Earth-related post in {subreddit_name}: {submission.title}')
                time.sleep(2)  # Sleep for a few seconds to avoid rate limits
            except praw.exceptions.PRAWException as e:
                print(f'Error: {e}')

print("\n")

# Read subreddit names from the data.txt file and save Earth-related posts in those subreddits
with open('data.txt', 'r') as file:
    data = file.read().split('\n\n')

for entry in data:
    lines = entry.split('\n')
    if len(lines) < 4:
        continue  # Skip incomplete entries
    subreddit_name = lines[0].replace('Subreddit: ', '').strip()
    save_earth_pics(subreddit_name)
    print(f'Saved Earth-related posts in {subreddit_name}')  

# Call the function to save Earth-related posts in the "pics" subreddit
save_earth_pics('pics')

print("\n")

# Function to search for subreddits based on a provided query
def search_subreddits(query, limit=5):
    try:
        subreddits = list(reddit.subreddits.search(query, limit=limit))
        for subreddit in subreddits:
            print(f'Search result in {subreddit_name} subreddit is {subreddit.display_name}')
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

print("\n")

time.sleep(10)

