import asyncio
import websockets
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)

async def echo_handler(websocket, path):
    """
    Handles a single WebSocket connection.
    path is typically used for routing but is ignored here.
    """
    logging.info(f"Client connected from {websocket.remote_address}")
    try:
        async for message in websocket:
            logging.info(f"Received message: {message}")
            # Echo the message back to the client
            await websocket.send(f"Server echo: {message}")
    except websockets.exceptions.ConnectionClosedError:
        logging.info(f"Connection closed by client from {websocket.remote_address}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

async def main():
    # Set up the server to listen on all interfaces (0.0.0.0) and port 8765
    async with websockets.serve(echo_handler, "0.0.0.0", 8765):
        logging.info("WebSocket server started and listening on ws://0.0.0.0:8765")
        # Run forever to keep the server alive
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())
