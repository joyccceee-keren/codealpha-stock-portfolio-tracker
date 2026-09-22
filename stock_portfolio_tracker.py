"""
CodeAlpha Internship - Task 2
Stock Portfolio Tracker

Goal:
A Python-based Stock Portfolio Tracker that calculates total investment value 
based on predefined (hardcoded) stock prices and user inputs.

Key Concepts:
- Dictionaries (price lookup & portfolio storage)
- Input / Output handling & validation
- Basic arithmetic calculations
- File handling (saving report to .csv / .txt)
"""

import csv
import datetime
import os


# Predefined/hardcoded dictionary of stock prices (USD)
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.00,
    "MSFT": 420.75,
    "GOOGL": 175.25,
    "AMZN": 185.00,
    "NVDA": 125.80,
    "META": 505.30,
    "NFLX": 640.20,
}


def display_available_stocks():
    """Display the available stocks and their fixed prices."""
    print("\n" + "=" * 45)
    print("        AVAILABLE STOCKS & PRICES (USD)")
    print("=" * 45)
    print(f"{'Symbol':<10} | {'Price per Share ($)':>20}")
    print("-" * 45)
    for symbol, price in sorted(STOCK_PRICES.items()):
        print(f"{symbol:<10} | ${price:>19.2f}")
    print("=" * 45 + "\n")


def get_positive_integer(prompt):
    """Prompt user for a positive integer (quantity)."""
    while True:
        user_input = input(prompt).strip()
        try:
            qty = int(user_input)
            if qty <= 0:
                print("[!] Quantity must be greater than 0. Please try again.")
                continue
            return qty
        except ValueError:
            print("[!] Invalid input! Please enter a valid whole number.")


def collect_portfolio():
    """Interactive loop to collect stock purchases from user."""
    portfolio = {}  # Format: {symbol: quantity}

    display_available_stocks()
    print("[*] Enter your stocks below. Type 'DONE' when finished.\n")

    while True:
        symbol = input("Enter Stock Symbol (e.g. AAPL, TSLA) or 'DONE': ").strip().strip("\"'").upper()

        if symbol == "DONE":
            if not portfolio:
                print("[!] No stocks added yet. Please add at least one stock or enter 'EXIT' to quit.")
                continue
            break
        
        if symbol == "EXIT":
            return None

        if symbol not in STOCK_PRICES:
            print(f"[!] '{symbol}' is not in the predefined price list.")
            print(f"    Available symbols: {', '.join(sorted(STOCK_PRICES.keys()))}")
            continue

        quantity = get_positive_integer(f"Enter quantity of shares for {symbol}: ")
        
        # Add to portfolio (if already entered, update quantity)
        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"[+] Updated {symbol}! New total shares: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f"[+] Added {quantity} share(s) of {symbol} to your portfolio.")

        print("-" * 45)

    return portfolio


def calculate_and_display_summary(portfolio):
    """Calculate and display a formatted portfolio summary table."""
    print("\n" + "=" * 65)
    print("                 PORTFOLIO SUMMARY REPORT")
    print("=" * 65)
    print(f"{'Stock':<10} | {'Shares':<10} | {'Price ($)':<15} | {'Total Value ($)':<15}")
    print("-" * 65)

    grand_total = 0.0
    summary_data = []

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        total_val = qty * price
        grand_total += total_val
        summary_data.append({
            "symbol": symbol,
            "shares": qty,
            "price": price,
            "total_value": total_val
        })
        print(f"{symbol:<10} | {qty:<10} | ${price:<14.2f} | ${total_val:<14.2f}")

    print("=" * 65)
    print(f"{'TOTAL PORTFOLIO INVESTMENT:':<38} | ${grand_total:<14.2f}")
    print("=" * 65 + "\n")

    return grand_total, summary_data


def save_portfolio_to_csv(summary_data, grand_total, filename="portfolio_summary.csv"):
    """Save the portfolio summary into a CSV file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Portfolio Tracker Report"])
        writer.writerow(["Generated At", timestamp])
        writer.writerow([])
        writer.writerow(["Stock Symbol", "Shares Owned", "Price Per Share ($)", "Total Value ($)"])
        
        for item in summary_data:
            writer.writerow([item["symbol"], item["shares"], f"{item['price']:.2f}", f"{item['total_value']:.2f}"])
        
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"${grand_total:.2f}"])
    
    print(f"[+] Successfully saved portfolio report to: {os.path.abspath(filename)}")


def save_portfolio_to_txt(summary_data, grand_total, filename="portfolio_summary.txt"):
    """Save the portfolio summary into a plain TXT file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write("=" * 65 + "\n")
        file.write("                 STOCK PORTFOLIO REPORT\n")
        file.write(f" Generated: {timestamp}\n")
        file.write("=" * 65 + "\n")
        file.write(f"{'Stock':<10} | {'Shares':<10} | {'Price ($)':<15} | {'Total Value ($)':<15}\n")
        file.write("-" * 65 + "\n")
        for item in summary_data:
            file.write(f"{item['symbol']:<10} | {item['shares']:<10} | ${item['price']:<14.2f} | ${item['total_value']:<14.2f}\n")
        file.write("=" * 65 + "\n")
        file.write(f"{'TOTAL INVESTMENT:':<38} | ${grand_total:<14.2f}\n")
        file.write("=" * 65 + "\n")
    
    print(f"[+] Successfully saved portfolio report to: {os.path.abspath(filename)}")


def main():
    print("\n" + "#" * 55)
    print("   STOCK PORTFOLIO TRACKER (CODEALPHA TASK 2)")
    print("#" * 55)

    portfolio = collect_portfolio()
    if not portfolio:
        print("\nProgram exited. Have a great day!")
        return

    grand_total, summary_data = calculate_and_display_summary(portfolio)

    # Optional file export prompt
    print("Save Report Options:")
    print("  1. Save as CSV file (.csv)")
    print("  2. Save as Text file (.txt)")
    print("  3. Save both (.csv & .txt)")
    print("  4. Skip saving")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    if choice == "1":
        save_portfolio_to_csv(summary_data, grand_total)
    elif choice == "2":
        save_portfolio_to_txt(summary_data, grand_total)
    elif choice == "3":
        save_portfolio_to_csv(summary_data, grand_total)
        save_portfolio_to_txt(summary_data, grand_total)
    else:
        print("[-] File export skipped.")

    print("\n[+] Thank you for using Stock Portfolio Tracker!\n")


if __name__ == "__main__":
    main()
