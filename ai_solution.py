```python
# Peer Link targeted rewards allocation

allocation = {
    "Monobank": {
        "max": 50,
        "scope": """One UAH transfer adapter, tests, docs and one authorized live report; account owner needed."""
    },
    "Vietcombank": {
        "max": 50,
        "scope": """One VND Digibank transfer adapter, tests, docs and one authorized live report; lead must reconfirm scope and payout eligibility."""
    },
    "Chase": {
        "max": 25,
        "scope": """Bounded feasibility and field-provenance package for one US transfer surface."""
    },
    "Bank of America": {
        "max": 25,
        "scope": """Same bounded feasibility scope."""
    },
    "Wells Fargo": {
        "max": 25,
        "scope": """Same bounded feasibility scope."""
    }
}

total_allocated = sum([v["max"] for v in allocation.values()])
print(f"Total allocated: ${total_allocated}")
```