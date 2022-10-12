# Import
from fastapi import FastAPI

# Define an API object
app = FastAPI()

# Map HTTP method and path to python function
@app.get("/")
async def root():
    return {"message": "Hello Kea students. Welcome to the FastAPI page!"}

@app.get("/newendpoint")
async def function_demo_get():
    return {"message": "This is /newendpoint endpoint"}


# Start the FastAPI application (on command line)
# uvicorn main:app --reload