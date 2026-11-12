# Stock Portfolio Tracker

A small command-line Python project that estimates the value of a stock portfolio using predefined sample prices.

## Features

- Supports AAPL, TSLA, MSFT, GOOGL, and AMZN.
- Calculates each holding's value and the total portfolio value.
- Saves the summary to `portfolio_summary.csv`.

## Requirements

- Python 3
- No third-party packages

## Run

From this directory, run:

```bash
python stock_tracker.py
```

On Windows, you can also use:

```powershell
py stock_tracker.py
```

Enter the number of stocks to add, then provide each supported symbol and a positive quantity.

## Prices and output

Prices are hard-coded sample values in USD; they are not live market data. Edit the `stock_prices` dictionary in `stock_tracker.py` to change them.

Each run replaces `portfolio_summary.csv` with the current holdings and a total row. This repository is public, so do not commit personal portfolio data.
