import sqlite3

db = sqlite3.connect('my_base.db')
cursor = db.cursor()
class University():
    def __init__(self, nameun):
        self.name = nameun

    def add_student(self, name, age):   # добавить студента
        self.name = name
        self.age = age
        cursor.execute("INSERT INTO students (name, age)"
                       f"VALUES ('{self.name}', '{self.age}')")
        db.commit()

    def add_grade(self, student_id, subject, grade):     # добавить зачет
        self.student_id = student_id
        self.subject = subject
        self.grade = grade
        cursor.execute("INSERT INTO grades (student_id, subject, grade)"
                       f"VALUES ('{self.student_id}','{self.subject}', '{self.grade}')")
        db.commit()

    def get_students(self, subject=None):     # выбрать зачеты по заданному предмету
        self.subject = subject
        print(self.subject)
        if self.subject != None:
            cursor.execute("SELECT students.name, students.age, grades.subject,"
                           " grades.grade FROM students JOIN grades"
                           " ON grades.student_id = students.id WHERE "
                           f"grades.subject = '{self.subject}';")
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(row)
            else:
                print('Нет такого предмета')

        else:
            print('Не задан предмет')

