from main import currentUserID
from main import connection
from main import cursor
import uuid

class Admin:
    @staticmethod
    def createAllTables():
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Users(id TEXT PRIMARY KEY, firstName TEXT, lastName TEXT, userName TEXT, password TEXT, address TEXT, creditCardNumber TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Books(id TEXT PRIMARY KEY, ISBN TEXT, title TEXT, author TEXT, genre TEXT, stock INTEGER)")
        cursor.execute("CREATE TABLE IF NOT EXISTS Carts(id TEXT PRIMARY KEY, bookID TEXT, userID TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS OrderHistory(id TEXT PRIMARY KEY, bookID TEXT, userID TEXT)")
        connection.commit()

    @staticmethod
    def resetUsersTable():
        cursor.execute("DELETE FROM Users")
        connection.commit()

    @staticmethod
    def resetBooksTable():
        cursor.execute("DELETE FROM Books")
        Admin.createBook(str(uuid.uuid1()), '978-1734554908', 'Computer Science Principles: The Foundational Concepts of Computer Science', 'Mr. Kevin P Hare', 'Computer Science', 10)
        Admin.createBook(str(uuid.uuid1()), '978-1951204006', 'A Programmer\'s Guide to Computer Science','Dr. William M Springer II', 'Computer Science', 10)
        Admin.createBook(str(uuid.uuid1()), '978-1119293491', 'Calculus For Dummies', 'Mark Ryan', 'Math', 10)
        Admin.createBook(str(uuid.uuid1()), '978-0486457956', 'Advanced Calculus', 'Avner Friedman', 'Math', 10)
        Admin.createBook(str(uuid.uuid1()), '978-1119629900', 'Basic Physics', 'Karl F. Kuhn', 'Physics', 10)
        Admin.createBook(str(uuid.uuid1()), '978-0060935467', 'To Kill a Mockingbird', 'Harper Lee', 'Southern Gothic', 10)
        Admin.createBook(str(uuid.uuid1()), '978-0399501487', 'Lord of the Flies', 'William Golding', 'Fiction', 10)
        Admin.createBook(str(uuid.uuid1()), '978-1954839373', 'Dr. Jekyll and Mr. Hyde', 'Robert Louis Stevenson', 'Fiction', 10)
        Admin.createBook(str(uuid.uuid1()), '978-1451673319', 'Fahrenheit 451', 'Ray Bradbury', 'Fiction', 10)
        Admin.createBook(str(uuid.uuid1()), '978-0062387240', 'Divergent', 'Veronica Roth', 'Fiction', 10)
        connection.commit()

    @staticmethod
    def createBook(id, ISBN, title, author, genre, stock):
        cursor.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)", (id, ISBN, title, author, genre, stock))
        connection.commit()

    @staticmethod
    def resetCartsTable():
        cursor.execute("DELETE FROM Carts")
        connection.commit()

    @staticmethod
    def resetOrderHistoryTable():
        cursor.execute("DELETE FROM OrderHistory")
        connection.commit()

    @staticmethod
    def resetAllTables():
        Admin.resetBooksTable()
        Admin.resetCartsTable()
        Admin.resetOrderHistoryTable()
        Admin.resetUsersTable()

    @staticmethod
    def viewUserTable():
        print("----- Admin: User Table -----")
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()

        if len(users) == 0:
            print("No items have been added to User table")
        else:
            index = 1
            for user in users:
                userID = user[0]
                username = user[3]
                print(str(index) + ". userID: " + userID + ", user name: " + username)
                index += 1

    @staticmethod
    def viewBookTable():
        print("----- Admin: Book Table -----")
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()

        if len(books) == 0:
            print("No items have been added to Book table")
        else:
            index = 1
            for book in books:
                bookID = book[0]
                title = book[2]
                print(str(index) + ". bookID: " + bookID + ", title:" + title)
                index += 1

    @staticmethod
    def viewCartTable():
        print("----- Admin: Cart Table -----")
        cursor.execute("SELECT * FROM Carts")
        carts = cursor.fetchall()

        if len(carts) == 0:
            print("No items have been added to Cart table")
        else:
            index = 1
            for cartItem in carts:
                bookID = cartItem[1]
                userID = cartItem[2]
                print(str(index) + ". " + "bookID: " + bookID + ", userID: " + userID)
                index += 1

    @staticmethod
    def viewOrderHistoryTable():
        print("----- Admin: Order History Table -----")
        cursor.execute("SELECT * FROM OrderHistory")
        histories = cursor.fetchall()

        if len(histories) == 0:
            print("No items have been added to Order History table")
        else:
            index = 1
            for historyItem in histories:
                bookID = historyItem[1]
                userID = historyItem[2]
                print(str(index) + ". " + "userID: " + userID + ", bookID: " + bookID)
                index += 1

