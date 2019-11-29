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

