#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:52:53 2020

@author: Michael Perfetto
"""
from library import Book, Library, Customer

book1 = Book("Nineteen Eighty-Four", "George Orwell", 1949, 0, 10, 5)
book2 = Book("The Catcher in the Rye", "J.D. Salinger", 1951, 2, 5, 4)
book3 = Book("Infinite Jest", "David Foster Wallace", 1996, 1, 1, 20)

customer1 = Customer("Michael", "Neiman", 15, 1, 1, 1) 
customer2 = Customer("Gal", "Oz-Ari", 22, 1, 1, 2)
customer3 = Customer("Bob", "Jones", 1, 1, 1, 1)

"""
0. Displaying book/customer data.
"""
print(book1.display_book_details() == "[Nineteen Eighty-Four, George Orwell, 1949, 0, 10, 5]")
print(customer1.display_customer_details() == "Michael Neiman")

"""
1. add/remove_book methods recieve only objects of type Book - TODO.
"""

"""
2. add/remove_customer methods recieve only objects of type Customer - TODO.
"""

"""
3. borrow/retrieve/recommend methods recieve only objects of type Book and Customer - TODO.
"""

"""
4. Exceeding the maximal amount of customers/books in library.
"""
library1 = Library(0,0,0)
print(library1.add_book(book1) == "Library at maximal capacity. You cannot add any more books.")
print(library1.add_customer(customer1) == "Library at maximal capacity. You cannot add any more customers.")
print(library1.remove_book(book1) == "Inventory empty.")
print(library1.remove_customer(customer1) == "Customer database empty.")

"""
5. Adding/removing books/customers.
"""
library2 = Library(1,1,0)
library2.add_book(book1)
print(len(library2.books)==1)
library2.remove_book(book1)
print(len(library2.books)==0)
library2.add_customer(customer1)
print(len(library2.customers)==1)
library2.remove_customer(customer1)
print(len(library2.customers)==0)

"""
6. Removing a book/customer that doesn't exist.
"""
library2.add_book(book1)
library2.add_customer(customer1)
print(library2.remove_book(book2) == "This book does not exist in our inventory.")
print(library2.remove_customer(customer2) == "This customer does not exist in our database.")

"""
7. Adding a customer that already exists.
"""
library2.add_customer(customer1)
print(library2.add_customer(customer1) == "You seem to be already registered in this library.")

"""
8. Adding a customer from another library.
"""
library3 = Library(1,1,1)
print(library3.add_customer(customer1) == "This customer is already registered to another library.")

"""
9. All customers get a unique ID.
"""
library2.remove_customer(customer1)
library4 = Library(1,3,1)
library4.add_customer(customer1)
library4.add_customer(customer2)
library4.add_customer(customer3)
print(isinstance(customer1.customer_id, int))
print(customer1.customer_id != customer2.customer_id)
print(customer2.customer_id != customer3.customer_id)

"""
10. Borrowing more books than allowed.
"""
library5 = Library(2, 1, 1)
customer4 = Customer("John", "Smith", 0, 1, 1, 1)
library5.add_book(book1)
library5.add_book(book2)
library5.add_customer(customer4)
library5.borrow(customer4, book1)
print(library5.borrow(customer4, book2) == "Sorry, you've already borrowed the maximal amount of books.")

"""
11. Borrowing a book that doesn't satisfy the minimal enjoyment cap.
"""
library6 = Library(1, 1, 1)
library6.add_book(book1)
customer5 = Customer("Snob", "Snobson", 1000, 1, 1, 1)
library6.add_customer(customer5)
print(library6.borrow(customer5, book1) == "This book doesn't seem right for you.")
"""
11. Retrieving a book from a customer who doesn't have it.
"""
print(library6.retrieve(customer5, book2) == "You don't seem to have that book")
"""
12. Removing a customer who's borrowed books returns the books to the library.
"""
library7 = Library(2, 1, 2)
customer6 = Customer("Larry", "David", 1, 1, 1, 1)
library7.add_book(book1)
library7.add_book(book2)
library7.add_customer(customer6)
library7.borrow(customer6, book1)
library7.borrow(customer6, book2)
library7.remove_customer(customer6)
print(len(library7.books) == 2)
"""
13. The recommended book is the right one.
"""
library8 = Library(3, 1, 1)
customer2 = Customer("Gal", "Oz-Ari", 22, 1, 1, 2)
book1 = Book("Nineteen Eighty-Four", "George Orwell", 1949, 0, 10, 5)
book2 = Book("The Cather in the Rye", "J.D. Salinger", 1951, 2, 5, 4)
book3 = Book("Infinite Jest", "David Foster Wallace", 1996, 1, 1, 20)
library8.add_book(book1)
library8.add_book(book2)
library8.add_book(book3)
print(library8.recommend(customer2) == "Perhaps you'd like to try Infinite Jest - David Foster Wallace (1996)")