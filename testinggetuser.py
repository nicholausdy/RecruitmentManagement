from twitter_main import UserData
from twitter_database import DBManager

a = UserData.getUserData('williamhalimwh')
print(a)
DBManager.insertToProfile(a)
print(DBManager.readFromAccount('williamhalimwh'))