import pymysql

def connect_db():
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='khushi_db', charset='utf8')
        print('DB connected')
        return connection
    except:
        print('DB connection failed')

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('Error while disconnecting DB')

def create_db():
    connection = connect_db()
    query = 'create database IF NOT EXISTS khushi_db;'
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    connection.commit()
    disconnect_db(connection)

def create_table():
    connection = connect_db()
    query = "create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(32) not null, gender char check(gender in ('m','M','F','f')),location varchar(32),dob datetime);"
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    print('Table created')
    connection.commit()
    disconnect_db(connection)

def read_person_details():
    name=input('Enter name: ')
    gender = input('Enter gender: ')[0]
    location = input('Enter location: ')
    dob = input('Enter DOB(yyyy/mm/dd): ')
    return(name, gender, location, dob)

def insert_row():
    person = read_person_details()
    query = 'insert into persons(name,gender,location,dob) values (%s,%s,%s,%s);'
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query, person)
    print('Row created')
    connection.commit()
    disconnect_db(connection)

create_db()
create_table()
insert_row()

