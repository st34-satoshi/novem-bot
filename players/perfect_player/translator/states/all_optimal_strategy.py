from players.perfect_player.translator.states.all_state_value import AllStateValue
import logging


class AllOptimalStrategies(AllStateValue):

    def __init__(self, all_state):
        super().__init__()
        # load the computed result
        self.all_states = all_state.all_states
        self.initiate_state = all_state.initial_state
        self.optimal_strategies = {}  # {state_key: PerfectPlayer}

    def next_action(self, key, player_type):
        """
        :param key:
        :param player_type: Row or Column
        :return: 1, 2, or 3
        """
        if key not in self.optimal_strategies:
            logging.error(f"No state key. {key}")
            return None
        perfect_player = self.optimal_strategies[key]
        return perfect_player.next_action(player_type)

