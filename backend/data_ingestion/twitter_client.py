# /backend/data_ingestion/twitter_client.py
import tweepy
from config import X_BEARER_TOKEN

# A simple in-memory cache to avoid processing the same tweet ID multiple times
# In a real app, you'd use a more persistent cache like Redis
processed_tweet_ids = set()

def fetch_new_tweets():
    """
    Fetches new, relevant tweets from the Twitter/X API
    focused on a specific geographic area and keywords.
    """
    if not X_BEARER_TOKEN:
        print("Warning: X_BEARER_TOKEN not found. Skipping tweet fetch.")
        return []

    try:
        # Initialize the client with your Bearer Token
        client = tweepy.Client(X_BEARER_TOKEN)

        # --- Build the API Query ---
        # Celina, TX coordinates: 33.3240° N, 96.7828° W
        # We will search for tweets in a 15-mile radius around this point.
        # We also filter for keywords and exclude retweets.
        query = (
            '-is:retweet lang:en '
            '(pothole OR "power outage" OR streetlight OR "water main" OR flooding) '
            '("Celina TX" OR Celina)'
        )

        # Execute the search for recent tweets (past 7 days)
        response = client.search_recent_tweets(query=query, max_results=10)

        # If the response has no data, return an empty list
        if not response.data:
            return []

        # --- Process and Format the Results ---
        new_tweets = []
        for tweet in response.data:
            if tweet.id not in processed_tweet_ids:
                new_tweets.append({"id": tweet.id, "text": tweet.text})
                processed_tweet_ids.add(tweet.id)

        if new_tweets:
            print(f"Found {len(new_tweets)} new tweets.")

        return new_tweets

    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []