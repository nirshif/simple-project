import sqlite3

conn = sqlite3.connect(r'C:\Users\mer student\ssqqll1.db')
# #conn.execute("INSERT INTO COMPANY VALUES (9,'James', 44, 'Norway', 5000.00 );")
#
# id=10
# name='James'
# age=45
# address='Houston'
# salary=5000
# conn.execute(f"INSERT INTO COMPANY VALUES ({id}, '{name}', {age}, '{address}', {salary});")

cursor=conn.execute("SELECT * FROM COMPANY")
for worker in cursor:
    print(f"id={worker[0]}, name={worker[1]}, age={worker[2]}, address={worker[3]}, salary={worker[4]}")
    conn.execute((f"UPDATE COMPANY SET SALARY = {worker[4]+10} WHERE ID = {worker[0]} "))
    conn.commit()

print()
