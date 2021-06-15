import sqlite3
connection = sqlite3.connect("state_numb_cars_kg.db")
c = connection.cursor()

c.execute("CREATE TABLE cars_base (ID int, Model text, Car_numb varchar(10), Color text")
c.execute("INSERT INTO persons VALUES ('1', 'HONDA Avancier', '8951BC', 'White')")
# c.execute("INSERT INTO persons VALUES ('John', 'Doe')")
# a = input('Name ')
# b = input('Last Name ')
# c.execute(f"INSERT INTO persons VALUES ('{a}', '{b}')")
connection.commit()

# fname = ["Gofaslf", "kfjaksfja", "sfkjaqrwf"]
# lname = ["Gofasdlf", "kfjaksadffja", "sffafkjaqrwf"]
# for i, a in zip(fname, lname):
#     c.execute("INSERT INTO persons VALUES (?, ?)", (i, a))
#     connection.commit()

for row in c.execute("SELECT * FROM cars_base;"):
    print(row)

# #name = input("Namn: ")
# #for row in c.execute("SELECT * FROM persons WHERE fname=?", (name,)):
# #    print(row)

# connection.close()