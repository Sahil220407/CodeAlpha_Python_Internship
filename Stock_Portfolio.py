
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====", flush=True)
print("\nAvailable Stocks:", flush=True)

for name, price in stock_prices.items():
    print(f"{name} = ${price}", flush=True)

while True:
    stock = input(
        "\nEnter stock name (or DONE to finish): "
    ).strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name. Try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print("Stock added successfully!")

    except ValueError:
        print("Please enter a valid whole number.")

print("\n===== PORTFOLIO REPORT =====")

total = 0

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total += value
    print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}")

print(f"TOTAL INVESTMENT: ${total}")

with open("portfolio_report.txt", "w") as file:
    file.write(f"Portfolio: {portfolio}\n")
    file.write(f"Total Investment: ${total}\n")

print("Report saved successfully!")
