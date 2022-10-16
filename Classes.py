class User:
    id = ()
    firstName = ()
    lastName = ()
    userName = ()
    password = ()
    address = ()
    payment = ()

    def login(self):
        print("TODO: LOGIN")

    def logout(self):
        print("TODO: LOGOUT")

    def delete(self):
        print("TODO: DELETE")

    def getCart(self):
        print("TODO: GET CART")

    def getOrderHistory(self):
        print("TODO: GET ORDER HISTORY")

class Book:
    id = ()
    ISBN = ()
    title = ()
    author = ()
    stock = ()
    category = ()

    def setStock(self):
        print("TODO: SET STOCK")

class Cart:
    id = ()
    user = ()

    def add(self):
        print("TODO: ADD")

    def remove(self):
        print("TODO: REMOVE")

    def getAllBooksInCart(self):
        print("TODO: GET ALL BOOKS IN CART")

    def getAllBooks(self):
        print("TODO: GET ALL BOOKS")

    def getBooksInCategory(self):
        print("TODO: GET BOOKS IN CATEGORY")

    def checkout(self):
        print("TODO: CHECKOUT")

class History:
    id = ()
    user = ()

    def add(self):
        print("TODO: ADD")

    def remove(self):
        print("TODO: REMOVE")