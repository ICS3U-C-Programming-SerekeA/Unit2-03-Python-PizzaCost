#!/usr/bin/env pytthon3
# created by : Sereke Asfeday
# date:29th sept 2026
# This program asks the user for the pizza diameter and
# then calculates and displays the price pizza.


def main():
    # input
    print("Note: 1 inch = 2.54 cm")
    diameter = int(input("Enter the diameter of the pizza in, (inches):"))

    # process
    # Calculate the subtotal
    subtotal = 2.00 + 2.25 + 1.5 * diameter

    # Calculate the tax
    tax = 0.13 * subtotal

    # DISPLAY total
    total = subtotal + tax

    # output
    print(f"The total cost of the pizza is, ${total:.2f}")


if __name__ == "__main__":
    main()
