import mysql.connector
# Replace these with your database details
host = "localhost"
user = "root"
password = "avishkar123"
database = "a1"

# Create a connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

def display () :
    query = "SELECT * FROM Student order by prn desc"
    cursor.execute(query)
    results = cursor.fetchall()
    
    for row in results:
        for it in row : 
            print(it,end=" ")
        print()



def insert(d) :
    query = "INSERT into Student (prn,name,age) values (%s, %s, %s)"
    data=d
    cursor.execute(query,data)
    connection.commit()

def delete(p):
    query="DELETE from Student where prn=%s"
    data=(p,)
    cursor.execute(query,data)
    connection.commit()



# # Example SELECT query
# query = "SELECT * FROM Student order by prn desc"
# cursor.execute(query)

# # Fetch the results
# results = cursor.fetchall()

# # Iterate through the results
# for row in results:
#     for it in row : 
#         print(it,end=" ")
#     print()


# #Query 2 : 
# query = "SELECT prn from Student"
# cursor.execute(query)
# results = cursor.fetchall()

# for row in results : 
#     print(row[0])


display()
#  insert((21610088,"Amir Khan",24))
print("***************************************************")
display()
print("***************************************************")
delete(21610090)
display()










cursor.close()
connection.close()
