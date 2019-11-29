import json
import http.server
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
import threading
from socketserver import ThreadingMixIn
import ssl
from twitter_database import DBManager
from twitter_main import UserData

class Parse:
	def pathURLBeforeID(url):
		parsed = urlparse(url)
		path = parsed.path
		parts = path.split('/')
		endpoint = '/'
		for i in range(1,4):
			endpoint = endpoint + parts[i]
			endpoint = endpoint + '/'
		return endpoint
	def pathID(url):
		parsed = urlparse(url)
		path = parsed.path
		parts = path.split('/')
		return parts[4]

class Request(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if Parse.pathURLBeforeID(self.path) == '/users/accounts/profile/' :
			username = Parse.pathID(self.path)
			print(username)
			db_query_result = json.loads(DBManager.readFromAccount(username))
			print(db_query_result)
			if "Feedback" in db_query_result:
				get_result = UserData.getUserData(username)
				print(get_result)
				insert_result = DBManager.insertToProfile(get_result)
				print(insert_result)
				if insert_result['Message'] == 'Record inserted sucessfully into database':
					db_query_result = json.loads(DBManager.readFromAccount(username))
					print(db_query_result)
					self.send_response(200)
					self.send_header("Content-type","application/json")
					self.end_headers()
					self.wfile.write(json.dumps(db_query_result).encode())
			elif "account_username" in db_query_result:
				self.send_response(200)
				self.send_header("Content-type","application/json")
				self.send_header("Access-Control-Allow-Origin","*")
				self.end_headers()
				self.wfile.write(json.dumps(db_query_result).encode())

		elif Parse.pathURLBeforeID(self.path) == '/users/accounts/stats/' :
			username = Parse.pathID(self.path)
			print(username)
			db_query_result = json.loads(DBManager.readFromStats(username))
			print(db_query_result)
			if "Feedback" in db_query_result:
				get_result = UserData.getUserStats(username)
				print(get_result)
				insert_result = DBManager.insertToStats(get_result)
				print(insert_result)
				if insert_result['Message'] == 'Record inserted sucessfully into database':
					db_query_result = json.loads(DBManager.readFromStats(username))
					print(db_query_result)
					self.send_response(200)
					self.send_header("Content-type","application/json")
					self.end_headers()
					self.wfile.write(json.dumps(db_query_result).encode())
			elif "account_username" in db_query_result:
				self.send_response(200)
				self.send_header("Content-type","application/json")
				self.send_header("Access-Control-Allow-Origin","*")
				self.end_headers()
				self.wfile.write(json.dumps(db_query_result).encode())

		elif Parse.pathURLBeforeID(self.path) == '/users/accounts/tweets/' :
			username = Parse.pathID(self.path)
			print(username)
			db_query_result = json.loads(DBManager.readFromTweets(username))
			print(db_query_result)
			if "Feedback" in db_query_result:
				get_result = UserData.getTimelineTweets(username)
				print(get_result)
				insert_result = DBManager.insertToTweets(get_result)
				print(insert_result)
				if insert_result['Message'] == 'Record inserted sucessfully into database':
					db_query_result = json.loads(DBManager.readFromTweets(username))
					print(db_query_result)
					self.send_response(200)
					self.send_header("Content-type","application/json")
					self.send_header("Access-Control-Allow-Origin","*")
					self.end_headers()
					self.wfile.write(json.dumps(db_query_result).encode())
			elif "account_username" in db_query_result:
				self.send_response(200)
				self.send_header("Content-type","application/json")
				self.send_header("Access-Control-Allow-Origin","*")
				self.end_headers()
				self.wfile.write(json.dumps(db_query_result).encode())


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	pass

if __name__ == '__main__':
	port=10100
	server = ThreadedHTTPServer(("",port),Request)
	try:
		print("Twitter serving at port ",port,"...")
		server.serve_forever()
	except KeyboardInterrupt:
		print("End")
		server.socket.close()