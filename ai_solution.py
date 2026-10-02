```javascript
// banks/vn/vietcombank/adapter.js
const VietcombankAdapter = {
  id: 'vietcombank',
  name: 'Vietcombank',
  supportedTypes: ['VND'],
  getTransactions: async (params) => {
    return {
      success: true,
      transactions: [
        {
          id: 'VNTX000000123',
          currency: 'VND',
          amount: 50000,
          date: '2024-01-01',
          status: 'Cleared',
          payee: 'John Doe',
          payer: 'Jane Smith'
        }
      ]
    };
  }
};

// banks/vn/vietcombank/manifest.json
{
  "name": "Vietcombank",
  "adapter": "VietcombankAdapter",
  "version": "1.0.0",
  "description": "Adapter for Vietcombank VND transactions."
}

// banks/vn/vietcombank/acquisition-notes.md
- VND is used without minor units.
- Transactions are captured as objects with the specified properties.
- Status is returned as 'Cleared' for completed transactions.
```