from sqlalchemy.orm import Session
from . import models, schemas

def get_customer_by_id(db: Session, custid: int):
    return db.query(models.CustomerInfo).filter(models.CustomerInfo.cust_id == custid).first()


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_user = models.CustomerInfo(cust_name=customer.customername, cust_email=customer.customeremail, cust_mobil=customer.customermobil)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user