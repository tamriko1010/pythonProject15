import sqlite3
from univer import University

db = sqlite3.connect('my_base.db')
cursor = db.cursor()

# Создаем таблицы 'students' и 'grades'

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY,
name STR,
age INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
id INTEGER PRIMARY KEY,
student_id INTEGER,
subject STR,
grade FLOAT,
FOREIGN KEY (student_id) REFERENCES students(id)
)
''')
# Добавляем студентов и зачеты
u1 = University('Urban')

u1.add_student('Ivan', 26)
u1.add_student('Ilya', 24)
u1.add_student('Denis', 28)
u1.add_student('Andrey', 32)


u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)
u1.add_grade(3, 'Python', 4.5)
u1.add_grade(4, 'PHP', 4.2)
u1.add_grade(1, 'PHP', 4.0)
u1.add_grade(2, 'Python', 4.5)
u1.add_grade(3, 'PHP', 3.7)
u1.add_grade(4, 'Python', 3.2)


# Просмотр базы данных

cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT * FROM grades")
result = cursor.fetchall()
for row in result:
    print(row)

db.close()