## Business

```py
class Business(TypedDict):
    id: str
    name: str
    owner_name: str
    email: str
    phone_number: str
    address: str
    registration_date: datetime
    active_status: bool
    billing_details: str
    notification_ids: List[str]
```

```json
{
  "id": "00000000-0000-0000-0000-000000000001",
  "name": "Tech Supplies Co.",
  "owner_name": "Alice Smith",
  "email": "alice@techsupplies.com",
  "phone_number": "+1234567890",
  "address": "123 Tech Park, Silicon Valley, CA",
  "registration_date": "2024-01-15T10:00:00.000Z",
  "active_status": true,
  "billing_details": "Bank Transfer",
  "notification_ids": ["1001", "1002"]
}
```
