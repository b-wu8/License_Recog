import mysql.connector

# User Mark created, password MarkMark123!
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
        'database': str(self.database),
        'raise_on_warnings': True,}
        try:
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor()
            return True
        except:
            return False

    # search plates, general searches
    def search(self, content):
        self.cursor.execute(""
                           "SELECT * "
                           "FROM Plates "
                           "WHERE num='%s' or car_color='%s' or owner_name='%s' or room='%s' or make='%s'"%(content, content, content, content, content))
        result = self.cursor.fetchall()
        print(result)
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


    # control access, S, A, B, C
    # add and delete car plates
    def add(self):
        print("add")
    def delete(self):
        print("delete")

    # add and delete user
    def manage_user(self):
        return
