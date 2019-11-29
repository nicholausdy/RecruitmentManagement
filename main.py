from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

consumer_key="ShGU1J46KOaWtJm5IvgfY8hp9"
consumer_secret="JyfvAE2udldVzCkxFEAFjvETJnWfclh2ZObQg9P1NVs58ndR1d"
access_token="362485949-3GOV8E370bSqCd0qMmjzvEiwD0SuZwW38NwBiToO"
access_token_secret="rTjYaVV6XIgNmCG0l1N41LdwBqeOapChzpksahxf0EaLA"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

def getUserData(username):
  try:
    account_list = []
    if (len(sys.argv) > 1):
      account_list = sys.argv[1:]
    else:
      print("Please provide a list of usernames at the command line.")
      sys.exit(0)

    if len(account_list) > 0:
      for target in account_list:
        print("Getting data for " + target)
        item = auth_api.get_user(target)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        print("description: " + item.description)
        print("statuses_count: " + str(item.statuses_count))
        print("friends_count: " + str(item.friends_count))
        print("followers_count: " + str(item.followers_count))

        tweets = item.statuses_count
        account_created_date = item.created_at
        delta = datetime.utcnow() - account_created_date
        account_age_days = delta.days
        print("Account age (in days): " + str(account_age_days))
        if account_age_days > 0:
          print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))

        hashtags = []
        mentions = []
        tweet_count = 0
        end_date = datetime.utcnow() - timedelta(days=30)
        for status in Cursor(auth_api.user_timeline, id=target).items():
          tweet_count += 1
          if hasattr(status, "entities"):
            entities = status.entities
            if "hashtags" in entities:
              for ent in entities["hashtags"]:
                if ent is not None:
                  if "text" in ent:
                    hashtag = ent["text"]
                    if hashtag is not None:
                      hashtags.append(hashtag)
            if "user_mentions" in entities:
              for ent in entities["user_mentions"]:
                if ent is not None:
                  if "screen_name" in ent:
                    name = ent["screen_name"]
                    if name is not None:
                      mentions.append(name)
          if status.created_at < end_date:
            break

        print
        print("Most mentioned Twitter users:")
        for item, count in Counter(mentions).most_common(10):
          print(item + "\t" + str(count))

        print
        print("Most used hashtags:")
        for item, count in Counter(hashtags).most_common(10):
          print(item + "\t" + str(count))

        print
        print ("All done. Processed" + str(tweet_count) + " tweets.")
        print

        dump ={
          "AccountID":item.screen_name,
          "AccountName":item.name,
          "AccountDescription":item.description,
          "AccountStatus":item.statuses_count,
          "AccountFriends":item.friends_count,
          "AccountFollowers":item.followers_count,
        }
  except NoUsernameFound as exception:
    dump={'Feedback: No Username Found'}
  finally:
    return dump

