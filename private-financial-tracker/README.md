# Personal Finance Tracker

A simple **command-line based Personal Finance Tracker** written in Python.
It allows you to:

* Add and store transactions (income or expense).
* View transactions within a given date range.
* Display summaries (total income, expenses, and net savings).
* Visualize transactions over time with a graph.

Inspired by: [Python Finance Tracker Tutorial](https://youtu.be/Dn1EjhcQk64?si=d_D5wjgz8GyMJgn6)

---

## Project Structure

```
project-folder/
│── main.py           # Main program (CLI and menu options)
│── data_entry.py     # Handles user input and validation
│── financial_data.csv # Auto-created CSV file storing transactions
│── README.md         # Documentation
```

---

## Requirements

Make sure you have **Python 3.8+** installed.

### Install Dependencies

```bash
pip install pandas matplotlib
```

---

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the program with:

   ```bash
   python main.py
   ```
4. Follow the menu prompts:

   * `1` → Add a new transaction
   * `2` → View transactions & summary (with optional graph)
   * `3` → Exit

---

## Usage Details

### Adding a Transaction

* Enter date in `dd-mm-yyyy` format (or press Enter for today's date).
* Enter the amount (must be greater than zero).
* Choose category:

  * `i` → Income
  * `e` → Expense
* Enter a description (optional).

Example:

```
Enter the date of the transaction (dd-mm-yyyy) or press 'enter' for today's date: 25-09-2025
Enter the amount of money: 1000
Enter the category ('i' for Income or 'e' for Expense): i
Enter a description (optional): Salary
```

### Viewing Transactions

* Enter a start and end date (format: `dd-mm-yyyy`).
* Program shows a list of transactions, totals, and net savings.
* Optionally display a **graph of income vs. expenses over time**.

---

## Example Graph

When selecting "Yes" for the graph option, you’ll see an interactive plot:

* **Green line** → Income
* **Red line** → Expense

---

## Features

* Saves data to `financial_data.csv`.
* Summarizes total income, expenses, and savings.
* Visualizes trends with matplotlib.
* Input validation for dates, amounts, and categories.

---

## Future Improvements

* Export filtered transactions to Excel/CSV.
* Support monthly/weekly summaries.
* Add more categories (e.g., Food, Rent, Utilities).

---
