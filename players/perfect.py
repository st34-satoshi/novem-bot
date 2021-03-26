import pickle
import logging
import json
from players.player import Player
from config import PERFECT_FILE
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))


def load_perfect():
    logging.info("Loading perfect info")
    with open(PERFECT_FILE, mode='rb') as f:
        all_optimal = pickle.load(f)
    logging.info("finish loading")
    return all_optimal


class OptimalPlayer(Player):

    def __init__(self):
        super().__init__()
        self.name = "Perfect_Bot"
        self.all_optimal_strategy = load_perfect()

    def send_action(self, ws, receive_message):
        player_type = receive_message['type']  # Row or Column
        room_id = receive_message["room_id"]

        # generate key for perfect
        board = receive_message["board"]
        rounds = receive_message["round"]
        row_point = receive_message["row_point"]
        column_point = receive_message["column_point"]
        key = self.gen_key(board, int(rounds), int(row_point)-int(column_point))
        logging.debug(f"state key = {key}")

        action = self.all_optimal_strategy.next_action(key, player_type)

        if action is None:  # Error
            logging.error(f"perfect player has no strategy. key = {key}")
            return super().send_action(ws, receive_message)

        action = super().action_type(player_type) + str(action)
        message = {'action': 'play-action',
                   'room_id': room_id,
                   'play_action': action}
        logging.info(f'send: {message}')
        ws.send(json.dumps(message))

    @staticmethod
    def gen_board(str_board):
        """
        :param str_board: 159672834951438276
        :return: bottom and top
        """
        bottom = [[0 for _ in range(3)] for _ in range(3)]
        top = [[0 for _ in range(3)] for _ in range(3)]
        for i, c in enumerate(str_board):
            if i < 9:
                bottom[i // 3][i % 3] = c
            else:
                top[(i-9) // 3][(i-9) % 3] = c
        return bottom, top

    def gen_key(self, board, rounds, point_diff):
        # point_diff = row - column
        key = ""
        # board
        bottom, top = self.gen_board(board)
        for i in range(3):
            for j in range(3):
                if top[i][j] != '0':
                    key += "2"
                elif bottom != '0':
                    key += "1"
                else:
                    key += "0"
        logging.debug(f"gen key! {board, bottom, top, key}")
        # turn
        if rounds % 2 == 0:  # Row is attacking
            key += "n1"
        else:
            key += "n2"
        # point
        key += "p" + str(point_diff)
        return key


if __name__ == '__main__':
    load_perfect()
