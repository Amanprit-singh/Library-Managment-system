from utils import books, issued_books
from datetime import date
from utils import date_of_issue

def issue_book():
    print("\n ISSUE BOOK")
    print("-" * 30)
    
    book_name = input("Enter the book name:").upper()
    
    
    if book_name not in books:
        print(f"Book '{book_name}' is not available.\n")
        return
        
        
    student_name = input("Enter student name: ")
    d=int(input("enter today's day:"))
    m=int(input("enter month:"))
    y=int(input("enter year:"))
    issue_date=date(y,m,d)
    date_of_issue.update({book_name:issue_date})
    days_allowed = int(input("Issued for how many days? : "))
    
    
    issued_books[book_name] = {
        "student_name": student_name,
        "issue_date": issue_date,
        "days_allowed": days_allowed
    }

    books.remove(book_name)

    print("\n✅ Book Issued Successfully!")
    print(f"Book Name      : {book_name}")
    print(f"Student Name   : {student_name}")
    print(f"Issue Date     : {issue_date}")
    print(f"Allowed Days   : {days_allowed}")
    print(f"""
        ⚠️ Late Fine Rules:
        Week 1 → ₹10/day
        Week 2 → ₹20/day
        Week 3 → ₹60/day (10×2×3)
        ...and so on""")
