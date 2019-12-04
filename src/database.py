import mysql.connector
from mysql.connector import errorcode

# User Mark created, password MarkMark123!
# User Admin created, password Admin123!
class Database:
    input = None
    def __init__(self, hostname, user, password, database):
        self.user = user
        self.password = password
        self.database = database
        self.host = hostname


    def connect(self):
        config = {
        'user': str(self.user),
        'password': str(self.password),
        'host': str(self.host),
        'database': str(self.database)
        }
        # need to change here when cant login
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

    # verify if the plate is in database
    # work with recognition
    def verify(self, content) -> bool:
        self.cursor.execute(""
                           "SELECT *"
                           "FROM Plates "
                           "WHERE num='%s'" % content)
        result = self.cursor.fetchall()
        if (len(result) > 0):
            return True
        return False


    def add(self, num, make, model, car_color, owner_name, age, room):
        query = "INSERT INTO Plates VALUES ('{}','{}','{}','{}','{}',{},'{}');".format(num, make, model, car_color, owner_name, age, room)
        self.cursor.execute(query)
        self.connection.commit()
        return True

    def delete(self, plate):
        query = "DELETE FROM Plates WHERE num='{}'".format(plate)
        self.cursor.execute(query)
        self.connection.commit()
        return True

    def update(self, old, num, make, model, car_color, owner_name, age, room):
        query = "UPDATE Plates SET num='{}', make='{}', model='{}', car_color='{}', owner_name='{}', age={}, room='{}'" \
                "WHERE num='{}';".format(num, make, model, car_color, owner_name, age, room, old)
        self.cursor.execute(query)
        self.connection.commit()
        return True

    def add_user(self, username, password):
        query = "CREATE USER '{}'@'localhost' IDENTIFIED BY '{}';".format(username, password)
        print(query)
        self.cursor.execute(query)
        self.connection.commit()
        return True