class Menu:

    @staticmethod
    def beforeLoginMenu():
        print("----- Main Menu -----")
        print("1. Login")
        print("2. Create account")
        print("3. Exit")
        print("4. (ADMIN) View Users")
        print("5. (ADMIN) View Books")
        print("6. (ADMIN) View Carts")
        print("7. (ADMIN) View Order History")

        option = input()
        valid = False
        if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option == "7":
            valid = True
        while not valid:
            print("Invalid input. Try again.")
            option = input()
            if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option == "7":
                valid = True

        if option == "1":
            User.login()
        elif option == "2":
            User.createAccount()
        elif option == "3":
            cursor.close()
            connection.close()
            exit()
        elif option == "4":
            Admin.viewUserTable()
            Menu.beforeLoginMenu()
        elif option == "5":
            Admin.viewBookTable()
            Menu.beforeLoginMenu()
        elif option == "6":
            Admin.viewCartTable()
            Menu.beforeLoginMenu()
        elif option == "7":
            Admin.viewOrderHistoryTable()
            Menu.beforeLoginMenu()

    @staticmethod
    def afterLoginMenu():
        print("----- Main Menu -----")
        print("1. View all books")
        print("2. View all genres")
        print("3. View shopping cart")
        print("4. View account")

        option = input()
        valid = False
        if option == "1" or option == "2" or option == "3" or option == "4":
            valid = True
        while not valid:
            print("Invalid input. Try again.")
            option = input()
            if option == "1" or option == "2" or option == "3" or option == "4":
                valid = True

        if option == "1":
            Book.getAllBooks()
        elif option == "2":
            Book.getAllGenres()
        elif option == "3":
            Cart.get()
        elif option == "4":
            User.viewAccount()

    @staticmethod
    def exit():
        quit()

class User:

    @staticmethod
    def createAccount():
        print("----- Creating Account -----")
        firstName = input("First name: ")
        lastName = input("Last name: ")
        username = input("Username: ")
        password = input("Password: ")
        address = input("Address: ")
        payment = input("Credit card number: ")

        cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?)", (str(uuid.uuid1()), firstName, lastName, username, password, address, payment))
        connection.commit()
        Menu.beforeLoginMenu()

    @staticmethod
    def login():
        print("----- Logging In -----")
        username = input("Username: ")
        password = input("Password: ")
        cursor.execute("SELECT * FROM Users WHERE userName = (?) AND password = (?)", (username, password,))
        userFetch = cursor.fetchall()

        if len(userFetch) == 1:
            currentUser = userFetch[0][0]
            currentUserID = currentUser[0]
            Menu.afterLoginMenu()
        else:
            print("Error. Please try again.")
            print("1. Go back")
            print("2. Login")

            option = input()
            valid = False
            if option == "1" or option == "2":
                valid = True
            while not valid:
                print("Invalid input. Try again.")
                option = input()
                if option == "1" or option == "2":
                    valid = True

            if option == "1":
                Menu.beforeLoginMenu()
            elif option == "2":
                User.login()

    @staticmethod
    def logout():
        currentUserID = ""
        Menu.beforeLoginMenu()

    @staticmethod
    def delete():
        print("Deleting account " + currentUserID + "\n")
        cursor.execute("DELETE FROM Users WHERE id = ?", (currentUserID,))
        connection.commit()
        User.logout()

    @staticmethod
    def getOrderHistory():
        print("----- Order History -----")
        cursor.execute("SELECT * FROM OrderHistory WHERE userID = ?", (currentUserID,))
        books = cursor.fetchall()

        if len(books) == 0:
            print("No order history")
        else:
            index = 1
            for book in books:
                bookID = book[0]
                cursor.execute("SELECT title FROM Books WHERE id = ?", (bookID,))
                book = cursor.fetchall()[0]
                title = book[0]
                print(str(index) + ". " + title)
                index += 1
        User.viewAccount()

    @staticmethod
    def changeAddress():
        print("Enter new address: ")
        newAddress = input()
        cursor.execute("UPDATE Users SET address = ? WHERE id = ?", (newAddress, currentUserID))
        connection.commit()
        User.viewAccount()

    @staticmethod
    def changePaymentInfo():
        newPaymentInfo = input("Enter new credit card number: ")
        cursor.execute("UPDATE Users SET creditCardNumber = ? WHERE id = ?", (newPaymentInfo, currentUserID))
        connection.commit()
        User.viewAccount()

    @staticmethod
    def viewAccount():
        print("----- Account -----")
        print("1. Go back")
        print("2. View order history")
        print("3. Change address")
        print("4. Change payment info")
        print("5. Logout")
        print("6. Delete account")

        option = input()
        valid = False
        if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6":
            valid = True
        while not valid:
            print("Invalid input. Try again.")
            option = input()
            if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6":
                valid = True

        if option == "1":
            Menu.afterLoginMenu()
        elif option == "2":
            History.get()
        elif option == "3":
            User.changeAddress()
        elif option == "4":
            User.changePaymentInfo()
        elif option == "5":
            User.logout()
        elif option == "6":
            User.delete()

