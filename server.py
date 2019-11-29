import json
import http.server
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
import threading
from socketserver import ThreadingMixIn
import ssl
from database import DBManager

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

class Wait:
	def waitForResponse(server):
		server.send_response(200)
		server.send_header("Content-type","application/json")
		server.end_headers()
		wait_message = {'Feedback': 'Username not found'}
		server.wfile.write(json.dumps(wait_message).encode())

class Request(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if Parse.pathURLBeforeID(self.path) == '/users/accounts/profile/' :
			username = Parse.pathID(self.path)
			db_query_result = DBManager.readFromAccount(username)
			message = threading.currentThread.getName()
			print(message)
			if db_query_result[0] == 'InvalidAccountID':
				Wait.waitforResponse(self)
				get_result = getUserData(username)
				insert_result = DBManager.insertToAccount(get_result)
				if insert_result[0] == 'Record inserted sucessfully into database':
					db_query_result = DBManager.readFromAccount(username)
					dict_result = {
						'AccountID':db_query_result[0],
						'AccountName':db_query_result[1],
						'AccountDescription':db_query_result[2],
						'AccountStatus':db_query_result[3],
						'AccountFriends':db_query_result[4],
						'AccountFollowers':db_query_result[5],
					}
					self.send_response(200)
					self.send_header("Content-type","application/json")
					self.end_headers()
					message = threading.currentThread().getName()
					print(message)
					self.wfile.write(json.dumps(error_message).encode())

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	pass

if __name__ == '__main__':
	port=10100
	server = ThreadedHTTPServer(("",port),Request)
	try:
		print("Twitter serving at port ",port,"...")
		server.serve_forever()
	except KeyboardInterrupt:
		print("Dammn")
		server.socket.close()