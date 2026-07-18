#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = input("Enter the coffee size (Small, Medium, or Large): ")
        if self.size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large.")
            self.size = input("Enter the coffee size (Small, Medium, or Large): ")
        
        self.price = float(input("Enter the price: "))

    def tip(self):
        print(f"This coffee is great, here's a tip!")
        self.price += 1

coffee = Coffee()
coffee.tip()