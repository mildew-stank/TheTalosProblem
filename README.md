# Usage
In [The Talos Principle](https://store.steampowered.com/app/2806640/The_Talos_Principle_Reawakened/) you can stack boxes to gain height. To gain the most height with a given number of boxes you will need to pull the ladder up from under yourself, so to speak, by moving lower boxes to higher positions. Run main.py through [Python](https://www.python.org/downloads/) and enter a height to get the minimum number of boxes required to reach it, along with a representation of the final stack layout.

This is essentially a sorting algorithm with a two-step process as defined in `place_right_left()` and `swap_left()` that gets repeated until improvements cease.
