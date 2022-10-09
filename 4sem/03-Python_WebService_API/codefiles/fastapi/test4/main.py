from fastapi import FastAPI

app = FastAPI() # Create FastAPI object

# Create a dummy "database"
users = {
    "default" : {"Subject" : "Subject" , "Grade" : 0},
    "Peter Hansen" : {"Subject" : "Business" , "Grade" : 7},
    "Ulla Jensen" : {"Subject" : "Business" , "Grade" : 10},
    "Tue Hellstern" : {"Subject" : "Python" , "Grade" : 12},
}

@app.get("/") # Base path
def read_root():
    return {"Response": "Hi Kea students"}


@app.get("/user") # Path to get users information
def get_user_info(user: str = "default"):
    return {user : users[user]} # Return information of the specified user


# Start server
#

# Find info about one person
# http://localhost:8000/user?user=Tue%20Hellstern