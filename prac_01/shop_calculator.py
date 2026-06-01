"""
A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""

total_price = 0
number_of_item = int(input("Number of Items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of Items: "))
for item in range(number_of_item):
    price_of_item = float(input("Price of Item: "))
    total_price += price_of_item
if total_price > 100:
    total_price = total_price * 0.9
print(f"Total price of {number_of_item} items is ${total_price:.2f}")
