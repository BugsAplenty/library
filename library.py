#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:52:53 2020

@author: Michael Perfetto
"""

from random import choice

class Library:
    def __init__(self,
                 max_books,
                 max_customers,
                 max_borrow):
        self.max_books = max_books
        self.max_customers = max_customers
        self.max_borrow = max_borrow

        self.books = []
        self.customers = []
        self.id_numbers = [0]
        

    def add_book(self, book):
        """
        Adds a book to the library's list of books.
        :param book: an object of type Book.
        :type book: Book
        """
        if len(self.books) < self.max_books:
            self.books.append(book)
        else:
            fail_string = "Library at maximal capacity. You cannot add any more books."
            return fail_string

    def remove_book(self, book):
        """
        Removes a book to the library's list of books.
        :param book: an object of type Book.
        :type book: Book
        """
        if len(self.books) > 0:
            if not book in self.books:
                fail_string = "This book does not exist in our inventory."
                return fail_string
            else:
                self.books.remove(book)
        else:
            fail_string = "Inventory empty."
            return fail_string

    def add_customer(self, customer):
        """
        Adds a customer to the library's list of customers.
        :param book: an object of type Customer.
        :type book: Customer
        """
        if not customer in self.customers:
            if len(self.customers) < self.max_customers:
                if customer.customer_id == None:
                    self.customers.append(customer)
                    customer.customer_id = choice([i for i in range(self.max_customers+2) if i not in self.id_numbers])
                    self.id_numbers.append(customer.customer_id)
                else:
                    fail_string = "This customer is already registered to another library."
                    return fail_string
            else:
                fail_string = "Library at maximal capacity. You cannot add any more customers."
                return fail_string
        else:
            fail_string = "You seem to be already registered in this library."
            return fail_string

    def remove_customer(self, customer):
        """
        Removes a customer to the library's list of customers.
        :param book: an object of type Customer.
        :type book: Customer
        """
        if len(self.customers) > 0:
            if customer in self.customers:
                for book in customer.books_borrowed:
                    self.books.append(book)
                customer.books_borrowed.clear()
                self.customers.remove(customer)
                customer.customer_id = None
            else:
                fail_string = "This customer does not exist in our database."
                return fail_string

        else:
            fail_string = "Customer database empty."
            return fail_string

    def borrow(self, customer, book):
        """
        Adds a book to the customer's list of borrowed books and removes it from the library's list of books.
        :param customer: An object of type Customer.
        :type customer: Customer
        :param book: An object of type Book.
        :type book: Book
        """
        book_value = customer.weight_educational * book.val_educational + \
                     customer.weight_dramatic * book.val_dramatic + \
                     customer.weight_comedic * book.val_comedic
        if customer in self.customers:
            if book_value > customer.min_enjoyment:
                if len(customer.books_borrowed) < self.max_borrow:
                    if(self.remove_book(book) == None):
                        self.remove_book(book)
                        customer.books_borrowed.append(book)
                    else:
                        return self.remove_book(book)
                else:
                    fail_string = "Sorry, you've already borrowed the maximal amount of books."
                    return fail_string
            else:
                fail_string = "This book doesn't seem right for you."
                return fail_string
        else:
            fail_string = "This customer does not exist in our database."
            return fail_string

    def retrieve(self, customer, book):
        """
        Removes a book from the customer's list of borrowed books and adds it to the library's list of books.
        :param customer: An object of type Customer.
        :type customer: Customer
        :param book: An object of type Book.
        :type book: Book
        """
        if book in customer.books_borrowed:
            if customer in self.customers:
                if(self.add_book(book) == None):
                    customer.books_borrowed.remove(book)
                else:
                    return self.add_book(book)
            else:
                fail_string = "This customer does not exist in our database."
                return fail_string
        else:
            fail_string = "You don't seem to have that book"
            return fail_string


    def recommend(self, customer):
        """
        Selects a book from the library's list of books and recommends it to the customer.
        :param customer: An object of type Customer.
        :type customer: Customer
        :return: A message recommending the best fit book out of the library's list.
        """
        compatibility = [0] * len(self.books)
        for i in range(len(self.books)):
            compatibility[i] = self.books[i].val_comedic * customer.weight_comedic + \
                               self.books[i].val_dramatic * customer.weight_dramatic + \
                               self.books[i].val_educational * customer.weight_educational
            
        index_recommended = compatibility.index(max(compatibility))
        book_recommended = self.books[index_recommended]
        
        recommend_string = f"Perhaps you'd like to try {book_recommended.title} - {book_recommended.author} ({book_recommended.year_publish})"
        return recommend_string

class Book:
    def __init__(self,
                 title,
                 author,
                 year_publish,
                 val_comedic,
                 val_dramatic,
                 val_educational):
        self.title = title
        self.author = author
        self.year_publish = year_publish
        self.val_comedic = val_comedic
        self.val_dramatic = val_dramatic
        self.val_educational = val_educational

    def __hash__(self):
        return hash((self.title, self.author, self.year_publish))

    def __eq__(self, other):
        return (self.title, self.author, self.year_publish) == (other.title, 
               other.author, other.year_publish)

    def __ne__(self, other):
        return not(self == other)
    
    def __str__(self):
        return f"{self.title}, by {self.author} ({self.year_publish})"
    
    def __repr__(self):
        return f"{self.title} - {self.author} ({self.year_publish})"
    
    def display_book_details(self):
        return f"[{self.title}, {self.author}, {self.year_publish}, {self.val_comedic}, {self.val_dramatic}, {self.val_educational}]"
    
class Customer:

    def __init__(self,
                 first_name,
                 last_name,
                 min_enjoyment,
                 weight_comedic,
                 weight_dramatic,
                 weight_educational):
        
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = None
        self.min_enjoyment = min_enjoyment
        self.weight_comedic = weight_comedic
        self.weight_dramatic = weight_dramatic
        self.weight_educational = weight_educational
        self.books_borrowed = []
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}, ID: {self.customer_id}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, ID: {self.customer_id}"
    
    def display_customer_details(self):
        return f"{self.first_name} {self.last_name}"
    



