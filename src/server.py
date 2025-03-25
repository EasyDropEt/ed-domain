import uvicorn
from fastapi import FastAPI

from domain.entities import (
    Business,
    Car,
    Consumer,
    DeliveryJob,
    Driver,
    DriverPayment,
    Location,
    Notification,
    Order,
    Route,
    User,
    WarehouseWorker,
)

app = FastAPI(title="domain-models", description="domain models API")


@app.get("/business", response_model=Business)
def business(): ...


@app.get("/car", response_model=Car)
def car(): ...


@app.get("/consumer", response_model=Consumer)
def consumer(): ...


@app.get("/delivery_job", response_model=DeliveryJob)
def delivery_job(): ...


@app.get("/driver", response_model=Driver)
def driver(): ...


@app.get("/driver_payment", response_model=DriverPayment)
def driver_payment(): ...


@app.get("/location", response_model=Location)
def location(): ...


@app.get("/notification", response_model=Notification)
def notification(): ...


@app.get("/order", response_model=Order)
def order(): ...


@app.get("/route", response_model=Route)
def route(): ...


@app.get("/user", response_model=User)
def user(): ...


@app.get("/warehouse_worker", response_model=WarehouseWorker)
def warehouse_worker(): ...


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
