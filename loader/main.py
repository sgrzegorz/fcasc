from websocket import create_connection
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
print ("Sent")
print ("Receiving...")
result =  ws.recv()
print (f"Received {result}")
import time
while True:
    # time.sleep(3)
    result = ws.recv()
    print(result)
ws.close()
