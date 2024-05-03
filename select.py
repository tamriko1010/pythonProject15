import sqlite3
from univer import University

db = sqlite3.connect('my_base.db')
cursor = db.cursor()

# Запросы

u1 = University('Urban')
u1.get_students()
u1.get_students('Assembler')
u1.get_students('Python')

db.close()