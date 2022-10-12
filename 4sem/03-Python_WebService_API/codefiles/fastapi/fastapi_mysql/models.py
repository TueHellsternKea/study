from sqlalchemy import Column, Integer, String
from sql_app.database import Base

class CustomerInfo(Base):
    __tablename__ = "customers"

    cust_id = Column(Integer, primary_key=True, index=True)
    cust_name = Column(String)
    cust_email = Column(String)
    cust_mobil = Column(String)