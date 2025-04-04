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

    def can_move_right(self, index: int) -> bool:
        """
        Checks if the player index can move right.

        The end of world_space, a stack of boxes Δ2 low,
        or ground level returns False.
        """
        if index + 1 >= len(self.world_space):
            return False
        if self.world_space[index + 1] < self.world_space[index] - 1:
            return False
        if self.world_space[index + 1] <= 0:
            return False
        return True

    def traverse_left(self, start_index: int) -> int:
        """
        Returns player index after moving as far left as possible.

        A return of -1 means something went wrong.
        """
        for index in range(start_index, -1, -1):
            if not self.can_move_left(index):
                return index
        return self.ERROR_INDEX

    def traverse_right(self, start_index: int) -> int:
        """
        Returns player index after moving as far right as possible.

        A return of -1 means something went wrong.
        """
        for index in range(start_index, len(self.world_space)):
            if not self.can_move_right(index):
                return index
        return self.ERROR_INDEX

    def place_rightmost_to_leftmost(self, start_index: int) -> int:
        """
        Takes the rightmost box and drops it as far left as possible.

        Repeats until stuck, then returns player index.
        """
        start_index = self.traverse_right(start_index)  # start on the right.
        if not self.can_move_left(start_index):
            return start_index
        start_index -= 1  # don't stand on what we're going to pick up.
        for index in range(start_index, -1, -1):
            left_side = self.traverse_left(index)
            self.world_space[index + 1] -= 1  # pick up a box to the right,
            if not self.can_move_left(index):
                self.world_space[index + 1] += 1  # place it back down,
                return index
            self.world_space[left_side] += 1  # or place it to the far left.
            if not self.can_move_left(index):
                return index  # don't move the index if the box got us stuck.
        return 0

    def swap_until_leftmost(self, start_index: int) -> int:
        """
        Takes the left box, moves left, drops the box right.

        Repeats until stuck or at the end of world_space,
        then returns player index.
        """
        for index in range(start_index, -1, -1):
            if index - 1 < 0:
                return index
            self.world_space[index - 1] -= 1  # pick up the left box,
            self.world_space[index] += 1  # and we know we can move left so drop it.
        return 0

    def get_max_height(self, number_of_boxes: int) -> int:
        """
        Returns max attainable height with a given number of boxes.

        A return of -1 means something went wrong.
        """
        if number_of_boxes <= 0:
            self.world_space.clear()
            return self.ERROR_INDEX
        self.initialize_world_space(number_of_boxes)
        pos = self.place_rightmost_to_leftmost(number_of_boxes - 1)
        world_snapshot = self.world_space[0]
        # quit when things stop changing and we're on the left side of the world.
        while world_snapshot != self.world_space[0] or self.traverse_left(pos) != 0:
            world_snapshot = self.world_space[0]
            pos = self.swap_until_leftmost(pos)
            pos = self.place_rightmost_to_leftmost(pos)
        return self.world_space[0]

    def get_min_boxes(self, number_of_boxes: int) -> int:
        """
        Returns min amount of boxes required to reach a given height.

        A return of -1 means something went wrong.
        """
        if number_of_boxes <= 0:
            self.world_space.clear()
            return self.ERROR_INDEX
        iteration = 0
        result = -1
        while result < number_of_boxes:
            iteration += 1
            result = self.get_max_height(iteration)
        return iteration
