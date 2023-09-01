import sqlite3 as sq
with sq.connect('student') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby TEXT,
    name TEXT,
    surname TEXT,
    birth INTEGER,
    scores INTEGER
    )''')
    cur.execute('''INSERT INTO student(hobby, name, surname, birth, scores) VALUES 
    ('Играть в волейбол', 'Екатерина', 'Александрова', 1997, 10),
    ('Рисовать', 'Игорь', 'Макаров', 2000, 15),
    ('Фотографировать', 'Иван', 'Лебедев', 2001, 9),
    ('Делать оригами', 'Мария', 'Медведева', 1999, 12),
    ('Путешествовать', 'Андрей', 'Лавринович', 2003, 10),
    ('Изучать астрологию', 'Михаил', 'Севастьянов', 1998, 16),
    ('Играть в компьютерные игры', 'Тимофей', 'Романов', 2001, 7),
    ('Программирование', 'Асыл', 'Сулайманова', 2002, 18),
    ('Танцевать', 'Диана', 'Кульмухамбетова', 1997, 17),
    ('Играть в футбол', 'Владислав', 'Петров', 2001, 8)
    ''')
    cur.execute('''SELECT * FROM student WHERE LENGTH(surname) > 10''')
    item = cur.fetchall()
    for i in item:
        print(i)
    cur.execute('''UPDATE student SET name = 'genius' WHERE scores > 10''')
    cur.execute('''SELECT * FROM student WHERE name == 'genius' ''')
    item = cur.fetchall()
    for i in item:
        print(i)
    cur.execute('''DELETE FROM student WHERE id %2 = 0''')