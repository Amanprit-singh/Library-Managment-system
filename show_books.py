from utils import books

def show_book():
    print("\n SHOW BOOK")
    print("-" * 30)
    
    if len(books)==0:
        print("Book not available")
    else:
        for _ in  books:
            print("Book:",_)
