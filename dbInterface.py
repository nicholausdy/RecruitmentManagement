import psycopg2


class DBManager:
    def connect():
        #connect to postgresql
        conn = None
        try:
            #connect using md5 method (change /var/lib/pgsql/10/data/pg_hba.conf method from ident to md5)
            conn = psycopg2.connect(host="localhost",database="linkedin",user="postgres",password="swordbeach") 
            print("Connected to database")
            return conn
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(conn):
        #close connection to postgresql
        if conn is not None:
            conn.close()
            print('Database connnection closed')

    def insertToAccount(info):
        conn = DBManager.connect()
        #create a cursor to execute command
        try:
            cur = conn.cursor()
            query = """ INSERT INTO account(account_id,account_name,account_title,account_region) VALUES (%(id)s,%(name)s,%(title)s,%(region)s) """
            values = {'id':info['AccountID'],'name':info['AccountName'],'title':info['AccountTitle'], 'region':info['AccountRegion']}
            cur.execute(query,values)
            conn.commit()
            count = cur.rowcount
            dump = {'Message': 'Record inserted successfully into DB'}
            message = [dump['Message']]
            print(dump)
            return message
        except(Exception, psycopg2.Error) as error:
            if(conn):
                dump = {'Message':'Failed to insert record into mobile table','Detail':error}
                message = [dump['Message'],dump['Detail']]
                print(dump)
                return message
        finally:
            DBManager.close(conn)

    def insertToEducation(info):
        conn = DBManager.connect()
        #create a cursor to execute command
        try:
            cur = conn.cursor()
            query = """ INSERT INTO education(account_id,education_institution,education_title) VALUES (%(id)s,%(inst)s,%(title)s) """
            values = {'id':info['AccountID'],'inst':info['EducationInstitution'],'title':info['EducationTitle']}
            cur.execute(query,values)
            conn.commit()
            count = cur.rowcount
            dump = {'Message': 'Record inserted successfully into DB'}
            message = [dump['Message']]
            print(dump)
            return message
        except(Exception, psycopg2.Error) as error:
            if(conn):
                dump = {'Message':'Failed to insert record into mobile table','Detail':error}
                message = [dump['Message'],dump['Detail']]
                print(dump)
                return message
        finally:
            DBManager.close(conn)

    def insertToWorkplace(info):
        conn = DBManager.connect()
        #create a cursor to execute command
        try:
            cur = conn.cursor()
            query = """ INSERT INTO workplace(account_id,workplace1,workplace2) VALUES (%(id)s,%(w1)s,%(w2)s) """
            values = {'id':info['AccountID'],'w1':info['Workplace1'],'w2':info['Workplace2']}
            cur.execute(query,values)
            conn.commit()
            count = cur.rowcount
            dump = {'Message': 'Record inserted successfully into DB'}
            message = [dump['Message']]
            print(dump)
            return message
        except(Exception, psycopg2.Error) as error:
            if(conn):
                dump = {'Message': 'Failed to insert record into mobile table','Detail':error}
                message = [dump['Message'],dump['Detail']]
                print(dump)
                return message
        finally:
            DBManager.close(conn)

    def readFromAccount(idSearch):
        conn = DBManager.connect()
        try:
            cur = conn.cursor()
            query = """ SELECT * FROM account WHERE account_id = %(id)s """
            values = {'id': idSearch}
            cur.execute(query,values)
            if(cur.rowcount == 0):
                dump = {'Feedback':'Invalid AccountID','AccountID':idSearch}
                message = [dump['Feedback'],dump['AccountID']]
                print(dump)
                return message
            else:
                result = cur.fetchall()
                for row in result:
                    dump = {'AccountID':row[0],'AccountName':row[1],'AccountTitle':row[2],'AccountRegion':row[3]}
                message = [dump['AccountID'],dump['AccountName'],dump['AccountTitle'],dump['AccountRegion']]
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
    def readFromEducation(idSearch):
        conn = DBManager.connect()
        try:
            cur = conn.cursor()
            query = """ SELECT * FROM education WHERE account_id = %(id)s """
            values = {'id': idSearch}
            cur.execute(query,values)
            if(cur.rowcount == 0):
                dump = {'Feedback':'Invalid AccountID','AccountID':idSearch}
                message = [dump['Feedback'],dump['AccountID']]
                print(dump)
                return message
            else:
                result = cur.fetchall()
                for row in result:
                    dump = {'AccountID':row[0],'EducationInstitution':row[1],'EducationTitle':row[2]}
                message = [dump['AccountID'],dump['EducationInstitution'],dump['EducationTitle']]
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
    def readFromWorkplace(idSearch):
        conn = DBManager.connect()
        try:
            cur = conn.cursor()
            query = """ SELECT * FROM workplace WHERE account_id = %(id)s """
            values = {'id': idSearch}
            cur.execute(query,values)
            if(cur.rowcount == 0):
                dump = {'Feedback':'Invalid AccountID','AccountID':idSearch}
                message = [dump['Feedback'],dump['AccountID']]
                print(dump)
                return message
            else:
                result = cur.fetchall()
                for row in result:
                    dump = {'AccountID':row[0],'Workplace1':row[1],'Workplace2':row[2]}
                message = [dump['AccountID'],dump['Workplace1'],dump['Workplace2']]
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
        

    



        
