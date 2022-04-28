# Modules
import asyncio
import websockets
 
async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send("hello")
        response = await websocket.recv()
        print(response + " From server")
 
asyncio.get_event_loop().run_until_complete(test())