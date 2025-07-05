from dotenv import load_dotenv
import os
import praw

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),          # from your Reddit app
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),  # from your Reddit app
    user_agent='Stock ticker counter of recent 100 posts by AcanthaceaePristine7'  # any descriptive string
)

subreddit = reddit.subreddit('pennystocks')

for post in subreddit.top(limit=10, time_filter='month'):
    print(post.title)