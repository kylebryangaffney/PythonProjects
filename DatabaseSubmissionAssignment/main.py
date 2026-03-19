import sqlite3

# Function to build the table in the database with an auto-increment ID and a filename column
def build_table(tbl_name, tbl_col_name, connection):
    with connection:
        cursor = connection.cursor()
        # Create the table only if it doesn't already exist
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {tbl_name}( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    {tbl_col_name} TEXT \
                    )")
        connection.commit()


# Function to check each file in the list, insert .txt files into the DB, and print them
def addToDatabase(fileList, tbl_name, col_name, connection):
    for file in fileList:
        # Only process files that end with the .txt extension
        if file.endswith(".txt"):
            with connection:
                cursor = connection.cursor()
                # (file,) must be a tuple — a bare (file) is just a string
                cursor.execute(f"INSERT INTO {tbl_name} ({col_name}) VALUES (?)", (file,))
                print(file)


# File names to check
fileList = ("information.docx", "Hello.txt", "myImage.png", \
            "myMovie.mpg", "World.txt", "data.pdf", "myPhoto.jpg")

table_name = "tbl_files"
col_name = "col_fileName"

# Open the database connection (creates test.db if it doesn't exist)
connection = sqlite3.connect("test.db")

if __name__ == "__main__":
    build_table(table_name, col_name, connection)          # Build the table first
    addToDatabase(fileList, table_name, col_name, connection)  # Then insert and print .txt files
    connection.close()
