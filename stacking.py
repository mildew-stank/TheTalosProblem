class TheTalosProblem:
    def __init__(self):
        self.world_space = []
        self.ERROR_INDEX = -1

    def initialize_world_space(self, number_of_boxes: int) -> None:
        """Sets world_space length to number_of_boxes, and all values to 1."""
        self.world_space = [1] * number_of_boxes

    def can_move_left(self, index: int) -> bool:
        """
        Checks if the player index can move left.

        The end of world_space or a stack of boxes Δ2 high returns False.
        """
        if index - 1 < 0:
            return False
        if self.world_space[index - 1] > self.world_space[index] + 1:
            return False
        return True

    def can_move_right(self, index: int, can_fall: bool = False) -> bool:
        """
        Checks if the player index can move right.

        The end of world_space, ground level,
        or a stack of boxes Δ2 low if can_fall = True returns False.
        """
        if index + 1 >= len(self.world_space):
            return False
        next_stack = self.world_space[index + 1]
        if next_stack <= 0:
            return False
        if can_fall:
            return True
        if next_stack < self.world_space[index] - 1 and next_stack > 0:
            return False
        return True

    def traverse_left(self, start_index: int) -> int:
        """
        Returns player index after moving as far left as possible.

        Returns ERROR_INDEX if something went wrong.
        """
        for index in range(start_index, -1, -1):
            if not self.can_move_left(index):
                return index
        return self.ERROR_INDEX

    def traverse_right(self, start_index: int, can_fall: bool = False) -> int:
        """
        Returns player index after moving as far right as possible.

        Returns ERROR_INDEX if something went wrong.
        """
        for index in range(start_index, len(self.world_space)):
            if not self.can_move_right(index, can_fall):
                return index
        return self.ERROR_INDEX

    def place_right_left(self, start_index: int) -> int:
        """
        Takes the rightmost box and drops it as far left as possible.

        Repeats until stuck, then returns player index.
        """
        start_index = self.traverse_right(start_index)  # start on the right.
        if not self.can_move_left(start_index):
            return start_index
        index = start_index
        while index > -1:
            index = self.traverse_right(index) - 1  # step off the target box.
            left_side = self.traverse_left(index)
            self.world_space[index + 1] -= 1  # pick up a box to the right,
            if not self.can_move_left(index):
                self.world_space[index + 1] += 1  # place it back down,
                return index
            self.world_space[left_side] += 1  # or place it to the far left.
            if not self.can_move_left(index):
                return index  # don't move the index if the box got us stuck.
            index -= 1
        return index

    def swap_left(self, start_index: int) -> int:
        """
        Takes the left box, moves left, drops the box right.

        Repeats until stuck or at the end of world_space,
        then returns player index.
        """
        for index in range(start_index, -1, -1):
            if index - 1 < 0:
                return index
            if self.can_move_left(index):
                continue
            delta = self.world_space[index - 1] - self.world_space[index]
            # if we run into a stack higher than Δ2, spread it out behind us.
            if delta > 2:
                for _ in range(delta - 1):
                    delta = self.world_space[index - 1] - self.world_space[index]
                    self.world_space[index - 1] -= 1
                    self.world_space[index + delta - 2] += 1
                continue
            self.world_space[index - 1] -= 1
            self.world_space[index] += 1  # it's safe to drop before moving left.
        return 0

    def get_max_height(self, boxes: int) -> int:
        """Returns max attainable height with a given number of boxes."""
        if boxes <= 0:
            self.world_space.clear()
            return self.ERROR_INDEX
        self.initialize_world_space(boxes)
        pos = boxes - 1
        peak = 0
        last_peak = -1
        last_pos = -1
        history = []
        while not (self.world_space in history):
            history.append(self.world_space.copy())
            pos = self.traverse_right(pos, True)
            while not (pos == last_pos == 0 and peak == last_peak):
                last_pos = pos
                last_peak = peak
                pos = self.place_right_left(pos)
                pos = self.swap_left(pos)
                peak = self.world_space[0]
        max_peak = -1
        snapshot_index = -1
        for index, snapshot in enumerate(history):
            if snapshot[0] > max_peak:
                max_peak = snapshot[0]
                snapshot_index = index
        self.world_space = history[snapshot_index]
        return max_peak

    def get_min_boxes(self, height: int) -> int:
        """Returns min amount of boxes required to reach a given height."""
        if height <= 0:
            self.world_space.clear()
            return self.ERROR_INDEX
        boxes = 0
        while self.get_max_height(boxes) < height:
            boxes += 1
        return boxes
