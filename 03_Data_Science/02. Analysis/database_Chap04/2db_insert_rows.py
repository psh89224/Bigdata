import csv
import sqlite3
import sys

input_file = sys.argv[1]

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
                    (Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE);"""
c.execute(create_table)
con.commit()

file_reader = csv.reader(open(input_file, 'r'), delimiter = ',')
header = next(file_reader, None)     # header 건너뛰고 data만 접근하기 위하여
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?,?,?,?,?);", data)
con.commit()

output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
