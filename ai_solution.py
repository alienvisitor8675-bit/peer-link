```python
from datetime import datetime

class EasypaisaAdapter:
    def get_manifest(self):
        return {
            "name": "Easypaisa",
            "version": "1.0.0",
            "description": "Easypaisa adapter for PKR transfers."
        }

    def get_payees(self):
        return [
            {
                "id": "easypaisa_12345678",
                "name": "John Doe",
                "mobile": "+1234567890"
            },
            {
                "id": "easypaisa_987654321",
                "name": "Jane Smith",
                "mobile": "+1234567891"
            }
        ]

    def make_payment(self, payer_id, payee_id, amount, currency):
        return {
            "status": "success",
            "transaction_id": f"easypaisa_{datetime.now().isoformat()}",
            "payer": payer_id,
            "payee": payee_id,
            "amount": amount,
            "currency": currency,
            "timestamp": datetime.now().isoformat(),
            "time_zone": "UTC"
        }

# Example test cases
TEST_TRANSFER = {
    "payer": "easypaisa_12345678",
    "payee": "easypaisa_987654321",
    "amount": "100.00",
    "currency": "PKR"
}

NEGATIVE_TEST = {
    "payer": "easypaisa_12345678",
    "payee": "easypaisa_12345678",  # Same as payer
    "amount": "100.00",
    "currency": "PKR"
}
```