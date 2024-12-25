## Order

```py
class Order(TypedDict):
    id: str
    consumer: Consumer
    business_id: str
    bill_id: str
    latest_time_of_delivery: datetime
    parcel: Parcel
```

```json
{
    "id": "00000000-0000-0000-0000-000000000000",
    "consumer": {
        "name": "John Doe",
        "phone_number": "+1234567890",
        "location_id": "00000000-0000-0000-0000-000000000000"
    },
    "business_id": "00000000-0000-0000-0000-000000000000",
    "bill_id": "00000000-0000-0000-0000-000000000000",
    "latest_time_of_delivery": "2024-11-26T18:35:53.000Z",
    "parcel": {
        "size": "small",
        "weight": 1.5,
        "dimensions": {
            "length": 10,
            "width": 10,
            "height": 10
        }
    }
}
```
