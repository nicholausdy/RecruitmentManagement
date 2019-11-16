import json
import http.server
from LinkedIn_scrape import Scraper
from LinkedIn_dbInterface import DBManager
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
from socketserver import ThreadingMixIn
import threading
import ssl

class Parse:
    def pathURLBeforeID(url):
    #memberikan output path sebelum id
        parsed = urlparse(url) #parse url menjadi komponen2nya
        path = parsed.path #memperoleh komponen path dari hasil parsing
        parts = path.split('/') #menggabungkan kembali komponen-komponen yang sudah di-parsing
        endpoint = '/'
        for i in range(1,4):
            endpoint = endpoint + parts[i]
            endpoint = endpoint + '/'
        return endpoint
    def pathID(url):
    #memperoleh nomor id yang ada dalam URL path
        parsed = urlparse(url)
        path = parsed.path
        parts = path.split('/')
        return parts[4]

    def pathURLBeforeEmail(url):
    #memberikan output path sebelum email
        parsed = urlparse(url)
        path = parsed.path
        parts = path.split('/')
        endpoint = '/'
        for i in range(1,5):
            endpoint = endpoint + parts[i]
            endpoint = endpoint + '/'
        return endpoint

    def pathEmail(url):
    #memperoleh nomor email yang ada dalam URL path
        parsed = urlparse(url)
        path = parsed.path
        parts = path.split('/')
        return parts[5]

    def pathURLGetOne(url):
        parsed = urlparse(url)
        path = parsed.path
        return path

    def pathURLGetThree(url):
        parsed = urlparse(url)
        path = parsed.path
        parts = path.split('/')
        endpoint = '/'
        for i in range(1,3):
            endpoint = endpoint + parts[i]
            endpoint = endpoint + '/'
        return endpoint + parts[3]

    def pathURLGetTwo(url):
        parsed = urlparse(url)
        path = parsed.path
        parts = path.split('/')
        endpoint = '/'
        for i in range(1,2):
            endpoint = endpoint + parts[i]
            endpoint = endpoint + '/'
        return endpoint + parts[2]

class Wait:
    def waitForResponse(server):
    #tampilan menunggu hasil scrape
    #khusus untuk ditampilkan jika endpoint diakses melalui web browser
        server.send_response(200)
        server.send_header("Content-type","application/json")
        server.end_headers()
        wait_message = {'Feedback': 'Account ID not found on database','Message':'Please wait until scraping is finished (2-3 minutes), then reload the page'}
        server.wfile.write(json.dumps(wait_message).encode())
        

