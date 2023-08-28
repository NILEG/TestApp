from sqlite3 import connect
class Database:
    db=None
    cursor=None
    @staticmethod
    def connect():
        Database.db=connect("optoDatabase.db")
        Database.cursor=Database.db.cursor()
        Database.cursor.execute("CREATE TABLE IF NOT EXISTS users(email text PRIMARY KEY, password text NOT NULL, name text NOT NULL)")
        Database.cursor.execute("CREATE TABLE IF NOT EXISTS entries(entry_id integer PRIMARY KEY, email text NOT NULL, problem_name text NOT NULL)")
        Database.cursor.execute("CREATE TABLE IF NOT EXISTS data_table(id integer PRIMARY KEY, entry_id integer NOT NULL, email text NOT NULL, disease text NOT NULL, percentage text NOT NULL)")
        Database.db.commit()
        print("Connected Successfully")

    @staticmethod
    def insert_into_users(email, password, name):
        sql = "INSERT INTO users (email, password, name) VALUES(?,?,?)"
        val = (f"{email}", f"{password}", f"{name}")
        Database.cursor.execute(sql, val)
        Database.db.commit()

    @staticmethod
    def insert_into_entries(email, problem_name):
        sql = "INSERT INTO entries (email, problem_name) VALUES(?,?)"
        val = (f"{email}", f"{problem_name}")
        Database.cursor.execute(sql, val)
        Database.db.commit()
    @staticmethod
    def insert_into_data_table(entry_id, email, disease, percentage):
        sql = "INSERT INTO data_table (entry_id, email, disease, percentage) VALUES(?,?,?,?)"
        val = (f"{entry_id}", f"{email}",f"{disease}", f"{percentage}")
        Database.cursor.execute(sql, val)
        Database.db.commit()

    @staticmethod
    def isValid(email):
        sql = f"SELECT * FROM users WHERE email='{email}'"
        Database.cursor.execute(sql)
        result = Database.cursor.fetchall()
        if (result):
            return False
        else:
            return True

    @staticmethod
    def isExist(email, password):
        sql = f"SELECT * FROM users WHERE email='{email}' and password='{password}'"
        Database.cursor.execute(sql)
        result = Database.cursor.fetchall()
        if (result):
            return True
        else:
            return False

    @staticmethod
    def get_last_entryid(email):
        sql = f"SELECT * FROM entries WHERE email='{email}'"
        Database.cursor.execute(sql)
        result = Database.cursor.fetchall()[-1]
        return result[0]

    @staticmethod
    def get_data(email, entry_id):
        sql = f"SELECT * FROM data_table WHERE entry_id='{entry_id}' and email='{email}'"
        Database.cursor.execute(sql)
        result = Database.cursor.fetchall()
        return result
    @staticmethod
    def get_all_entries(email):
        sql = f"SELECT * FROM entries WHERE email='{email}'"
        Database.cursor.execute(sql)
        result = Database.cursor.fetchall()
        return result

    @staticmethod
    def getUserInfo(email):
        sql = f"SELECT * FROM users WHERE email='{email}'"
        Database.cursor.execute(sql)
        result = Database.cursor.fetchall()[0]
        return result

    @staticmethod
    def update_information(name, email, password):
        sql="UPDATE users SET password=?, name=? WHERE email=?"
        val = (f"{password}", f"{name}", f"{email}")
        Database.cursor.execute(sql, val)
        Database.db.commit()



