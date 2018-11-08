import csv
import sqlite3
import sys

input_file = sys.argv[1]

con = sqlite3.connect(':memory:')
query = """CREATE TABLE IF NOT EXISTS sales
            (customer VARCHAR(20),
            product VARCHAR(20),
            amount FLOAT,
            date DATE);"""
con.execute(query)
con.commit()

data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenney Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephan Randolph', 'Computer', 679.40, '2014-02-20')]
for tuple in data:
    print(tuple)
statement = "INSERT INTO sales VALUES(?,?,?,?)"
con.executemany(statement, data)
con.commit()

file_reader = csv.reader(open(input_file, 'r'), delimiter = ',')
header = next(file_reader, None)     # header 건너뛰고 data만 접근하기 위하여
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;", data)
con.commit()

cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range (len(row)):
        output.append(str(row[column_index]))
    print(output)
