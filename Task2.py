import yfinace as fy
import json
import os

PORTFOLIO_FILE = "portfolio.json"

# Load existing portfolio
def load_portfolio():
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, "r") as f:
            return json.load(f)
    return {}

# Save portfolio to file
def save_portfolio(portfolio):
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(portfolio, f, indent=2)

# Add a stock
def add_stock(portfolio):
    symbol = input("Stock Symbol (e.g. AAPL): ").upper()
    quantity = float(input("Quantity: "))
    buy_price = float(input("Buy Price per share: "))

    portfolio[symbol] = {
        "quantity": quantity,
        "buy_price": buy_price
    }
    print(f"✅ Added {quantity} of {symbol} at ${buy_price}")
    save_portfolio(portfolio)

# Remove a stock
def remove_stock(portfolio):
    symbol = input("Stock Symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"❌ Removed {symbol}")
        save_portfolio(portfolio)
    else:
        print("⚠️ Stock not found.")

# View performance
def view_portfolio(portfolio):
    print("\n📊 Portfolio Performance:")
    total_value = 0
    total_cost = 0

    for symbol, info in portfolio.items():
        stock = yf.Ticker(symbol)
        current_price = stock.info['regularMarketPrice']
        quantity = info['quantity']
        buy_price = info['buy_price']
        value = current_price * quantity
        cost = buy_price * quantity
        gain = value - cost
        percent = (gain / cost) * 100

        print(f"{symbol}:")
        print(f"  Current Price: ${current_price:.2f}")
        print(f"  Quantity: {quantity}")
        print(f"  Invested: ${cost:.2f}")
        print(f"  Value Now: ${value:.2f}")
        print(f"  Gain/Loss: ${gain:.2f} ({percent:.2f}%)\n")

        total_value += value
        total_cost += cost

    print(f"📦 Total Invested: ${total_cost:.2f}")
    print(f"💰 Total Value: ${total_value:.2f}")
    print(f"📈 Total Gain/Loss: ${total_value - total_cost:.2f}")

# Menu
def main():
    portfolio = load_portfolio()

    while True:
        print("\n==== STOCK PORTFOLIO TRACKER ====")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_stock(portfolio)
        elif choice == '2':
            remove_stock(portfolio)
        elif choice == '3':
            view_portfolio(portfolio)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
