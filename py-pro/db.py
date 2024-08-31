import mysql.connector as my

con = my.connect(
    host='localhost',
    user='root',
    password='mysql@123',
    database='ecommerce'
)

cr = con.cursor()
cr.execute("show databases")
databases = cr.fetchall()

# Print the list of databases
print("Databases:")
for db in databases:
    print(db)

# a = int(input("enter id"))
# b = input("enter name")
# c = input("enter category")
# d = input("enter stock")
# data = [a,b,c,d]
# cr.execute("insert into product values(%s,%s,%s,%s)",data)
data = [[106, 'xyz', 'null', 10], [
    107, 'abc', 'null', 20], [108, 'pqr', 'null', 30]]
cr.executemany("insert into product values(%s,%s,%s,%s)", data)
con.commit()
