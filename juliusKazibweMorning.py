import tkinter as tk


class InsufficientFundsError(Exception):
    pass


class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append("Deposit: +shs{:.2f}".format(amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append("Withdrawal: -shs{:.2f}".format(amount))

    def get_balance(self):
        self.transaction_history.append("Balance Inquiry")
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

    def clear_transaction_history(self):
        self.transaction_history = []


class BankingSystem:
    def __init__(self):
        self.customers = {}
        self.current_user = None

    def add_customer(self, username, password):
        if username not in self.customers:
            self.customers[username] = Customer(username, password)

    def authenticate(self, username, password):
        if username in self.customers and self.customers[username].password == password:
            self.current_user = username
            return True
        return False

    def logout(self):
        self.current_user = None

    def deposit(self, amount):
        if self.current_user:
            self.customers[self.current_user].deposit(amount)

    def withdraw(self, amount):
        if self.current_user:
            try:
                self.customers[self.current_user].withdraw(amount)
            except InsufficientFundsError:
                raise

    def get_balance(self):
        if self.current_user:
            return self.customers[self.current_user].get_balance()
        return 0.0

    def get_transaction_history(self):
        if self.current_user:
            return self.customers[self.current_user].get_transaction_history()
        return []

    def clear_transaction_history(self):
        if self.current_user:
            self.customers[self.current_user].clear_transaction_history()


banking_system = BankingSystem()


def authenticate_user():
    username = username_entry.get()
    password = password_entry.get()
    if banking_system.authenticate(username, password):
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        login_frame.pack_forget()
        banking_frame.pack()
        status_text.set("User authenticated. You can now perform transactions.")
    else:
        status_text.set("Invalid credentials. Please try again.")


def logout_user():
    banking_system.logout()
    banking_frame.pack_forget()
    receipt_frame.pack_forget()
    login_frame.pack()
    status_text.set("User logged out.")


def show_receipt():
    banking_frame.pack_forget()
    receipt_text.delete("1.0", tk.END)

    if banking_system.current_user is None:
        receipt_text.insert(tk.END, "Please log in first.\n")
        receipt_frame.pack()
        return

    # Generate receipt
    receipt = "Customer: {}\n\n".format(banking_system.current_user)
    receipt += "----- Receipt -----\n"

    operation = operation_var.get()

    if operation == "Deposit":
        amount_str = amount_entry.get()
        if amount_str.isdigit():
            amount = float(amount_str)
            banking_system.deposit(amount)
            receipt += "Operation: Deposit\nAmount: shs{:.2f}\n".format(amount)
            receipt += "New Balance: shs{:.2f}\n".format(banking_system.get_balance())
        else:
            receipt += "Invalid amount. Please enter a valid integer.\n"

    elif operation == "Withdraw":
        amount_str = amount_entry.get()
        if amount_str.isdigit():
            amount = float(amount_str)
            try:
                banking_system.withdraw(amount)
                receipt += "Operation: Withdrawal\nAmount: shs{:.2f}\n".format(amount)
                receipt += "New Balance: shs{:.2f}\n".format(
                    banking_system.get_balance()
                )
            except InsufficientFundsError:
                receipt += "Insufficient funds\n"
        else:
            receipt += "Invalid amount. Please enter a valid integer.\n"

    elif operation == "Balance Inquiry":
        receipt += "Operation: Balance Inquiry\n"
        receipt += "Balance: shs{:.2f}\n".format(banking_system.get_balance())

    elif operation == "Transaction History":
        receipt += "Operation: Transaction History\n"
        transaction_history = banking_system.get_transaction_history()
        if transaction_history:
            receipt += "----- Transaction History -----\n"
            for transaction in transaction_history:
                receipt += "{}\n".format(transaction)
        else:
            receipt += "No transaction history available.\n"

    receipt += "-------------------\n"

    receipt_text.insert(tk.END, receipt)
    receipt_frame.pack()


def back_to_banking():
    receipt_frame.pack_forget()
    banking_frame.pack()


# Create GUI window
window = tk.Tk()
window.title(" Julius Kazibwe Banking Receipt Program")

# Create login frame
login_frame = tk.Frame(window)

username_label = tk.Label(login_frame, text="Username:")
username_label.pack()

username_entry = tk.Entry(login_frame)
username_entry.pack()

password_label = tk.Label(login_frame, text="Password:")
password_label.pack()

password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=authenticate_user)
login_button.pack()

status_text = tk.StringVar()
status_label = tk.Label(login_frame, textvariable=status_text)
status_label.pack()

# Create banking frame
banking_frame = tk.Frame(window)

# Add customers to the banking system
banking_system.add_customer("user1", "password1")
banking_system.add_customer("user2", "password2")
banking_system.add_customer("user3", "password3")

operation_label = tk.Label(banking_frame, text="Operation:")
operation_label.pack()

operation_var = tk.StringVar(banking_frame)
operation_var.set("Deposit")  # Default operation

operation_menu = tk.OptionMenu(
    banking_frame,
    operation_var,
    "Deposit",
    "Withdraw",
    "Balance Inquiry",
    "Transaction History",
)
operation_menu.pack()

amount_label = tk.Label(banking_frame, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(banking_frame)
amount_entry.pack()


def update_amount_entry_state(*args):
    operation = operation_var.get()
    if operation == "Deposit" or operation == "Withdraw":
        amount_entry.config(state="normal")
    else:
        amount_entry.delete(0, tk.END)
        amount_entry.config(state="disabled")


operation_var.trace("w", update_amount_entry_state)

print_button_text = tk.StringVar()
print_button_text.set("Print Receipt ")


def update_button_text(*args):
    selected_operation = operation_var.get()
    print_button_text.set("Print " + selected_operation)


operation_var.trace("w", update_button_text)


print_button = tk.Button(
    banking_frame, textvariable=print_button_text, command=show_receipt
)
print_button.pack()

logout_button = tk.Button(banking_frame, text="Logout", command=logout_user)
logout_button.pack()

# Create receipt frame
receipt_frame = tk.Frame(window)

receipt_text = tk.Text(receipt_frame, height=15, width=45)
receipt_text.pack()

back_button = tk.Button(receipt_frame, text="Back to Banking", command=back_to_banking)
back_button.pack()

# Initial page: Login
login_frame.pack()

# Run the GUI event loop
window.mainloop()
