import random
import sqlite3


name = ['Oliver', 'George', 'Arthur', 'Leo', 'Muhammad', 'Oscar', 'Harry', 'Noah', 'John', 'Jack']
lastname = ['BROWN', 'SMITH', 'JONES', 'TAYLOR', 'WILSON',
            'DAVIES', 'EVANS', 'JOHNSON', 'THOMAS', 'ROBERTS',
            'WALKER', 'WRIGHT', 'THOMPSON', 'ROBINSON', 'WHITE']


def create_name():
    return str(name[random.randint(0, len(name)-1)])


def create_lastname():
    return str(lastname[random.randint(0, len(lastname)-1)])


db = sqlite3.connect('server.db')
sql = db.cursor()
sql.execute("DROP TABLE IF EXISTS People")
sql.execute('''CREATE TABLE IF NOT EXISTS People(
    name VARCHAR(40),
    surname VARCHAR(40),
    age INT
    )''')


def insert_person():
    sql.execute(f"INSERT INTO People VALUES(?, ?, ?)", (create_name(), create_lastname(), random.randint(10, 70)))
    db.commit()


def print_people():
    print('\nList of people:')
    list_of_users = sql.execute(
        "SELECT * FROM People WHERE age > 25 ORDER BY age DESC"
    )
    for person in list_of_users:
        print(person)


def print_workers():
    list_of_users = sql.execute(
        "SELECT * FROM Workers WHERE age > 25 ORDER BY age DESC"
    )
    for person in list_of_users:
        print(person)


def print__(list_of_people):
    for element in list_of_people:
        print(element)


def print_join():
    while True:
        n = int(input('\n1-Inner Join\n2-Left Outer Join\nEnter: '))
        if n == 1:
            print('Inner Join:')
            list_of_people = sql.execute(
                "SELECT * FROM People INNER JOIN Workers ON people.age = workers.age"
            )
            print__(list_of_people)
        if n == 2:
            print('Left Outer Join:')
            list_of_people = sql.execute(
                "SELECT * FROM People INNER JOIN Workers ON people.age = workers.age"
            )
            print__(list_of_people)
        else:
            break


def average_age():
    avg = sql.execute("SELECT AVG(age) FROM People")
    for elem in avg:
        print('Average age = ', *elem)


def min_age():
    print('\nMinimal age:')
    minimal_age = sql.execute("SELECT surname, MIN(age) FROM People \
        GROUP BY surname \
        HAVING age > 30")
    for person in minimal_age:
        print(person)


def update():
    sql.execute("UPDATE People SET name = '-' WHERE age > 50 ")


def delete():
    sql.execute("DELETE FROM People WHERE age < 40")


def alter():
    sql.execute("ALTER TABLE People ADD COLUMN position VARCHAR(20)")
    print_people()
    sql.execute("ALTER TABLE People DROP COLUMN position")
