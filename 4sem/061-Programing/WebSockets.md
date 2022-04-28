# WebSockets
A WebSocket is a standard protocol for two-way data transfer between a *client* and *server*. The WebSockets protocol **does not run over HTTP**, instead it is a separate implementation **on top of TCP**.

WebSockets enable a **bidirectional**, **full-duplex** communications channel that functions over HTTP.

# Example in Python
We create a "server" and a "client".

You have to install

    pip3 install websockets

## Server
```python
import asyncio
import websockets
 
# Create handler for each connection
async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"
    await websocket.send(reply)
 
start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server) 
asyncio.get_event_loop().run_forever()
```


## Client 
```python
# Modules
import asyncio
import websockets
 
async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send("hello")
        response = await websocket.recv()
        print(response + " From server")
 
asyncio.get_event_loop().run_until_complete(test())
```


# Link
- [websockets.readthedocs.io/en/stable/](https://websockets.readthedocs.io/en/stable/)
- [pypi.org/project/websockets/](https://pypi.org/project/websockets/)