# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$" + str(price))

n = int(input("\nEnter number of stocks you own: "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print("Investment Value =", investment)
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Save result in file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total_investment))
file.close()

print("Result saved in portfolio.txt")