class Book:

    def setStock(self):
        print("TODO: SET STOCK")

    @staticmethod
    def getAllBooks():
        print("----- All Books -----")
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()

        index = 1
        for book in books:
            title = book[2]
            print(str(index) + ". " + title)
            index += 1
        print("\n1. Go back")
        print("2. Add book to cart")

        option = input()
        valid = False
        if option == "1" or option == "2":
            valid = True
        while not valid:
            print("Invalid input. Try again.")
            option = input()
            if option == "1" or option == "2":
                valid = True

        if option == "1":
            Menu.afterLoginMenu()
        elif option == "2":
            bookIndex = input("Book #:")
            book = books[int(bookIndex) - 1]
            bookID = book[0]
            Cart.add(bookID)
            Menu.afterLoginMenu()

    @staticmethod
    def getAllGenres():
        print("----- All Genres -----")
        genres = cursor.execute("SELECT DISTINCT genre FROM Books")
        index = 1
        for genre in genres:
            genreName = genre[0]
            print(str(index) + ". " + genreName)
            index += 1

        print("\n1. Go back")
        print("2. See all books for specific genre")

        option = input()
        valid = False
        if option == "1" or option == "2":
            valid = True
        while not valid:
            print("Invalid input. Try again.")
            option = input()
            if option == "1" or option == "2":
                valid = True

        if option == "1":
            Menu.afterLoginMenu()
        elif option == "2":
            genre = input("Genre #: ")
            Book.getBooksInGenre(genre)

    @staticmethod
    def getBooksInGenre(genre):
        print("----- All Books for ", genre, "-----")
        print("TODO: GET BOOKS FOR genre FROM BOOKS TABLE")
        print("1. Go back")
        print("2. Add book to cart")

        option = input()
        valid = False
        if option == "1" or option == "2":
            valid = True
        while not valid:
            print("Invalid input. Try again.")
            option = input()
            if option == "1" or option == "2":
                valid = True

        if option == "1":
            Book.getAllGenres()
        if option == "2":
            book = input("Book #: ")
            Cart.add(book)

class Cart:

    @staticmethod
    def get():
        print("----- Shopping Cart -----")
        cursor.execute("SELECT * FROM Carts WHERE userID = ?", (currentUserID,))
        books = cursor.fetchall()

        if len(books) == 0:
            print("No books in cart")
        else:
            index = 1
            for book in books:
                bookID = book[1]
                cursor.execute("SELECT title FROM Books WHERE id = ?", (bookID,))
                book = cursor.fetchall()[0]
                title = book[0]
                print(str(index) + ". " + title)
                index += 1

            print("\n1. Go back")
            print("2. Remove book from cart")
            print("3. Checkout")

            option = input()
            valid = False
            if option == "1" or option == "2" or option == "3":
                valid = True
            while not valid:
                print("Invalid input. Try again.")
                option = input()
                if option == "1" or option == "2" or option == "3":
                    valid = True

            if option == "1":
                Menu.afterLoginMenu()
            elif option == "2":
                bookIndex = input("Book #: ")
                book = books[int(bookIndex) - 1]
                cartID = book[0]
                Cart.remove(cartID)
            elif option == "3":
                Cart.checkout()

    @staticmethod
    def add(bookID):
        cursor.execute("INSERT INTO Carts VALUES (?, ?, ?)", (str(uuid.uuid1()), bookID, currentUserID))
        connection.commit()

    @staticmethod
    def remove(cartID):
        cursor.execute("DELETE FROM Carts WHERE userID = ? AND id = ?", (currentUserID, cartID))
        connection.commit()
        Cart.get()

    @staticmethod
    def checkout():
        print("TODO: Checkout")
        Cart.get()

class History:

    @staticmethod
    def get():
        print("TODO: VIEW")

    @staticmethod
    def add():
        print("TODO: ADD")

    @staticmethod
    def remove():
        print("TODO: REMOVE")