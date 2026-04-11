from add_books import add_book
from show_books import show_book
from return_books import return_book
from issue_books import issue_book


def library():
    while True:
        print("---Library Managment---")
        print('\n1.Add Book')
        print('\n2.Show Book')
        print('\n3.Issue Book')
        print('\n4.Return Book')
        print('\n5.Exit')
    
        choice = int(input("Enter your choice:"))
    
        if choice == 1:  add_book()
        elif choice == 2:  show_book()
        elif choice == 3:  issue_book()
        elif choice == 4:  return_book()
        elif choice == 5:
           print("Thank you")
           break
library()