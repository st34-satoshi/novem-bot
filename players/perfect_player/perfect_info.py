import logging
import random


class PerfectInfo:
    """
    Save an optimal strategy for all states
    """

    def __init__(self, initial_state_number=None):
        self.initial_state_number = [[9, 5, 1],  # type A, top layer. bottom layer is 10 - top tile number
                                     [4, 3, 8],
                                     [2, 7, 6]]
        if initial_state_number is not None:
            self.initial_state_number = initial_state_number
        # state key = '012111210n1p3, the remaining tile number, n1/2: row/column is attacking, p = row - column point
        self.optimal_strategies = {}  # {state key: Strategy}

    def next_action(self, key, player_type):
        """
        :param key:
        :param player_type: Row or Column
        :return: 1, 2, or 3
        """
        if key not in self.optimal_strategies:
            logging.error(f"No state key. {key}")
            return None
        strategy = self.optimal_strategies[key]
        return strategy.next_action(player_type)


class Strategy:

    def __init__(self, row, column):
        self.row = row  # (0.5,0.4,0.1)
        self.column = column  # (0.4,0.4,0.2)

    def next_action(self, player_type):
        """
        :param player_type: Row or Column
        :return: 1, 2, or 3
        """
        strategy = self.row if player_type == "Row" else self.column
        logging.debug(f"optimal strategy = {strategy}")
        r = random.random()  # [0, 1]
        for i, s in enumerate(strategy):
            if r < s:
                return i + 1
            r -= s
        # In case r == 1
        return 3
