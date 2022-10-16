import sqlite3
import uuid

from Classes import User
from Classes import Book
from Classes import Cart
from Classes import History

def createAllTables():
    curser.execute("CREATE TABLE IF NOT EXISTS Users(id TEXT PRIMARY KEY, firstName TEXT, lastName TEXT, userName TEXT, password TEXT, address TEXT, payment TEXT)")
    curser.execute("CREATE TABLE IF NOT EXISTS Books(id TEXT PRIMARY KEY, ISBN TEXT, title TEXT, author TEXT, category TEXT, stock INTEGER)")
    curser.execute("CREATE TABLE IF NOT EXISTS Carts(id TEXT PRIMARY KEY, user TEXT)")
    curser.execute("CREATE TABLE IF NOT EXISTS OrderHistory(id TEXT PRIMARY KEY, user TEXT)")

def resetUsersTable():
    curser.execute("DELETE FROM Users")

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

def createBook(id, ISBN, title, author, category, stock):
    curser.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)", (id, ISBN, title, author, category, stock))

def resetCartsTable():
    curser.execute("DELETE FROM Carts")

def resetOrderHistoryTable():
    curser.execute("DELETE FROM OrderHistory")

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
        exit()

# Before login - Menu option 1
def login():
    print("----- Logging in -----")
    username = input("Username: ")
    password = input("Password: ")
    afterLoginMenu()

# Before login - Menu option 2
def createAccount():
    print("----- Creating account -----")
    username = input("Username: ")
    password = input("Password: ")
    beforeLoginMenu()

# Before login - Menu option 3
def exit():
    quit()

def afterLoginMenu():
    print("----- Main Menu -----")
    print("1. View all books")
    print("2. View all categories")
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
    curser.execute("SELECT * FROM Books")
    print(curser.fetchall())
    print("1. Go back")
    print("2. Add book to cart")
    option = input()
    if option == "1":
        afterLoginMenu()
    elif option == "2":
        book = input("Book #:")
        addBookToCart(book)
        afterLoginMenu()

# After login - Menu option 2
def viewAllCategories():
    print("----- All categories -----")
    print("TODO: GET CATEGORIES FROM BOOKS TABLE")
    print("1. Go back")
    print("2. See all books for specific category")
    option = input()
    if option == "1":
        afterLoginMenu()
    elif option == "2":
        category = input("Category #: ")
        seeAllBooksForCategory(category)

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
    print("TODO: LOGOUT")
    beforeLoginMenu()

def seeAllBooksForCategory(category):
    print("----- All books for ", category, "-----")
    print("TODO: GET BOOKS FOR CATEGORY FROM BOOKS TABLE")
    print("1. Go back")
    print("2. Add book to cart")
    option = input()
    if option == "1":
        viewAllCategories()
    if option == "2":
        book = input("Book #: ")
        addBookToCart(book=book)

def addBookToCart(book):
    print("TODO: Add book to cart")

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

beforeLoginMenu()