import sqlite3


## connectt to sqlite
connection=sqlite3.connect("student.db")

## create object to insert record,create table
cursor=connection.cursor()

##create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## insert some more records
cursor.execute('''Insert Into STUDENT values('KRISH','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Jhon ','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Jacob','Devops','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','Devops','A',35)''')

##Display all the records
print("The inserted records are ")
data=cursor.execute('''Select * from STUDENT''')
for row  in data:
    print(row)
    
## Commit your changes in database

connection.commit()
connection.close()    
