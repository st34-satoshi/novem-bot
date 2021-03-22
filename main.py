import websocket
import json
import logging
from config import URI
# You can choose a player
from player.player import Player

logging.basicConfig(level=logging.INFO)
PLAYER = Player()


def on_open(ws):
    print("opened")


def on_message(ws, message):
    message = json.loads(message)
    logging.info(f"receive = {message}")
    if 'action' not in message:
        logging.WARNING(f"no action in the message. {message}")
        return
    if message['action'] == 'room_list':
        # initial message
        # make a room for this bot
        logging.info("make a room")
        PLAYER.send_make_room(ws)
    elif message['action'] == 'playing':
        # return an action
        PLAYER.send_action(ws, message)


def on_close(ws):
    print("closed connection")


if __name__ == '__main__':
    webs = websocket.WebSocketApp(URI,
                                  on_open=on_open,
                                  on_message=on_message,
                                  on_close=on_close)
    webs.run_forever()
