import random
import logging


class PerfectPlayer:

    def __init__(self, key, row=None, column=None):
        self.key = key  # state key
        # An optimal strategy
        self.row_strategy = row
        self.column_strategy = column
        # sum of the probability is 1. probability to reach the result from this state
        # Value for the first (row) player
        self._win_probability = 0
        self._draw_probability = 0
        self._loss_probability = 0
        self._livelock_draw_probability = 0
        self.__done = False  # after computing this probability --> True

    def next_action(self, player_type):
        """
        :param player_type: Row or Columne
        :return: 1, 2, or 3
        """
        strategy = self.row_strategy if player_type == "Row" else self.column_strategy
        logging.debug(f"optimal strategy = {strategy}")
        r = random.random()
        for i, s in enumerate(strategy):
            if r < s:
                return i + 1
            r -= s
        return 3
