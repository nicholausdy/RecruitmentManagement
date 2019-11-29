import psycopg2
from psycopg2.extras import RealDictCursor
import json
class DBManager:
	def connect():
		conn = None
		try:
			conn = psycopg2.connect(host="3.227.193.57",port="5432",database="twitter",user="postgres",password="postgres")
			print("connected to database")
			return conn
		except(Exception, psycopg2.DatabaseError) as error :
			print(error)

	def close(conn):
		if conn is not None:
			conn.close()
			print("Database connection closed")

	def insertToProfile(info):
		conn=DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ INSERT INTO twittertable(account_username,account_name,account_description,account_status,account_friends,account_followers) VALUES (%(username)s,%(name)s,%(description)s,%(status)s,%(friends)s,%(followers)s)"""
			values = {
				'username':info['AccountID'],
				'name':info['AccountName'],
				'description':info['AccountDescription'],
				'status':info['AccountStatus'],
				'friends':info['AccountFriends'],
				'followers':info['AccountFollowers'],
			}
			cur.execute(query,values)
			conn.commit()
			count = cur.rowcount
			dump = {'Message' : 'Record inserted successfully into database'}
			print(dump)
			return json.dumps(dump)
		except(Exception,psycopg2.Error) as error :
			if(conn):
				dump={'Message':'Failed to insert record into mobile table','Detail':error}
				print(dump)
				return json.dumps(dump)
		finally:
			DBManager.close(conn)
	
	def readFromAccount(username):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM twittertable WHERE account_username = %(id)s """
			values = {'id': username}
			cur.execute(query,values)
			if(cur.rowcount == 0):
				dump = {'Feedback': 'Invalid AccountID','AccountID':username}
				print(dump)
				return json.dumps(dump)
			else:
				dump = json.dumps(cur.fetchone())
				print(dump)
				return dump
		except(Exception, psycopg2.Error) as error:
			if(conn):
				dump = {'Message': 'Failed to read record from mobile table','Detail':error}
				print(dump)
				return json.dumps(dump)
		finally:
			DBManager.close(conn)