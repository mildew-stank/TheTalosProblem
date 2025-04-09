from stacking import Solution


def main() -> None:
    stack = Solution()
    while True:
        user_input = input("Enter required stack height: ")
        if user_input.lower() in ["exit", "quit"]:
            return
        try:
            n = int(user_input)
        except:
            print("Input must be an integer.")
            continue
        if n <= 0:
            print("Integer must be greater than 0.")
            continue
        print("Minimum boxes required:", stack.get_min_blocks(n))
        print("Final stack:")
        out = [i for i in stack.world if i != 0]
        print(out)


main()
