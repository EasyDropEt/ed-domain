## Driver

```py
class Driver(TypedDict):
    id: uuid
    name: str
    profile_picture:str
    license_number: str
    phone_number: str
    email: str
    location_id: str
    active_status: bool
    car_id: str
    assigned_delivery_jobs: List[str]
    notification_ids: List[str]
    payment_history: List[DriverPayment]

```

```json
{
  "id": "00000000-0000-0000-0000-000000000002",
  "name": "John Doe",
  "profile_picture":"www.example.com/profile_pic"
  "license_number": "DL123456789",
  "phone_number": "+9876543210",
  "email": "john.doe@example.com",
  "location_id": "10001",
  "active_status": true,
  "car_id": "C1001",
  "assigned_delivery_jobs": ["DJ1001", "DJ1002"],
  "notification_ids": ["2001", "2002"],
  "payment_history": [
    {
      "amount": 50.0,
      "status": "paid",
      "date": "2024-12-15T10:00:00.000Z",
      "payment_method": "PayPal"
    }
  ]
}
```
