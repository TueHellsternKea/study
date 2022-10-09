from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from sql_app import models, schemas, crud
from sql_app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/customer", response_model=schemas.CustomerInfo)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_id(db, customerid=customer.  user.username)
    if db_customer:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_customer(db=db, user=user)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)