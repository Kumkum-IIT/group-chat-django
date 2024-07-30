import asyncio
import websockets

async def hello(websocket):
    try:
        while True:
            name = await websocket.recv()
            print(f"<<< {name}")

            greeting = f"Hello {name}!"

            await websocket.send(greeting)
            print(f">>> {greeting}")
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally")
    except websockets.exceptions.ConnectionClosedError:
        print("Connection closed with an error")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())