class Ruleset:
    """
    This class represents a simulation of a character navigating a 2D world made up of blocks.
    The character can move, grab, and drop blocks within the world, subject to certain constraints.
    Attributes:
        world (list[int]): A list representing the heights of blocks in the 2D world.
        position (int): The current position of the character in the world.
        equipped (bool): Indicates whether the character is holding a block.
    """

    def __init__(self):
        """Initializes the simulation with a default world of one block and the character at position 0."""
        self.world = [1]
        self.position = 0
        self.equipped = False

    def make_world(self, n: int) -> None:
        """Creates a new world with `n` blocks, all of height 1, and resets the character's position to 0."""
        self.world = [1] * n
        self.position = 0

    def step(self, direction: int, allow_fall: bool = False) -> bool:
        """
        Moves the character one step in the specified direction if the move is valid.
        Parameters:
            direction (int): The direction to move (-1 for left, 1 for right).
            allow_fall (bool): If True, allows the character to fall down by more than one block.
        Returns:
            bool: True if the step was successful, False otherwise.
        """
        destination = self.position + direction
        if destination < 0 or destination >= len(self.world):
            return False
        difference = self.world[destination] - self.world[self.position]
        too_high = difference > 1
        too_low = difference < -1
        if too_high or (not allow_fall and too_low) or self.world[destination] == 0:
            return False
        self.position += direction
        return True

    def walk(self, direction: int, max_steps: int = -1, allow_fall: bool = False) -> bool:
        """
        Moves the character in the specified direction for up to `max_steps` steps or until movement is blocked.
        Parameters:
            direction (int): The direction to move (-1 for left, 1 for right).
            max_steps (int): The maximum number of steps to take (-1 for unlimited).
            allow_fall (bool): If True, allows the character to fall down by more than one block.
        Returns:
            bool: True if the character moved at least one step, False otherwise.
        """
        start = self.position
        while self.step(direction, allow_fall) and (max_steps != 0):
            max_steps -= 1
        if start == self.position:
            return False
        return True

    def grab(self, direction: int) -> bool:
        """
        Picks up a block from the specified direction if possible.
        Parameters:
            direction (int): The direction to grab the block from (-1 for left, 1 for right).
        Returns:
            bool: True if the block was successfully grabbed, False otherwise.
        """
        target = self.position + direction
        if target < 0 or target >= len(self.world):
            return False
        difference = self.world[target] - self.world[self.position]
        if self.equipped or difference < -1 or self.world[target] == 0:
            return False
        self.world[target] -= 1
        self.equipped = True
        return True

    def drop(self, direction: int) -> bool:
        """
        Drops a block in the specified direction if possible.
        Parameters:
            direction (int): The direction to drop the block (-1 for left, 1 for right).
        Returns:
            bool: True if the block was successfully dropped, False otherwise.
        """
        target = self.position + direction
        if target < 0 or target >= len(self.world):
            return False
        difference = self.world[target] - self.world[self.position]
        if not self.equipped or difference > 1:
            return False
        self.world[target] += 1
        self.equipped = False
        return True


class Solution(Ruleset):
    """Extends `Ruleset` with stacking methods."""

    def stack_right(self):
        """Takes blocks from the left side of world and stacks them up on the right."""
        while True:
            self.walk(-1)
            self.grab(-1)
            self.step(1)
            self.grab(-1)
            if not self.walk(1):
                self.drop(-1)
                return
            self.step(-1)
            self.drop(1)

    def swap_left(self):
        """Swaps places with blocks by shifting them to the left while traversing to the right."""
        while True:
            self.walk(1)
            if not self.grab(1):
                return
            # spread out tall stacks behind us instead of swapping places
            direction = 1
            target = self.position + direction
            difference = self.world[target] - self.world[self.position]
            direction = max(-1, min(3 - difference, 1))
            self.walk(direction, 3 - difference)
            self.drop(-1)

    def find_peak_index(self, history: list[int]) -> int:
        """Returns an index containing the highest peak"""
        peak = 0
        history_index = 0
        for index, result in enumerate(history):
            if result[-1] > peak:
                peak = result[-1]
                history_index = index
        return history_index

    def get_max_height(self, blocks: int) -> int:
        """Returns the maximum reachable height for a given amount of `blocks`."""
        if blocks < 1:
            return 0
        history = []
        self.make_world(blocks)
        while not self.world in history:
            history.append(self.world.copy())
            while True:
                self.stack_right()
                snapshot = self.world[-1]
                self.swap_left()
                if snapshot == self.world[-1]:
                    break
            self.walk(-1, -1, True)
        index = self.find_peak_index(history)
        self.world = history[index]
        return history[index][-1]

    def get_min_blocks(self, height: int) -> int:
        """Returns the minimum amount of blocks required to reach a given `height`"""
        if height < 1:
            return 0
        blocks = height
        while self.get_max_height(blocks) < height:
            blocks += 1
        return blocks
