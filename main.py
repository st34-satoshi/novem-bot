import websocket
import json
import logging
from config import URI
from players.player import Player

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
PLAYER = Player()


def on_open(ws):
    logging.debug("opened")


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
        if message['is_terminal']:
            # The game is end. Close the connection and start a new connection
            logging.info("The game is end.")
            PLAYER.remove_ws(ws)
            ws.close()
            logging.info("Start a new connection")
            start_connection()
            return
        # return an action
        PLAYER.send_action(ws, message)


def on_close(ws):
    logging.debug("closed connection")


def start_connection():
    webs = websocket.WebSocketApp(URI,
                                  on_open=on_open,
                                  on_message=on_message,
                                  on_close=on_close)
    webs.run_forever()


if __name__ == '__main__':
    start_connection()
