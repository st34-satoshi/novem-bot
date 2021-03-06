import json
import logging
import random


class Player:
    """
    Random bot
    """

    def __init__(self):
        self.name = "Random_Bot"
        # This bot can play in some rooms at the same time
        self.players_type = {}  # {ws1: Row, ws2: Column} TODO: change to set

    def add_ws(self, ws, player_type):
        self.players_type[ws] = player_type

    def remove_ws(self, ws):
        logging.info(f"len ws = {len(self.players_type)}")
        logging.info(f"remove ws: {self.players_type.pop(ws)}")

    def send_make_room(self, ws):
        player_type = 'Row'
        message = {'action': 'make-room',
                   'player_type': player_type,  # Row or Column
                   'handicap': '-3',
                   'name': self.name}
        logging.info(f'send: {message}')
        ws.send(json.dumps(message))
        self.add_ws(ws, player_type)

    def send_action(self, ws, receive_message):
        player_type = self.players_type[ws]  # TODO: use type in receive_message
        room_id = receive_message["room_id"]
        action = self.action_type(player_type) + str(random.choice(["1", "2", "3"]))
        message = {'action': 'play-action',
                   'room_id': room_id,
                   'play_action': action}
        logging.info(f'send: {message}')
        ws.send(json.dumps(message))

    @staticmethod
    def action_type(player_type):
        if player_type == "Row":
            return 'r'
        return 'c'
