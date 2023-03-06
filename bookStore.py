# import tabulate
import sqlite3
import os.path
from tabulate import tabulate


class BookStore:

    def __init__(self, *args):
        try:
            if len(args) > 0:

                print("Creating a new database")
                print('Initializing the database table. Running program for the first time')
                self.db = sqlite3.connect('bookstore_db')
                self.cursor = self.db.cursor()

                self.cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER, Title TEXT, Author TEXT, Qty INTEGER)')

                for row in args[0]:
                    self.start_init(row)

            else:
                print("Using existing database")
                self.db = sqlite3.connect('bookstore_db')
                self.cursor = self.db.cursor()

            self.user_menu()
            self.db.commit()
            print('Exiting program...')
        except Exception as e:
            raise e

        finally:
            self.db.close()

    def start_init(self, *detail):
        self.cursor.execute('INSERT INTO books VALUES(?, ?, ?, ?)', detail[0])

    def view_all(self):
        self.cursor.execute('SELECT * FROM books')
        # for row in self.cursor:
        #     print(f'{row[0]}  {row[1]}  {row[2]}  {row[3]}')
        print(tabulate(self.cursor, headers=['id', 'Title', 'Author', 'Qty'], tablefmt='fancy_grid'))

    def check_id(self, get_id):
        self.cursor.execute('SELECT * FROM books WHERE id = ?', (get_id,))
        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def new_entry(self):
        while True:
            try:
                book_id = int(input("Book ID : "))
                book_title = input("Book Title: ")
                book_author = input("Book Author: ")
                book_qty = int(input("Book Quantity: "))

                self.cursor.execute('INSERT INTO books VALUES(?, ?, ?, ?)', (book_id, book_title, book_author, book_qty))
                # self.db.commit()

                break

            except Exception as e:
                print("Invalid input")
                raise e

        self.view_all()

    def update_book(self):
        update_msg = '''
        1. Update Title
        2. Update Author
        3. Update Qty
        4. Update All
        '''
        while True:
            try:
                book_id = int(input('Enter the ID to update: '))

                if not self.check_id(book_id):
                    print('Book id not found in the record')
                    continue
                self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
                print(tabulate(self.cursor, headers=['id', 'Title', 'Author', 'Qty'], tablefmt='fancy_grid'))

                # providing user with the choice to update either one of the attributes or all of the attributes
                update_choice = int(input(update_msg))

                if update_choice == 1:
                    updated_title = input('Enter Title to update : ')
                    self.cursor.execute('UPDATE books SET Title = ? WHERE id = ?', (updated_title, book_id))
                elif update_choice == 2:
                    updated_author = input('Enter Author update : ')
                    self.cursor.execute('UPDATE books SET Author = ? WHERE id = ?', (updated_author, book_id))
                elif update_choice == 3:
                    updated_qty = int(input('Enter Qty to update : '))
                    self.cursor.execute('UPDATE books SET Qty = ? WHERE id = ?', (updated_qty, book_id))
                elif update_choice == 4:
                    updated_title = input("Book Title: ")
                    updated_author = input("Book Author: ")
                    updated_qty = int(input("Book Quantity: "))
                    self.cursor.execute('UPDATE books SET Title = ?, Author=?, Qty=? WHERE id = ?', (updated_title, updated_author, updated_qty, book_id))
                break

            except ValueError:
                print('Invalid Error.')

    def delete_book(self):
        while True:
            try:
                book_id = int(input('Enter Book Id to delete : '))

                if not self.check_id(book_id):
                    print('Book id not found in the record.')
                    continue

                self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
                self.view_all()
                break

            except ValueError:
                print('Invalid Input')

    def search_book(self):
        while True:
            try:
                book_id = int(input('Enter Book Id to search : '))

                if not self.check_id(book_id):
                    print('Book id not found in the record.')
                    continue

                self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
                print(tabulate(self.cursor, ['id', 'Title', 'Author', 'Qty'], tablefmt='fancy_grid'))
                break

            except ValueError:
                print('Invalid Input')

    def user_menu(self):
        menu = ''' 
            Enter your choice:
    
            1. Enter book
            2. Update book
            3. Delete book
            4. Search book
            5. View all books
            0. Exit
            '''

        while True:
            choice = int(input(menu))

            if choice == 1:
                self.new_entry()
            elif choice == 2:
                self.update_book()

            elif choice == 3:
                self.delete_book()

            elif choice == 4:
                self.search_book()

            elif choice == 5:
                self.view_all()

            else:
                exit()


def main():
    book_details = ((3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
                    (3002, 'Harry Potter and the Philosopher\'s Stone', ' J.K Rowling', 40),
                    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S Lewis', 25),
                    (3004, 'The Lord of the Rings', 'J.R.R Tolkein', 37),
                    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12))

    if not os.path.exists('./bookstore_db'):
        BookStore(book_details)

    else:
        BookStore()


if __name__ == '__main__':
    main()
