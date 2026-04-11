from utils import books, issue_books

def issue_book():
    book_name = input("Enter the book name:").upper()
    if book_name in books:
        books.remove(book_name)
        issue_books.append(book_name)
        print(f"Book '{book_name}' issued.")
    else:
        print("Book not available")