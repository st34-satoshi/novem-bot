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


class Strategy:

    def __init__(self, row, column):
        self.row = row  # (0.5,0.4,0.1)
        self.column = column  # (0.4,0.4,0.2)
