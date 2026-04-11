from utils import books

def add_book():
    book_name = input("Enter book name to add:").upper()
    books.append(book_name)
    print(f"Book '{book_name}' added.")