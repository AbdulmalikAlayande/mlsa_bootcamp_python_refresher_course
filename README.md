# OOP Inheritance & Polymorphism Assignment

Welcome to your next OOP assignment! This will focus on testing your understanding of **Inheritance** and **Polymorphism** in Python. You will be tasked with creating unique solutions that incorporate the core principles of Object-Oriented Programming (OOP).

Please ensure to complete both tasks in separate files, and demonstrate all required concepts through detailed coding and comments.

---

## Task 1: Inheritance Challenge

### 📘 Problem Statement

You are tasked with developing a **Library Management System** that showcases various levels of inheritance.

### 💻 Instructions

1. **Base Class: `LibraryItem`**

   - This class should have the following fields:
     - `title`: the title of the item.
     - `author`: the author or creator of the item.
     - `publication_year`: the year the item was published.
   - Methods:
     - `__str__`: Returns a formatted string representing the library item.

2. **Derived Classes:**

   - Create the following derived classes from `LibraryItem`:
     - **`Book`**:
       - Fields:
         - `genre`: the genre of the book.
         - `isbn`: a unique identifier for the book.
       - Methods:
         - `__str__`: Override the `__str__` method to include book-specific details.
     - **`Journal`**:
       - Fields:
         - `volume`: the volume number of the journal.
         - `issue`: the issue number of the journal.
       - Methods:
         - `__str__`: Override the `__str__` method to include journal-specific details.
     - **`Magazine`**:
       - Fields:
         - `issue_month`: the month of the issue.
         - `editor`: the editor of the magazine.
       - Methods:
         - `__str__`: Override the `__str__` method to include magazine-specific details.

3. **Create Advanced Inheritance:**

   - Add a class **`ReferenceBook`** that inherits from the `Book` class and represents books that cannot be borrowed.
   - Fields:
     - `reference_section`: the section in the library where it is stored.
   - Override the methods in `Book` to restrict certain functionalities like issuing the book.

4. **Test Cases:**
   - Create instances of `Book`, `Journal`, `Magazine`, and `ReferenceBook` and print their details.
   - Demonstrate how inheritance is applied and how methods are overridden to suit specific item types.

### 📂 Submission:

- Filename: `library_management.py`
- Include detailed comments explaining how each class and method demonstrates **Inheritance**.

---

## Task 2: Polymorphism Challenge

### 📘 Problem Statement

You are tasked with developing a **Payment Gateway System** that will simulate multiple payment methods and their behaviors.

### 💻 Instructions

1. **Base Class: `PaymentGateway`**

   - Fields:
     - `amount`: The amount of the transaction.
     - `currency`: The currency in which the transaction is being made.
   - Methods:
     - `process_payment()`: This is an abstract method that should be overridden by derived classes to process payments using different payment methods.

2. **Derived Classes:**

   - Create the following derived classes from `PaymentGateway`:
     - **`CreditCardPayment`**:
       - Fields:
         - `card_number`: The card number used for payment.
         - `cardholder_name`: Name of the cardholder.
         - `expiry_date`: Expiry date of the card.
       - Methods:
         - Override the `process_payment()` method to simulate credit card payment. Include checks for valid card number format.
     - **`PayPalPayment`**:
       - Fields:
         - `email`: The email address associated with the PayPal account.
       - Methods:
         - Override the `process_payment()` method to simulate PayPal payment. Simulate payment failure if the email is not in the correct format.
     - **`CryptocurrencyPayment`**:
       - Fields:
         - `wallet_address`: The cryptocurrency wallet address.
         - `crypto_type`: Type of cryptocurrency (e.g., Bitcoin, Ethereum).
       - Methods:
         - Override the `process_payment()` method to simulate cryptocurrency payment. Include validation for wallet address length.

3. **Polymorphism with `process_payment()`**

   - Create a list of payment objects (`CreditCardPayment`, `PayPalPayment`, and `CryptocurrencyPayment`) and iterate over the list.
   - For each object, call `process_payment()` and observe how each payment method behaves differently, even though you are calling the same method.

4. **Additional Polymorphism:**
   - Use the `__str__` method to return a formatted string for each payment method, showing the unique fields (e.g., card number for `CreditCardPayment`, email for `PayPalPayment`, etc.).
   - Demonstrate method overriding and polymorphism by creating a payment processor that can process payments with various methods dynamically.

### 📂 Submission:

- Filename: `payment_gateway.py`
- Include detailed comments explaining how each class and method demonstrates **Polymorphism**.

---

## 🎯 Bonus Task

1. For both the **Library Management System** and **Payment Gateway System**, implement **exception handling** to cover edge cases such as invalid input, missing values, etc.
2. Ensure that your code is well-documented using **docstrings** for each class and method.

---

## 📦 Submission Guidelines

- Make sure your code is clean and follows Python coding conventions (PEP 8).
- Add comments where necessary to explain your logic.
- **Testing**: Ensure your code runs without errors. Test it thoroughly with edge cases.
- Submit your completed assignment via GitHub by pushing your changes to the respective repository.

Good luck and have fun coding! 🚀
