import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

async def hello_client():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            message = input("Enter your message ")
            await websocket.send(message)
            logging.info(f"Sent: {message}")
            
            response = await websocket.recv()
            logging.info(f"Received: {response}")
    except ConnectionRefusedError:
        logging.error("Connection refused. Make sure the server is running.")

if __name__ == "__main__":
    asyncio.run(hello_client())

