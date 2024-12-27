## Driver Payment

```py
class DriverPayment(TypedDict):
    amount: float
    status: str
    date: datetime
    payment_method: str
```

```json
{
  "amount": 50.0,
  "status": "paid",
  "date": "2024-12-15T10:00:00.000Z",
  "payment_method": "PayPal"
}
```
