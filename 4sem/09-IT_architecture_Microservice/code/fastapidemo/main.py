from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Kea"}

@app.get("/nosqldata")
async def root():
    return {"message": "NoSql Data"}

@app.get("/mysqldata")
async def root():
    return {"message": "MySql Data"}

