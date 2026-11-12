# CodeAlpha Internship
# Project: Stock Portfolio Tracker

import csv

# Predefined stock prices (sample prices in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 150,
    "AMZN": 190
}

# Store user's stock quantities
portfolio = {}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

# Display available stocks
print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Ask how many different stocks the user wants
while True:
    try:
        n = int(input("\nHow many stocks do you want to add? "))

        if n > 0:
            break
        print("Please enter a number greater than zero.")

    except ValueError:
        print("Please enter a valid whole number.")

# Get stock names and quantities
for i in range(n):

    stock = input("\nEnter stock symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid quantity.")

# Calculate and display investment
total_investment = 0
rows = []

print("\n========== PORTFOLIO SUMMARY ==========")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(f"{stock} | Price: ${price} | "
          f"Quantity: {quantity} | Value: ${investment}")

    rows.append([stock, price, quantity, investment])

print("---------------------------------------")
print(f"Total Investment: ${total_investment}")
print("=======================================")

# Save portfolio to CSV file
with open("portfolio_summary.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Stock", "Price", "Quantity", "Total Value"])

    writer.writerows(rows)

    writer.writerow(["TOTAL", "", "", total_investment])

print("\nPortfolio saved successfully!")
print("File name: portfolio_summary.csv")