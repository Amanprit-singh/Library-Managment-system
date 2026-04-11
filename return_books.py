from utils import books, issue_books
#from issue_books import issue_book

def return_book():
    book_name=input("Enter book name to be returned:").upper()
    if book_name in issue_books:
        issue_books.remove(book_name)
        books.append(book_name)
        print(f"Book '{book_name}'returned")
    else:
        print("blablabla")
   