```py
class DeliveryJob(TypedDict):
    id: str
    order_ids: List[str]
    route: Route
    driver_id: str
    driver_payment: DriverPayment
    status: str
    estimated_completion_time: datetime

```

```json
{
  "id": "00000000-0000-0000-0000-000000000002",
  "order_ids": ["00000000-0000-0000-0000-000000000002", "00000000-0000-0000-0000-000000000002"],
  "route": {
    "waypoints": [
      {
        "location_id": "00000000-0000-0000-0000-000000000001",
        "eta": "2024-12-26T14:00:00.000Z",
        "sequence": 1
      },
      {
        "location_id": "00000000-0000-0000-0000-000000000002",
        "eta": "2024-12-26T16:00:00.000Z",
        "sequence": 2
      }
    ],
    "total_distance": 20.5,
    "total_time": 2.5
  },
  "driver_id": "00000000-0000-0000-0000-000000000002",
  "driver_payment": {
    "amount": 25.0,
    "status": "pending",
    "date": "2024-12-26T10:00:00.000Z",
    "payment_method": "Bank Transfer"
  },
  "status": "in_progress",
  "estimated_completion_time": "2024-12-26T18:00:00.000Z"
}
```
