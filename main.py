import sqlite3
import uuid
from Classes import User
from Classes import Book
from Classes import Cart
from Classes import History

def createAllTables():
    curser.execute("CREATE TABLE IF NOT EXISTS Users(id TEXT PRIMARY KEY, firstName TEXT, lastName TEXT, userName TEXT, password TEXT, address TEXT, creditCardNumber TEXT)")
    curser.execute("CREATE TABLE IF NOT EXISTS Books(id TEXT PRIMARY KEY, ISBN TEXT, title TEXT, author TEXT, cat TEXT, stock INTEGER)")
    curser.execute("CREATE TABLE IF NOT EXISTS Carts(id TEXT PRIMARY KEY, bookID TEXT, userID TEXT)")
    curser.execute("CREATE TABLE IF NOT EXISTS OrderHistory(id TEXT PRIMARY KEY, userID TEXT)")
    connection.commit()

def resetUsersTable():
    curser.execute("DELETE FROM Users")
    connection.commit()

def resetBooksTable():
    curser.execute("DELETE FROM Books")
    createBook(str(uuid.uuid1()), '978-1734554908', 'Computer Science Principles: The Foundational Concepts of Computer Science', 'Mr. Kevin P Hare', 'Computer Science', 10)
    createBook(str(uuid.uuid1()), '978-1951204006', 'A Programmer\'s Guide to Computer Science', 'Dr. William M Springer II', 'Computer Science', 10)
    createBook(str(uuid.uuid1()), '978-1119293491', 'Calculus For Dummies', 'Mark Ryan', 'Math', 10)
    createBook(str(uuid.uuid1()), '978-0486457956', 'Advanced Calculus', 'Avner Friedman', 'Math', 10)
    createBook(str(uuid.uuid1()), '978-1119629900', 'Basic Physics', 'Karl F. Kuhn', 'Physics', 10)
    createBook(str(uuid.uuid1()), '978-0060935467', 'To Kill a Mockingbird', 'Harper Lee', 'Southern Gothic', 10)
    createBook(str(uuid.uuid1()), '978-0399501487', 'Lord of the Flies', 'William Golding', 'Fiction', 10)
    createBook(str(uuid.uuid1()), '978-1954839373', 'Dr. Jekyll and Mr. Hyde', 'Robert Louis Stevenson', 'Fiction', 10)
    createBook(str(uuid.uuid1()), '978-1451673319', 'Fahrenheit 451', 'Ray Bradbury', 'Fiction', 10)
    createBook(str(uuid.uuid1()), '978-0062387240', 'Divergent', 'Veronica Roth', 'Fiction', 10)
    connection.commit()

def createBook(id, ISBN, title, author, genre, stock):
    curser.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)", (id, ISBN, title, author, genre, stock))
    connection.commit()

def resetCartsTable():
    curser.execute("DELETE FROM Carts")
    connection.commit()

def resetOrderHistoryTable():
    curser.execute("DELETE FROM OrderHistory")
    connection.commit()

def beforeLoginMenu():
    print("1. Login")
    print("2. Create account")
    print("3. Exit")
    option = input()
    if option == "1":
        login()
    elif option == "2":
        createAccount()
    elif option == "3":
        curser.close()
        connection.close()
        exit()

# Before login - Menu option 1
def login():
    print("----- Logging in -----")
    username = input("Username: ")
    password = input("Password: ")
    curser.execute("SELECT * FROM Users WHERE userName = (?) AND password = (?)", (username, password,))
    userFetch = curser.fetchall()
    if len(userFetch) == 1:
        currentUserID = userFetch[0][0]
        afterLoginMenu()
    else:
        print("Error. Please try again.")
        print("1. Go back")
        print("2. Login")
        option = input()
        if option == "1":
            beforeLoginMenu()
        elif option == "2":
            login()

