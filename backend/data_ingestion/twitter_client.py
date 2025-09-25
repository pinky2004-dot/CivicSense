import tweepy
import random
from config import X_BEARER_TOKEN

# A simple in-memory cache to avoid processing the same tweet ID multiple times
# In a real app, I'd use a more persistent cache like Redis
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
    
MOCK_TWEETS = [
    {"id": 107, "text": "Huge pothole on Light Farms Way! Nearly blew a tire this morning. #CelinaRoads"},
    {"id": 108, "text": "Anyone know why the sirens went off just now? No storms in sight. #confused"},
    {"id": 109, "text": "Why are the traffic lights at Preston & Punk Carter out AGAIN? Total chaos."},
    {"id": 110, "text": "Trash pickup skipped our street today. Anyone else on Sunset Blvd have this issue?"},
    {"id": 111, "text": "Dog park water fountain hasn’t worked for months. Can the city fix it already?"},
    {"id": 112, "text": "Avoid Frontier Pkwy right now. Police blocking lanes, looks like an accident."},
    {"id": 113, "text": "Our neighborhood pool is green again… algae season I guess 🙄 #Celina"},
    {"id": 114, "text": "What’s with the construction on Preston? Lane closures every other day."},
    {"id": 115, "text": "I just saw someone blow through a stop sign at Malone & 3rd. Dangerous!"},
    {"id": 116, "text": "Why does the city spray for mosquitoes at 5am? Woke up to the truck outside."},
    {"id": 117, "text": "Big tree limb down on Carter Ranch Rd, partially blocking the street."},
    {"id": 118, "text": "Does anyone else’s tap water taste weird today? Metallic or something."},
    {"id": 119, "text": "It’s pitch black by the high school. Half the streetlights are out. Safety issue!"},
    {"id": 120, "text": "Graffiti on the new playground already… sad to see. #CelinaTX"},
    {"id": 121, "text": "Why is there no left-turn arrow at Preston & Founders? Traffic is insane."},
    {"id": 122, "text": "Fire truck and ambulance just flew down Louisiana Dr. Anyone know what happened?"},
    {"id": 123, "text": "The trains are taking forever lately… 20 min at the crossing this morning."},
    {"id": 124, "text": "Overgrown weeds blocking the sidewalk on Walnut St. Can barely walk a stroller through."},
    {"id": 125, "text": "Random power outage hit Light Farms. Whole street went dark for 10 minutes."},
    {"id": 126, "text": "Someone left a mattress on the side of the road near Ownsby. Looks terrible."},
    {"id": 127, "text": "The splash pad is closed AGAIN. Why is it always broken in summer?"},
    {"id": 128, "text": "That roundabout by the high school is confusing and dangerous. Needs better signage."},
    {"id": 129, "text": "Is the city doing anything about all these stray dogs lately? I see packs running around."},
    {"id": 130, "text": "Car stalled out in the middle of Preston Rd, backing up traffic for miles."},
    {"id": 131, "text": "The fountain downtown is empty and looks abandoned. Maintenance needed ASAP."},
    {"id": 132, "text": "Any updates on when the new rec center is opening? Been waiting forever."},
    {"id": 133, "text": "Dust clouds everywhere from the new housing construction. Hard to breathe outside."},
    {"id": 134, "text": "School zone lights didn’t flash this morning. Cars speeding through. Dangerous."},
    {"id": 135, "text": "Someone dumped a bunch of tires behind the strip mall on Preston. Gross."},
    {"id": 136, "text": "Police have part of 6th St blocked. Anyone know why?"},
    {"id": 137, "text": "Sidewalk by Celina Park is cracked and uneven. Nearly tripped jogging this morning."},
    {"id": 138, "text": "City hall parking lot lights don’t turn on at night. Super dark and sketchy."},
    {"id": 139, "text": "Why are we always the last to get our roads salted? Ice everywhere this morning."},
    {"id": 140, "text": "Library A/C must be out. Place feels like a sauna. #CelinaTX"},
]

def fetch_new_tweets():
    """Simulates fetching new, relevant tweets."""
    # I will return one random tweet to simulate a new event.
    return [random.choice(MOCK_TWEETS)]