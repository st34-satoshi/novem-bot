import pickle
import logging
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from players.translator.states import all_optimal_strategy
from players.translator.states import slack
from players.translator.t_config import SOLVING_RESULT
from config import PERFECT_FILE
from players.perfect_player.perfect_info import PerfectInfo, Strategy
sys.modules['states.all_optimal_strategy'] = all_optimal_strategy
sys.modules['slack'] = slack
logging.basicConfig(level=logging.INFO)


def load_perfect():
    logging.info("Loading perfect info")
    with open(SOLVING_RESULT, mode='rb') as f:
        all_optimal = pickle.load(f)
    logging.info("finish loading")
    return all_optimal


def translate(all_optimal):
    """
    Translate from the pickle result of solving Novem to PerfectInfo
    :param all_optimal:
    :return:

    state key = '012111210n1p3, the remaining tile number, n1/2: row/column is attacking, p = row - column point
    """
    logging.info("start translating")
    perfect_info = PerfectInfo()

    # translate
    for key, perfect in all_optimal.optimal_strategies.items():
        row_strategy = perfect.row_strategy
        column_strategy = perfect.column_strategy
        perfect_info.optimal_strategies[key] = Strategy(row_strategy, column_strategy)

    logging.info("finish translating")

    logging.info("start saving as pickle")
    # save
    with open(PERFECT_FILE, mode='wb') as f:
        pickle.dump(perfect_info, f)


if __name__ == '__main__':
    solving_result = load_perfect()
    translate(solving_result)
