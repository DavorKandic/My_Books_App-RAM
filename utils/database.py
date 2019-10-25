
"""
Concerned with storing and retrieving books from a list.
"""


books =[]


def take_input():
    inp = input('Your choice: ')
    return inp.lower().strip()
    


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    print('Database updated!\n')
    
    
def get_all_books():
    return books
    
def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            print('Database updated!\n')
        else:
            print('Book not found!')
    
##def delete_book(name):
##    for book in books:
##        if book['name'] == name:
##            books.remove(book)
##    print('Database updated!\n')
    
def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]
    print('Database updated!\n')
    
    