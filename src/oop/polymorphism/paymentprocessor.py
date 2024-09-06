def skip_lines():
    for _ in range(3):
        print()


class PaymentProcessor:
    """
    A class that handles payment processing using a specific payment method.
    """

    def __init__(
        self,
        payment_method: "PaymentMethod",
        payment_reference: str,
        transaction_fee: float,
    ) -> None:
        """
        Initializes the payment processor with a payment method, payment reference, and transaction fee.

        Args:
            payment_method (PaymentMethod): The payment method to be used (e.g., CreditCard, BankTransfer).
            payment_reference (str): A unique reference ID for tracking the transaction.
            transaction_fee (float): The fee charged for processing the transaction.
        """
        self._payment_method = payment_method
        self.payment_reference = payment_reference
        self.transaction_fee = transaction_fee

    def process_payment(self) -> str:
        """
        Processes the payment by invoking the execute_transaction method of the payment method.

        Returns:
            str: A confirmation message from the payment method.
        """
        confirmation = self._payment_method.execute_transaction()
        return f"Transaction with reference {self.payment_reference} processed. {confirmation}"


class PaymentMethod:
    """
    A base class for all payment methods.
    """

    def __init__(self, currency: str, payment_date: str) -> None:
        """
        Initializes the payment method with a currency and a payment date.

        Args:
            currency (str): The currency in which the payment is made (e.g., USD, EUR).
            payment_date (str): The date when the payment is made.
        """
        self.currency = currency
        self.payment_date = payment_date

    def execute_transaction(self) -> str:
        """
        A placeholder method that should be overridden by specific payment methods.

        Returns:
            str: A message indicating that the payment method should be specified.
        """
        return "Payment method not specified."

    def __str__(self) -> str:
        """
        Returns a string representation of the payment method.
        """
        return f"Payment in {self.currency} on {self.payment_date}"


class CreditCard(PaymentMethod):
    """
    A class representing credit card payments.
    """

    def execute_transaction(self) -> str:
        """
        Simulates executing a credit card transaction.

        Returns:
            str: A confirmation message for the credit card payment.
        """
        return (
            f"Credit card payment processed in {self.currency} on {self.payment_date}."
        )


class BankTransfer(PaymentMethod):
    """
    A class representing bank transfer payments.
    """

    def execute_transaction(self) -> str:
        """
        Simulates executing a bank transfer.

        Returns:
            str: A confirmation message for the bank transfer payment.
        """
        return f"Bank transfer processed in {self.currency} on {self.payment_date}."


class CryptoCurrency(PaymentMethod):
    """
    A class representing cryptocurrency payments.
    """

    def execute_transaction(self) -> str:
        """
        Simulates executing a cryptocurrency transaction.

        Returns:
            str: A confirmation message for the cryptocurrency payment.
        """
        return f"Cryptocurrency transaction processed with {self.currency} on {self.payment_date}."


print("================Credit Card Usage================")

# Credit Card Usage:
credit_card = CreditCard(currency="USD", payment_date="2024-08-31")
credit_card_processor = PaymentProcessor(
    payment_method=credit_card, payment_reference="TXN12345", transaction_fee=2.5
)

credit_card_transaction_result = credit_card_processor.process_payment()
print(credit_card_transaction_result)

skip_lines()

print("================Crypto Currency Usage================")

# Crypto Currency Usage:
cryptoCurrency = CryptoCurrency(currency="Solana", payment_date="2024-06-09")
crypto_processor = PaymentProcessor(
    payment_method=cryptoCurrency, payment_reference="FGY78HYIU9", transaction_fee=3.0
)
crypto_transaction_result = cryptoCurrency.execute_transaction()
print(crypto_transaction_result)

skip_lines()

print("================Bank Transfer Usage================")

# Bank Transfer Usage:
bank_transfer = BankTransfer(currency="EUR", payment_date="2024-07-15")
bank_transfer_processor = PaymentProcessor(
    payment_method=bank_transfer, payment_reference="BT12345678", transaction_fee=1.5
)

bank_transfer_transaction_result = bank_transfer_processor.process_payment()
print(bank_transfer_transaction_result)

skip_lines()

print("================Usage without specifying any transaction method================")

# Usage without specifying any transaction method:
generic_payment = PaymentMethod(currency="USD", payment_date="2024-09-01")
generic_processor = PaymentProcessor(
    payment_method=generic_payment, payment_reference="GENERIC123", transaction_fee=0.0
)

generic_transaction_result = generic_processor.process_payment()
print(generic_transaction_result)

skip_lines()
