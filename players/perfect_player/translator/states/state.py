class State:

    def __init__(self, all_state, p1_point, p2_point, next_player):
        # the number. if no plate, 0  ex[[1, 1, 2], [0, 0, 1], [2, 2, 2]] 0:nothing, 1:1number, 2:2numbers
        self.all_state = all_state
        self.p1_point = p1_point
        self.p2_point = p2_point
        self.next_player = next_player  # p1 tern if True else p2 tern
        # the list of each next state value. if not decided the value is None
        self.all_value = [[None, None, None], [None, None, None], [None, None, None]]
        self.this_state_value = None  # value for p1 player
        self.key = None
        # self.key = self.gen_key()

        self.children_keys = None  # list of next states key(str) without pair state. this is computed at self.next_reachable_states method
        self.pair_key = None
        self.children_key_list = None  # list of 3*3. save each child
        self.has_empty = None
        self.is_terminal = None
        # self.has_empty = self.has_empty_tile()
        # self.is_terminal = self.is_end_game()

