import pandas 
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt



class CSV:
    CSV_FILE = "financial_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    date_format = "%d-%m-%Y"

    @classmethod
    def initialiaze_csv(cls):
        try:
            pandas.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            data_frame = pandas.DataFrame(columns=cls.COLUMNS)
            data_frame.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Data added successfully!")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        data_frame = pandas.read_csv(cls.CSV_FILE)
        data_frame["date"] = pandas.to_datetime(data_frame["date"], format=CSV.date_format)
        start_date = datetime.strptime(start_date, CSV.date_format)
        end_date = datetime.strptime(end_date, CSV.date_format)

        mask = (data_frame["date"] >= start_date) & (data_frame["date"] <= end_date)
        filtered_dataFrame = data_frame.loc[mask]

        if filtered_dataFrame.empty:
            print(f"No transactions found within the date range")
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.date_format)} to {end_date.strftime(CSV.date_format)}"
                )
            print(
                filtered_dataFrame.to_string(index=False, formatters={"date": lambda x:x.strftime(CSV.date_format)})
            )

            total_income = filtered_dataFrame[filtered_dataFrame["category"] == "Income"]["amount"].sum()
            total_expense = filtered_dataFrame[filtered_dataFrame["category"] == "Expense"]["amount"].sum()

            print("\n")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

            return filtered_dataFrame


def add_function():
    CSV.initialiaze_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press 'enter' for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def graph_transaction(data_frame):
    data_frame.set_index("date", inplace=True)

    income_dataFrame = (
        data_frame[data_frame["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(data_frame.index, fill_value=0)
    ) #make row for each date for missing date
    expense_dataFrame = (
        data_frame[data_frame["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(data_frame.index, fill_value=0)
    ) #make row for each date for missing date

    plt.figure(figsize=(15,6)) #size of the screen
    plt.plot(income_dataFrame.index, income_dataFrame["amount"], label="Income", color="g")
    plt.plot(expense_dataFrame.index, expense_dataFrame["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Incomes and Expenses Graph")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    is_running = True
    while is_running:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit the program")
        choice = input("Enter your choice (1-3): ").strip()
        print("\n")

        if choice == "1":
            add_function()

        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            print("\n")
            data_frame = CSV.get_transactions(start_date, end_date)
            if input("Do you want to display the graph? (y/n): ").lower().strip() == "y":
                graph_transaction(data_frame)

        elif choice == "3":
            print("Exiting the program...")
            is_running = False
        else: 
            print("Invalid choice. Please enter between 1,2, or 3.")

if __name__ == "__main__":
    main()