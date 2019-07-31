# Importing the needed libaries 
import dataset
import json
import tweepy
from sqlalchemy.exc import ProgrammingError
from textblob import TextBlob
 
# your credetionals, generated from twitter developer account
CONSUMER_KEY="plz provide your counsumer key"
CONSUMER_SECRET="plz provide your consumer seceret"
ACCESS_TOKEN="Plz provide your ACCESS_TOKEN"
ACCESS_TOKEN_SECRET="plz provide your ACCESS_TOKEN_SECRET"

# connection to sqlite database
db = dataset.connect("sqlite:///tweets.db")

# setting streamlistner class with needed fields to stream
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.retweeted:
            return
        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        device = status.source
        bg_color = status.user.profile_background_color
        blob = TextBlob(text)
        sent = blob.sentiment
        if geo is not None:
            geo = json.dumps(geo)
        if coords is not None:
            coords = json.dumps(coords)
        table = db["Election_2019"]
        table.insert(dict(
            user_description=description,
                          user_location=loc,
                          coordinates=coords,
                          text=text,
                          geo=geo,
                          user_name=name,
                          user_created=user_created,
                          user_followers=followers,
                          id_str=id_str,
                          created=created,
                          retweet_count=retweets,
                          tweeting_device= device, 
                          user_bg_color=bg_color,
                          polarity=sent.polarity,
                          subjectivity=sent.subjectivity))
        print("Tweet inserted.")
    def on_error(self, status_code):
        return True
# running the stream with provided filter keywords for streaming
if __name__ == '__main__':
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  while True:
      try:
          stream_listener = StreamListener()
          stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
          stream.filter(track=["#MainBhiChowkidar"," #PhirEkbaarModiSarkar","#ChowkidarPhirSe", " #iTrustChowkidar #","MainBhiChowkidar","PhirEkbaarModiSarkar","chowkidar","#chowkidar","bjp","#bjp","#modi","#IndiaWithNamo","Narendra Modi","#Narendra Modi","Chowkidar Narendra Modi","#Chowkidar Narendra Modi","#2019Elections","#AbkiBaarPhirModiSarkar"])
      except Exception:
          print("Stream crashed, restarting")
