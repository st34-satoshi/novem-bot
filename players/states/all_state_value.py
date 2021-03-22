class AllStateValue:
    """
    save all states as dictionary (key, state)
    """

    def __init__(self):
        self.all_states = {}  # dictionary of {key, state}

    def get_value(self, state):
        # state is state class
        key = state.get_key()
        return self.all_states[key].get_value()
