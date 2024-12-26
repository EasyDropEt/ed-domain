## Cunsumer

```py
class Consumer(TypedDict):
    id: str
    name: str
    role: str
    phone_number: str
    email: str
    active_status: bool
    notification_ids: List[str]

```

```json
{
  "id": "00000000-0000-0000-0000-000000000004",
  "name": "Alice Johnson",
  "role": "consumer",
  "phone_number": "+6543219870",
  "email": "alice.johnson@example.com",
  "active_status": true,
  "notification_ids": ["4001", "4002"]
}
```
