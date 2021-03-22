import websocket
import json
from player.player import Player

PLAYER = Player()


def on_open(ws):
    print("opened")


def on_message(ws, message):
    message = json.loads(message)
    print(message)
    print(type(message))
    if 'action' not in message:
        print(f"no action in the message. {message}")
        return
    if message['action'] == 'room_list':
        # initial message
        # make a room for this bot
        print("make a room")
        PLAYER.make_room(ws)


def on_close(ws):
    print("closed connection")


if __name__ == '__main__':
    socket = "ws://localhost:8080/ws-novem"
    ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)
    ws.run_forever()
