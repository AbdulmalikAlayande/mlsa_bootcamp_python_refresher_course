"""
Problem Statement:

You are tasked with designing a Payment Processor that can handle multiple payment methods such as:

    CreditCard
    BankTransfer
    CryptoCurrency

All payment methods should implement a standard method process_payment() but may have different ways of processing the payment based on their unique requirements.

Your task is to:

    Create a PaymentMethod base class with a process_payment() method.
    Implement child classes for CreditCard, BankTransfer, and CryptoCurrency that override the process_payment() method.
    Write a function that takes any payment method and calls the process_payment() method, demonstrating polymorphism.
"""
