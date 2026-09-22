# CodeAlpha Internship - Task 2: Stock Portfolio Tracker

A simple and robust Python-based **Stock Portfolio Tracker** that calculates the total investment value based on hardcoded stock prices and user inputs.

---

## 📌 Project Overview

- **Goal:** Build a simple stock tracker that calculates total investment based on manually defined stock prices.
- **Key Concepts Used:**
  - `Dictionaries` for storing stock price lookup tables and portfolio data.
  - `Input / Output` handling with validation for share quantities and stock symbols.
  - `Basic Arithmetic` for calculating individual holding values and overall portfolio worth.
  - `File Handling` to optionally export the portfolio summary to `.csv` or `.txt` format.

---

## 🚀 Features

1. **Predefined Stock Prices:** Hardcoded price dictionary for popular stocks (`AAPL`, `TSLA`, `MSFT`, `GOOGL`, `AMZN`, `NVDA`, `META`, `NFLX`).
2. **Interactive CLI:** Add stocks interactively by typing the symbol and the quantity of shares owned.
3. **Input Validation:** Handles invalid ticker symbols and non-numeric / non-positive quantities gracefully.
4. **Summary Breakdown:** Displays a formatted table with symbol, shares owned, price per share, total holding value, and overall grand total.
5. **File Export:** Save summary reports to `.csv`, `.txt`, or both with timestamp tracking.

---

## 🛠️ How to Run

### 1. Prerequisites
Ensure you have Python 3.x installed.

### 2. Run the Script
Open your terminal in this directory and execute:
```bash
python stock_portfolio_tracker.py
```

---

## 💻 Example Output

```text
#######################################################
   STOCK PORTFOLIO TRACKER (CODEALPHA TASK 2)
#######################################################

=============================================
        AVAILABLE STOCKS & PRICES (USD)
=============================================
Symbol     |          Price per Share ($)
---------------------------------------------
AAPL       | $             180.50
AMZN       | $             185.00
GOOGL      | $             175.25
META       | $             505.30
MSFT       | $             420.75
NFLX       | $             640.20
NVDA       | $             125.80
TSLA       | $             250.00
=============================================

[*] Enter your stocks below. Type 'DONE' when finished.

Enter Stock Symbol (e.g. AAPL, TSLA) or 'DONE': AAPL
Enter quantity of shares for AAPL: 10
[+] Added 10 share(s) of AAPL to your portfolio.
---------------------------------------------
Enter Stock Symbol (e.g. AAPL, TSLA) or 'DONE': TSLA
Enter quantity of shares for TSLA: 5
[+] Added 5 share(s) of TSLA to your portfolio.
---------------------------------------------
Enter Stock Symbol (e.g. AAPL, TSLA) or 'DONE': DONE

=================================================================
                 PORTFOLIO SUMMARY REPORT
=================================================================
Stock      | Shares     | Price ($)       | Total Value ($)
-----------------------------------------------------------------
AAPL       | 10         | $180.50         | $1805.00       
TSLA       | 5          | $250.00         | $1250.00       
=================================================================
TOTAL PORTFOLIO INVESTMENT:            | $3055.00       
=================================================================

Save Report Options:
  1. Save as CSV file (.csv)
  2. Save as Text file (.txt)
  3. Save both (.csv & .txt)
  4. Skip saving

Enter your choice (1-4): 1
[+] Successfully saved portfolio report to: portfolio_summary.csv
```
