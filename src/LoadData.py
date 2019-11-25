import mysql.connector
import csv

config = {
'user': 'root',
'password': '',
'host': '127.0.0.1',
'database': 'Plates'
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

file = open('../data/demo_data.txt', 'r')
reader = csv.reader(file)
for row in reader:
    query = "INSERT INTO Plates VALUES ('{}','{}','{}','{}','{}',{},'{}');".format(row[0].strip(),row[1].strip(),row[2].strip(),row[3].strip(),row[4].strip(),row[5].strip(),row[6].strip())
    print(query)
    cursor.execute(query)
    connection.commit()
