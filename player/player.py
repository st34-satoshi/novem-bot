import json


class Player:
    """
    Random bot
    """

    def __init__(self):
        self.name = "Random_Bot"

    def make_room(self, ws):
        message = {'action': 'make-room',
                   'player_type': 'Row',  # Row or Column
                   'handicap': '-3',
                   'name': self.name}
        print(f'send: {message}')
        ws.send(json.dumps(message))
