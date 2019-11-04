import mysql.connector

# User Mark created, password MarkMark123!
class Database:
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
            self.connect = mysql.connector.connect(**config)
            return True
        except:
            return False

    # search plates
    def search(self, content):
        with self.connection.cursor() as cursor:
            cursor.execute(""
                           "SELECT * "
                           "FROM Plates"
                           "WHERE num='%s' or car_color='%s' or owner_name='%s' or room='%s' or make='%s'" % content)
            result = cursor.fetchall()
            print(result)

    def verify(self, content) -> bool:
        with self.connection.cursor() as cursor:
            cursor.execute(""
                           "SELECT *"
                           "FROM Plates"
                           "WHERE num='%s" % content)
            result = cursor.fetchall()
            value, = result
            return value




    # work on new window for search and verify, add and delete
    # add and delete car plates
    def add(self):
        return
    def delete(self):
        return

    # add and delete user
    def manage_user(self):
        return
