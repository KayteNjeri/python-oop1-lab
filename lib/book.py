#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = input("Enter the title of the book: ")
        
        self.page_count = input("Enter the page count: ")
        try:
            self.page_count = int(self.page_count)
        except ValueError:
            print("page_count must be an integer")

    def turn_page(self):
        print(f"Flipping the page...wow, you read fast!")

book = Book()
book.turn_page()