class Request(http.server.SimpleHTTPRequestHandler):
# kelas untuk mengurus API reuqest dari pengguna
    def do_GET(self): #method untuk mengurus HTTP verb GET
        if Parse.pathURLGetOne(self.path) == '/applicants':
            db_query_result = DBManager.readFromApplicants()
            message = threading.currentThread().getName()
            print(db_query_result)
            print(message)
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(db_query_result.encode())

        elif Parse.pathURLGetTwo(self.path) == '/users/all':
            db_query_result = DBManager.readAll()
            message = threading.currentThread().getName()
            print(db_query_result)
            print(message)
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(db_query_result.encode())

        elif Parse.pathURLGetThree(self.path) == '/users/accounts/general':
            db_query_result = DBManager.readAllFromAccount()
            message = threading.currentThread().getName()
            print(db_query_result)
            print(message)
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(db_query_result.encode())

        elif Parse.pathURLGetThree(self.path) == '/users/accounts/education':
            db_query_result = DBManager.readAllFromEducation()
            message = threading.currentThread().getName()
            print(db_query_result)
            print(message)
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(db_query_result.encode())

        elif Parse.pathURLGetThree(self.path) == '/users/accounts/workplace':
            db_query_result = DBManager.readAllFromWorkplace()
            message = threading.currentThread().getName()
            print(db_query_result)
            print(message)
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(db_query_result.encode())


        elif Parse.pathURLBeforeEmail(self.path) == '/user/account/general/email/': #jika endpoint sebagai berikut:
            email = Parse.pathEmail(self.path) #dapatkan id dari hasil parsing
            db_query_result = DBManager.readFromAccount(email) #memperoleh hasil query database dalam bentuk array
            message = threading.currentThread().getName()
            print(message)
            if db_query_result[0] == 'Invalid AccountID': # jika data tidak ditemukan di database, lakukan scraping
                Wait.waitForResponse(self)
                scrape_result = Scraper.scrapingAboutByEmail(email) 
                insert_result = DBManager.insertToAccount(scrape_result) #masukkan hasil scraping ke dalam database
                if insert_result[0] == 'Record inserted successfully into DB':
                    db_query_result = DBManager.readFromAccount(email)
                    # ubah array hasil query menjadi dictionary 
                    dict_result = {'AccountID': db_query_result[0],'AccountName': db_query_result[1],'AccountTitle':db_query_result[2],'AccountRegion':db_query_result[3]} 
                    self.send_response(200)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(dict_result).encode()) # konversi dictionary menjadi json + encode
                else:
                    error_message = {'Feedback': 'Invalid AccountID','AccountID': idSearch} #jika record tidak berhasil dimasukkan ke dalam DB/tidak ada id yang valid, lakukan hal berikut:
                    self.send_response(404)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(error_message).encode())
            elif db_query_result[0] == email: #jika data sudah ada dalam database:
                dict_result = {'AccountID': db_query_result[0],'AccountName': db_query_result[1],'AccountTitle':db_query_result[2],'AccountRegion':db_query_result[3]} 
                self.send_response(200)
                self.send_header("Content-type","application/json")
                self.end_headers()
                message = threading.currentThread().getName()
                print(message)
                self.wfile.write(json.dumps(dict_result).encode())

        elif Parse.pathURLBeforeEmail(self.path) == '/user/account/education/email/': #jika endpoint sebagai berikut:
            email = Parse.pathEmail(self.path) #dapatkan id dari hasil parsing
            db_query_result = DBManager.readFromEducation(email) #memperoleh hasil query database dalam bentuk array
            message = threading.currentThread().getName()
            print(message)
            if db_query_result[0] == 'Invalid AccountID': # jika data tidak ditemukan di database, lakukan scraping
                Wait.waitForResponse(self)
                scrape_result = Scraper.scrapingEducationByEmail(email) 
                insert_result = DBManager.insertToEducation(scrape_result) #masukkan hasil scraping ke dalam database
                if insert_result[0] == 'Record inserted successfully into DB':
                    db_query_result = DBManager.readFromEducation(email)
                    # ubah array hasil query menjadi dictionary 
                    dict_result = {'AccountID': db_query_result[0],'EducationInstitution': db_query_result[1],'EducationTitle':db_query_result[2]} 
                    self.send_response(200)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(dict_result).encode()) # konversi dictionary menjadi json + encode
                else:
                    error_message = {'Feedback': 'Invalid AccountID','AccountID': email} #jika record tidak berhasil dimasukkan ke dalam DB/tidak ada id yang valid, lakukan hal berikut:
                    self.send_response(404)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(error_message).encode())
            elif db_query_result[0] == email: #jika data sudah ada dalam database:
                dict_result = {'AccountID': db_query_result[0],'EducationInstitution': db_query_result[1],'EducationTitle':db_query_result[2]}
                self.send_response(200)
                self.send_header("Content-type","application/json")
                self.end_headers()
                message = threading.currentThread().getName()
                print(message)
                self.wfile.write(json.dumps(dict_result).encode())

        elif Parse.pathURLBeforeEmail(self.path) == '/user/account/workplace/email/': #jika endpoint sebagai berikut
            email = Parse.pathEmail(self.path) #dapatkan id dari hasil parsing
            db_query_result = DBManager.readFromWorkplace(email) #memperoleh hasil query database dalam bentuk array
            message = threading.currentThread().getName()
            print(message)
            if db_query_result[0] == 'Invalid AccountID': # jika data tidak ditemukan di database, lakukan scraping
                Wait.waitForResponse(self)
                scrape_result = Scraper.scrapingWorkplaceByEmail(email) 
                insert_result = DBManager.insertToWorkplace(scrape_result) #masukkan hasil scraping ke dalam database
                if insert_result[0] == 'Record inserted successfully into DB':
                    db_query_result = DBManager.readFromWorkplace(email)
                    # ubah array hasil query menjadi dictionary 
                    dict_result = {'AccountID': db_query_result[0],'Workplace1': db_query_result[1],'Workplace2':db_query_result[2]} 
                    self.send_response(200)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(dict_result).encode()) # konversi dictionary menjadi json + encode
                else:
                    error_message = {'Feedback': 'Invalid AccountID','AccountID': email} #jika record tidak berhasil dimasukkan ke dalam DB/tidak ada id yang valid, lakukan hal berikut:
                    self.send_response(404)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(error_message).encode())
            elif db_query_result[0] == email: #jika data sudah ada dalam database:
                dict_result = {'AccountID': db_query_result[0],'Workplace1': db_query_result[1],'Workplace2':db_query_result[2]}
                self.send_response(200)
                self.send_header("Content-type","application/json")
                self.end_headers()
                message = threading.currentThread().getName()
                print(message)
                self.wfile.write(json.dumps(dict_result).encode())

        elif Parse.pathURLBeforeID(self.path) == '/user/account/general/': #jika endpoint sebagai berikut:
            idSearch = Parse.pathID(self.path) #dapatkan id dari hasil parsing
            db_query_result = DBManager.readFromAccount(idSearch) #memperoleh hasil query database dalam bentuk array
            message = threading.currentThread().getName()
            print(message)
            if db_query_result[0] == 'Invalid AccountID': # jika data tidak ditemukan di database, lakukan scraping
                Wait.waitForResponse(self)
                scrape_result = Scraper.scrapingAbout(idSearch) 
                insert_result = DBManager.insertToAccount(scrape_result) #masukkan hasil scraping ke dalam database
                if insert_result[0] == 'Record inserted successfully into DB':
                    db_query_result = DBManager.readFromAccount(idSearch)
                    # ubah array hasil query menjadi dictionary 
                    dict_result = {'AccountID': db_query_result[0],'AccountName': db_query_result[1],'AccountTitle':db_query_result[2],'AccountRegion':db_query_result[3]} 
                    self.send_response(200)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(dict_result).encode()) # konversi dictionary menjadi json + encode
                else:
                    error_message = {'Feedback': 'Invalid AccountID','AccountID': idSearch} #jika record tidak berhasil dimasukkan ke dalam DB/tidak ada id yang valid, lakukan hal berikut:
                    self.send_response(404)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(error_message).encode())
            elif db_query_result[0] == idSearch: #jika data sudah ada dalam database:
                dict_result = {'AccountID': db_query_result[0],'AccountName': db_query_result[1],'AccountTitle':db_query_result[2],'AccountRegion':db_query_result[3]} 
                self.send_response(200)
                self.send_header("Content-type","application/json")
                self.end_headers()
                message = threading.currentThread().getName()
                print(message)
                self.wfile.write(json.dumps(dict_result).encode())
                
        elif Parse.pathURLBeforeID(self.path) == '/user/account/education/': #jika endpoint sebagai berikut:
            idSearch = Parse.pathID(self.path) #dapatkan id dari hasil parsing
            db_query_result = DBManager.readFromEducation(idSearch) #memperoleh hasil query database dalam bentuk array
            message = threading.currentThread().getName()
            print(message)
            if db_query_result[0] == 'Invalid AccountID': # jika data tidak ditemukan di database, lakukan scraping
                Wait.waitForResponse(self)
                scrape_result = Scraper.scrapingEducation(idSearch) 
                insert_result = DBManager.insertToEducation(scrape_result) #masukkan hasil scraping ke dalam database
                if insert_result[0] == 'Record inserted successfully into DB':
                    db_query_result = DBManager.readFromEducation(idSearch)
                    # ubah array hasil query menjadi dictionary 
                    dict_result = {'AccountID': db_query_result[0],'EducationInstitution': db_query_result[1],'EducationTitle':db_query_result[2]} 
                    self.send_response(200)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(dict_result).encode()) # konversi dictionary menjadi json + encode
                else:
                    error_message = {'Feedback': 'Invalid AccountID','AccountID': idSearch} #jika record tidak berhasil dimasukkan ke dalam DB/tidak ada id yang valid, lakukan hal berikut:
                    self.send_response(404)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(error_message).encode())
            elif db_query_result[0] == idSearch: #jika data sudah ada dalam database:
                dict_result = {'AccountID': db_query_result[0],'EducationInstitution': db_query_result[1],'EducationTitle':db_query_result[2]}
                self.send_response(200)
                self.send_header("Content-type","application/json")
                self.end_headers()
                message = threading.currentThread().getName()
                print(message)
                self.wfile.write(json.dumps(dict_result).encode())

        elif Parse.pathURLBeforeID(self.path) == '/user/account/workplace/': #jika endpoint sebagai berikut
            idSearch = Parse.pathID(self.path) #dapatkan id dari hasil parsing
            db_query_result = DBManager.readFromWorkplace(idSearch) #memperoleh hasil query database dalam bentuk array
            message = threading.currentThread().getName()
            print(message)
            if db_query_result[0] == 'Invalid AccountID': # jika data tidak ditemukan di database, lakukan scraping
                Wait.waitForResponse(self)
                scrape_result = Scraper.scrapingWorkplace(idSearch) 
                insert_result = DBManager.insertToWorkplace(scrape_result) #masukkan hasil scraping ke dalam database
                if insert_result[0] == 'Record inserted successfully into DB':
                    db_query_result = DBManager.readFromWorkplace(idSearch)
                    # ubah array hasil query menjadi dictionary 
                    dict_result = {'AccountID': db_query_result[0],'Workplace1': db_query_result[1],'Workplace2':db_query_result[2]} 
                    self.send_response(200)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(dict_result).encode()) # konversi dictionary menjadi json + encode
                else:
                    error_message = {'Feedback': 'Invalid AccountID','AccountID': idSearch} #jika record tidak berhasil dimasukkan ke dalam DB/tidak ada id yang valid, lakukan hal berikut:
                    self.send_response(404)
                    self.send_header("Content-type","application/json")
                    self.end_headers()
                    message = threading.currentThread().getName()
                    print(message)
                    self.wfile.write(json.dumps(error_message).encode())
            elif db_query_result[0] == idSearch: #jika data sudah ada dalam database:
                dict_result = {'AccountID': db_query_result[0],'Workplace1': db_query_result[1],'Workplace2':db_query_result[2]}
                self.send_response(200)
                self.send_header("Content-type","application/json")
                self.end_headers()
                message = threading.currentThread().getName()
                print(message)
                self.wfile.write(json.dumps(dict_result).encode())




    def do_POST(self): #method untuk mengurus HTTP verb POST
        if Parse.pathURLGetOne(self.path) == '/applicants':
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            info = json.loads(self.data_string)
            print(info)
            message = threading.currentThread().getName()
            print (message)
            db_query_result = DBManager.insertToApplicants(info)
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(db_query_result.encode())



class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    #handle requests in a separate thread
    pass
            
if __name__=='__main__':
#execute server 
    port = 8000
    server = ThreadedHTTPServer(("",port), Request)
    try:
        print("LinkedIn Maid serving at port ", port, "...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Cafe ditutup")
        server.socket.close()







