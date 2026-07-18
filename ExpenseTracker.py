# Simple Expense Tracker in Python
expenses = []
total_spent = 0

def show_menu():
    print("\n=== Expense Tracker  ===")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. View All Expenses")
    print("4. Quit")

def add_expense():
    global total_spent
    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print(" Amount must be positive!")
            return
        
        description = input("Enter description (optional): ").strip()
        
        expenses.append({"amount": amount, "description": description})
        total_spent += amount
        
        print(f" Added: {amount:.2f} - {description if description else 'Expense'}")
    except ValueError:
        print(" Please enter a valid number!")

def view_total():
    print(f"\n Total Spent: {total_spent:.2f}")

def view_all_expenses():
    if not expenses:
        print(" No expenses recorded yet!")
    else:
        print("\n All Expenses:")
        for i, exp in enumerate(expenses, 1):
            desc = exp['description'] if exp['description'] else "No description"
            print(f"{i}. ₹{exp['amount']:.2f} - {desc}")

# Main Program
print("Welcome to Expense Tracker! ")

while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total()
    elif choice == "3":
        view_all_expenses()
    elif choice == "4":
        print(f"\nFinal Total Spent: ₹{total_spent:.2f}")
        print(" Thank you for using Expense Tracker!")
        break
    else:
        print(" Invalid choice! Please enter 1, 2, 3, or 4.")