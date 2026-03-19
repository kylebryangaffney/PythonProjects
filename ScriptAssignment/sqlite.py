import sqlite3

connection = sqlite3.connect("test.db")

# with connection:
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
#                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
#                    col_fname TEXT, \
#                    col_lname TEXT, \
#                    col_email TEXT \
#                    )")
#     connection.commit()
# connection.close()
 

# with connection:
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
#                    ("Robert", "Smithington", "bsmith@hotmail.com"))
    
#     connection.commit()
# connection.close()



# with connection:
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
#                    ("Alex", "Waterford", "awater@hotmail.com"))
#     cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
#                    ("Dexter", "Gordo", "dgordo@aol.com"))
#     cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
#                    ("Amelia", "Airheart", "aair@google.com"))
#     cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
#                    ("Sara", "McMahon", "smchaone@work.com"))
#     cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
#                    ("Sandy", "Cheeks", "scheeks@aol.com"))
    
#     connection.commit()
# connection.close()


with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Alex'")
    var_person = cursor.fetchall()

    message = ""
    for element in var_person:
        message = f"First Name {element[0]}\nLast Name: {element[1]}\nEmail: {element[2]}"
    connection.commit()
    print(message)
    
connection.close()

