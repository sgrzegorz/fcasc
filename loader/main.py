from websocket import create_connection
import time

# Time to feed single file in seconds
timeout = 5

ws = create_connection("wss://ws-feed.exchange.coinbase.com")
ws.send(
    """{
    "type": "subscribe",
    "product_ids": [
        "ETH-USD"],
    "channels": [
        "level2",
        "heartbeat",
        {
            "name": "ticker",
            "product_ids": [
                "ETH-USD"]
        }
    ]
}
"""
)
filename = f"data_{time.time()}.txt"
f = open(filename, "a")
print ("Sent")
print ("Receiving...")
start = time.time()
while True:
    result = ws.recv()
    f.write(result + '\n')
    if (time.time() - start > timeout):
        print(f"Creating new file {filename}")
        f.close()
        filename = f"data_{time.time()}.txt"
        f = open(filename, "a")
        start = time.time()
ws.close()
