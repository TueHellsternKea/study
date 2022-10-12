from typing import List
from pydantic import BaseModel


class CustomerInfoBase(BaseModel):
    customerid: int
    customername: str
    customeremail: str
    customermobil: str


class CustomerCreate(CustomerInfoBase):
    password: str


class CustomerInfo(CustomerInfoBase):
    id: int

    class Config:
        orm_mode = True