import sqlite3
currentUserID = ""
connection = sqlite3.connect("LibraryProject.db")
cursor = connection.cursor()

if __name__ == '__main__':
    from Classes import Admin
    from Classes import Menu

    Admin.createAllTables()
    # Admin.resetAllTables()

    Menu.beforeLoginMenu()