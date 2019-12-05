import mysql.connector
from mysql.connector import errorcode

# User Mark created, password MarkMark123!
# User admin created, password Admin123!
class Database:
    input = None
    def __init__(self, hostname, user, password, database):
        self.user = user
        self.password = password
        self.database = database
        self.host = hostname

    # connect to local database
    def connect(self):
        config = {
        'user': str(self.user),
        'password': str(self.password),
        'host': str(self.host),
        'database': str(self.database)
        }
        try:
            self.connection = mysql.connector.connect(**config)
            if self.connection.is_connected():
                self.cursor=self.connection.cursor()
                return True
            else:
                print("Something went wrong")
                return False
        except mysql.connector.Error as err:
            if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something wrong with credentials")
                return False
            else:
                print(err)
            return False

    # search plates, general searches
    def search(self, content):
        self.cursor.execute(""
                           "SELECT * "
                           "FROM Plates "
                           "WHERE num='{}' or car_color='{}' or owner_name='{}' or room='{}' or make='{}'".format(content, content, content, content, content))
        result = self.cursor.fetchall()
        return result

    # add new plates
    def add(self, num, make, model, car_color, owner_name, age, room):
        query = "INSERT INTO Plates VALUES ('{}','{}','{}','{}','{}',{},'{}');".format(num, make, model, car_color, owner_name, age, room)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except mysql.connector.errorcode as err:
            print(err)
            return False

    # remove existing plates
    def delete(self, plate):
        query = "DELETE FROM Plates WHERE num='{}'".format(plate)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except mysql.connector.errorcode as err:
            print(err)
            return False

    # change existing plate info
    def update(self, old, num, make, model, car_color, owner_name, age, room):
        query = "UPDATE Plates SET num='{}', make='{}', model='{}', car_color='{}', owner_name='{}', age={}, room='{}'" \
                "WHERE num='{}';".format(num, make, model, car_color, owner_name, age, room, old)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except mysql.connector.errorcode as err:
            print(err)
            return False

    # add new user with access control
    def add_user(self, username, password, edit):
        query = "CREATE USER '{}'@'localhost' IDENTIFIED BY '{}'; ".format(username, password)
        query += "GRANT SELECT ON Plates.Plates TO '{}'@'localhost'; ".format(username)
        if edit:
            query += "GRANT UPDATE, INSERT, DELETE ON Plates.Plates TO '{}'@'localhost'; ".format(username)

        try:
            self.cursor.execute(query)
            return True
        except mysql.connector.errorcode as err:
            print(err)
            return False

    # remove existing user
    def remove_user(self, user):
        query = "DROP USER '{}'@'localhost';".format(user)
        try:
            self.cursor.execute(query)
            return True
        except mysql.connector.errorcode as err:
            print(err)
            return False

    # change existing user permissions
    def edit_user(self, user, edit):
        if user=='root':
            return False
        try:
            query = "SHOW GRANTS FOR '{}'@'localhost';".format(user)
            self.cursor.execute(query)
            result = self.cursor.fetchall()[1][0]
            if 'INSERT' not in result and edit:
                query = "GRANT UPDATE, INSERT, DELETE ON Plates.Plates TO '{}'@'localhost'; ".format(user)
                self.cursor.execute(query)
            elif 'INSERT' in result and not edit:
                query = "REVOKE UPDATE, INSERT, DELETE ON Plates.Plates FROM '{}'@'localhost'; ".format(user)
                self.cursor.execute(query)
            return True
        except mysql.connector.errorcode as err:
            print(err)
            return False



