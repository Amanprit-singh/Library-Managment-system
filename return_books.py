from utils import books, issued_books, date_of_issue
from datetime import date
from math import factorial

def return_book():
    print("\n RETURN BOOK")
    print("-" * 30)

    book_name = input("Enter book name to be returned: ").strip().upper()

    if book_name in issued_books:
        print("\n Enter Return Date")
        day = int(input("Day   : "))
        month = int(input("Month : "))
        year = int(input("Year  : "))

        return_date = date(year, month, day)

        # Calculate total days
        total_days = (return_date - date_of_issue[book_name]).days

        # Calculate late days (after 7 days)
        late_days = max(0, total_days - 7)

        # Fine Calculation
        fine = 0
        week = 1

        while late_days > 0:
            days_in_week = min(7, late_days)
            fine += days_in_week * (10 * factorial(week))
            late_days -= days_in_week
            week += 1

        # Update records
        del issued_books[book_name]
        books.append(book_name)
        del date_of_issue[book_name]

        print("\n RETURN SUMMARY")
        print("-" * 35)
        print(f"Book Name    : {book_name}")
        print(f"Days Used    : {total_days}")
        print(f"Fine Amount  : ₹{fine}")
        print("-" * 35)

        if fine > 0:
            print(" Please pay the fine.")
        else:
            print(" Returned on time!")

        print(f" Book '{book_name}' returned successfully.\n")

    else:
        print(f"❌ Book '{book_name}' is not currently issued.\n")
