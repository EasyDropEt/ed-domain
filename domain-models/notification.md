## Notification

```py
class Notification(TypedDict):
    id: str
    user_id: str
    type: str
    message: str
    timestamp: datetime
    read_status: bool
```

```json
{
  "id": "4001",
  "user_id": "00000000-0000-0000-0000-000000000004",
  "type": "order_update",
  "message": "Your order O1001 is now out for delivery.",
  "timestamp": "2024-12-26T10:00:00.000Z",
  "read_status": false
}
```
