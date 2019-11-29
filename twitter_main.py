from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy

consumer_key="ShGU1J46KOaWtJm5IvgfY8hp9"
consumer_secret="JyfvAE2udldVzCkxFEAFjvETJnWfclh2ZObQg9P1NVs58ndR1d"
access_token="362485949-3GOV8E370bSqCd0qMmjzvEiwD0SuZwW38NwBiToO"
access_token_secret="rTjYaVV6XIgNmCG0l1N41LdwBqeOapChzpksahxf0EaLA"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)


class UserData :
  def getUserData(username):
    try:
      account_list = [username]
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

  def getTimelineTweets(username):
    try:
      api = tweepy.API(auth)
      account_list = [username]
      if len(account_list) > 0:
        for target in account_list:
          print("Getting data for " +target+"'s tweets")
          item = auth_api.get_user(target)
          count = 5
          result = []
          for i in range (0,5):
            tweet = api.user_timeline(id = username)[i]
            result.append(tweet.text)
          print(result)
          dump={
            "Tweet1":result[0],
            "Tweet2":result[1],
            "Tweet3":result[2],
            "Tweet4":result[3],
            "Tweet5":result[4],
            "AccountID":item.screen_name,
          }
    except NoUsernameFound as exception:
      dump={'Feedback: No Username Found'}
    finally:
      return dump

  def getUserStats(username):
    try:
      account_list = [username]
      if len(account_list) > 0:
        for target in account_list:
          print("Getting data for " + target)
          item = auth_api.get_user(target)
          tweets = item.statuses_count
          account_created_date = item.created_at
          delta = datetime.utcnow() - account_created_date
          account_age_days = delta.days
          print("Account age (in days): " + str(account_age_days))
          if account_age_days > 0:
            print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))
            variabel = (float(tweets)/float(account_age_days))
          
          dump = {
            "AccountID": item.screen_name,
            "AccountAge": account_age_days,
            "AverageTweets": variabel,
          }
    except NoUsernameFound as exception:
      dump = {'Feedback: No Username Found'}
    finally:
      return dump