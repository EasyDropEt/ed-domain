## Warehouse Worker

```py
class WarehouseWorker(TypedDict):
    id: str
    name: str
    phone_number: str
    email: str
    assigned_warehouse_id: str
    active_status: bool
    notification_ids: List[str]

```

```json
{
  "id": "00000000-0000-0000-0000-000000000003",
  "name": "Jane Doe",
  "phone_number": "+4567891230",
  "email": "jane.doe@example.com",
  "assigned_warehouse_id": "WH1001",
  "active_status": true,
  "notification_ids": ["3001"]
}
```
