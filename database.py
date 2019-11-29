import psycopg2

class DBManager:
	def connect():
		conn = None
		try:
			conn = psycopg2.connect(host="0.0.0.0",database="Twitter",user="postgres",password="postgres")
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
			cur = conn.cursor()
			query = """ INSERT INTO profile(account_username,account_name,account_description,account_status,account_friends,account_followers) VALUES (%(username)s,%(name)s,%(description)s,%(status)s,%(friends)s,%(followers)s)"""
			values = {
				'account_username':info['AccountID'],
				'account_name':info['AccountName'],
				'account_description':info['AccountDescription'],
				'account_status':info['AccountStatus'],
				'account_friends':info['AccountFriends'],
				'account_followers':info['AccountFollowers'],
			}
			cur.execute(query,values)
			conn.commit()
			count = cur.rowcount
			dump = {'Message' : 'Record inserted successfully into database'}
			message = [dump['Message']]
			print(dump)
			return message
		except(Exception,psycopg2.Error) as error :
			if(conn):
				dump={'Message':'Failed to insert record into mobile table','Detail':error}
				message = [dump['Message'],dump['Detail']]
				print(dump)
				return message
		finally:
			DBManager.close(conn)
	
	def readFromAccount(username):
		conn = DBManager.connect()
		try:
			cur = conn.cursor()
			query = """ SELECT * FROM profile WHERE account_username = %(id)s """
			values = {'id': username}
			cur.execute(query,values)
			if(cur.rowcount == 0):
				dump = {'Feedback': 'Invalid AccountID','AccountID':username}
				message = [dump['Feedback'],dump['AccountID']]
				print(dump)
				return message
			else:
				result = cur.fetchall()
				for row in result:
					dump = {'AccountID':row[0],'AccountName':row[1],'AccountDescription':row[2],'AccountStatus':row[3],'AccountFriends':row[4],'AccountFollowers':row[5]}
				message = [dump['AccountID'],dump['AccountName'],dump['AccountDescription'],dump['AccountStatus'],dump['AccountFriends'],dump['AccountFollowers']]
				print(dump)
				return message
		except(Exception, psycopg2.Error) as error:
			if(conn):
				dump = {'Message': 'Failed to read record from mobile table','Detail':error}
				message = [dump['Message'],dump['Detail']]
				print(dump)
				return message
		finally:
			DBManager.close(conn)