import sqlite3
connect = sqlite3.connect('school.db') 
cur = connect.cursor()

cur.execute("DROP TABLE IF EXISTS classes")
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS subjects")
cur.execute("DROP TABLE IF EXISTS marks")

cur.execute("PRAGMA foriegn_keys=on")

query1 = "CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY, class INT, num_of_stud INT, teacher TEXT, age INT)"
query2 = "CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, familia TEXT, imya TEXT, otchestvo TEXT, id_classes INT, gender TEXT, FOREIGN KEY (id_classes) REFERENCES classes (id) ON UPDATE CASCADE)"
query3 = "CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, subject TEXT)" 
query4 = "CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, mark INT, id_students INT, id_subjects INT, FOREIGN KEY (id_subjects) REFERENCES subjects (id) ON UPDATE CASCADE, FOREIGN KEY (id_students) REFERENCES student (id) ON UPDATE CASCADE)"

#query3 = "CREATE TABLE IF NOT EXISTS  (Id INT, class INT, num_of_stud INT, teacher INT,)"
cur.execute(query1)
cur.execute("INSERT INTO classes VALUES(1, 9, 21, 'Smirnov', 43)")
cur.execute("INSERT INTO classes VALUES(2, 9, 22, 'Petrova', 29)")
cur.execute("INSERT INTO classes VALUES(3, 10, 19, 'Popov', 37)")
cur.execute("INSERT INTO classes VALUES(4, 8, 24, 'Tarasova', 31)")
cur.execute("INSERT INTO classes VALUES(5, 1, 27, 'Zuev', 44)")

cur.execute(query2)
cur.execute("INSERT INTO students VALUES(11, 'Kotov', 'Andrew', 'Alexandrovich', 1, 'male')")
cur.execute("INSERT INTO students VALUES(12, 'Sobolev', 'Petya', 'Viktorovich', 2, 'male')")
cur.execute("INSERT INTO students VALUES(13, 'Frolov', 'Anotoliy', 'Vyachaslavovich', 3, 'male')")
cur.execute("INSERT INTO students VALUES(14, 'Volkova', 'Liza', 'Vasilevna', 4, 'female')")
cur.execute("INSERT INTO students VALUES(15, 'Ushinskiy', 'Denis', 'Vladimirovich', 5, 'male')")

cur.execute(query3)
cur.execute("INSERT INTO subjects VALUES(601, 'Russian language')")
cur.execute("INSERT INTO subjects VALUES(602, 'English language')")
cur.execute("INSERT INTO subjects VALUES(603, 'Math')")
cur.execute("INSERT INTO subjects VALUES(604, 'PE')")
cur.execute("INSERT INTO subjects VALUES(605, 'Physics')")

cur.execute(query4)
cur.execute("INSERT INTO marks VALUES(112, 2, 11, 601)")
cur.execute("INSERT INTO marks VALUES(113, 3, 12, 602)")
cur.execute("INSERT INTO marks VALUES(114, 4, 13, 603)")
cur.execute("INSERT INTO marks VALUES(115, 4, 14, 604)")
cur.execute("INSERT INTO marks VALUES(116, 5, 15, 605)")

cur.execute("SELECT * FROM classes")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT * FROM students")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT * FROM subjects")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT * FROM marks")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

connect.commit()
connect.close()