# Before login - Menu option 2
def createAccount():
    print("----- Creating account -----")
    firstName = input("First name: ")
    lastName = input("Last name: ")
    username = input("Username: ")
    password = input("Password: ")
    address = input("Address: ")
    payment = input("Credit card number: ")
    curser.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?)", (str(uuid.uuid1()), firstName, lastName, username, password, address, payment))
    connection.commit()
    beforeLoginMenu()

# Before login - Menu option 3
def exit():
    quit()

def afterLoginMenu():
    print("----- Main Menu -----")
    print("1. View all books")
    print("2. View all genres")
    print("3. View shopping cart")
    print("4. View account")
    option = input()
    if option == "1":
        viewAllBooks()
    elif option == "2":
        viewAllCategories()
    elif option == "3":
        viewShoppingCart()
    elif option == "4":
        viewAccount()

# After login - Menu option 1
def viewAllBooks():
    curser.execute("SELECT * FROM Books") #TODO: Only need to fetch titles
    books = curser.fetchall()
    index = 1
    for book in books:
        print(str(index) + ". " + book[2])
        index += 1
    print("\n1. Go back")
    print("2. Add book to cart")
    option = input()
    if option == "1":
        afterLoginMenu()
    elif option == "2":
        bookNumber = input("Book #:")
        addBookToCart(books[int(bookNumber)][0])
        afterLoginMenu()

# After login - Menu option 2
def viewAllCategories():
    print("----- All categories -----")
    genres = curser.execute("SELECT DISTINCT genre FROM Books")
    for genre in genres:
        print("- ", genre[0])
    print("1. Go back")
    print("2. See all books for specific genre")
    option = input()
    if option == "1":
        afterLoginMenu()
    elif option == "2":
        genre = input("Genre #: ")
        seeAllBooksForGenre(genre)

# After login - Menu option 3
def viewShoppingCart():
    print("----- Shopping cart -----")
    print("TODO: GET BOOKS IN SHOPPING CART FROM CARTS TABLE")
    print("1. Go back")
    print("2. Remove book from cart")
    print("3. Checkout")
    option = input()
    if option == "1":
        afterLoginMenu()
    elif option == "2":
        book = input("Book #: ")
        removeBookFromCart(book)
    elif option == "3":
        checkout()

# After login - Menu option 4
def viewAccount():
    print("----- Account -----")
    print("1. Go back")
    print("2. View order history")
    print("3. Change address")
    print("4. Change payment info")
    print("5. Logout")
    print("6. Delete account")
    option = input()
    if option == "1":
        afterLoginMenu()
    elif option == "2":
        viewOrderHistory()
    elif option == "3":
        changeAddress()
    elif option == "4":
        changePaymentInfo()
    elif option == "5":
        logout()
    elif option == "6":
        deleteAccount()

def logout():
    currentUserID = ""
    beforeLoginMenu()

def seeAllBooksForGenre(genre):
    print("----- All books for ", genre, "-----")
    print("TODO: GET BOOKS FOR genre FROM BOOKS TABLE")
    print("1. Go back")
    print("2. Add book to cart")
    option = input()
    if option == "1":
        viewAllCategories()
    if option == "2":
        book = input("Book #: ")
        addBookToCart(book)

def addBookToCart(bookID):
    curser.execute("INSERT INTO Carts VALUES (?, ?, ?)", (str(uuid.uuid1()), bookID, currentUserID))
    connection.commit()

def removeBookFromCart(book):
    print("TODO: Remove book from cart")
    viewShoppingCart()

def checkout():
    print("TODO: Checkout")
    viewShoppingCart()

def viewOrderHistory():
    print("TODO: View order history")
    viewAccount()

def changeAddress():
    print("TODO: Change address")
    viewAccount()

def changePaymentInfo():
    print("TODO: Change payment info")
    viewAccount()

def deleteAccount():
    print("TODO: Delete account")
    beforeLoginMenu()

# Start program
connection = sqlite3.connect("LibraryProject.db")
curser = connection.cursor()

createAllTables()

if False:
    resetBooksTable()
    resetCartsTable()
    resetOrderHistoryTable()
    resetUsersTable()

currentUserID = ""
beforeLoginMenu()