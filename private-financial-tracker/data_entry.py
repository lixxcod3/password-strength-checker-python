from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"i": "Income", "e": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter date in 'dd-mm-yyyy' format")

def get_amount():
    try: 
        amount = float(input("Enter the amount of money: "))
        if amount <= 0:
            raise ValueError("Invalid amount. Amount must not be a negative or zero value")
        return amount
    except ValueError as value_error:
        print(value_error)
        return get_amount()


def get_category():
    category = input("Enter the category ('i' for Income or 'e' for Expense): ").lower()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'i' for Income or 'e' for Expense")
    return get_category()

def get_description():
    description = input("Enter a description (optional): ").strip()
    if description == "":
        return "-"
    return description