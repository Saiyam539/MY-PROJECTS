# Student Library Managment System

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        if bookName in self.books:
            self.books.append(bookName)
            print('Thanks for returning the book.')
        else:
            print("This book is not given by Saiyam's Library")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         
try:
    if __name__ == "__main__":
        SaiyamLibrary = Library(['Python course', 'Django course', 'Full programming course', 'Space fact'])
        student = Student()
        # centraLibrary.displayAvailableBooks()
        while(True):
            welcomeMsg = '''\n ====== Welcome to SAIYAM's Library ======
            Please choose an option:
            1. List all the books
            2. Request a book
            3. Add/Return a book
            4. Exit the Library
            '''
            print(welcomeMsg)
            a = int(input("Enter a choice: "))
            if a == 1:
                SaiyamLibrary.displayAvailableBooks()
            elif a == 2:
                SaiyamLibrary.borrowBook(student.requestBook())
            elif a == 3:
                SaiyamLibrary.returnBook(student.returnBook())
            elif a == 4:
                print("Thanks for choosing Saiyam's Library. Have a great day ahead!")
                exit()
            else:
                print("Invalid Choice!")


except ValueError as e:
    print('Please enter the serial number of the opptions given')
