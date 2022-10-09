#
from fastapi import FastAPI, status, HTTPException, Depends


# Initialize app
app = FastAPI()

@app.get("/")
def root():
    return "Kea demo"


@app.route('/weather')
def weather():
    city = request.args.get('city')
    if city.isdigit():
        res = "City name must be string e.g. 'Amsterdam, Berlin'"
        return res
    response = requests.get("http://weather:3002/weather?city="+ city)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Run server 
# 

# Get weather - http://localhost/weather?city=amsterdam