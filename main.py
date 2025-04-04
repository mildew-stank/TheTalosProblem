from stacking import TheTalosProblem as ttp

def main() -> None:
    world = ttp()
    while True:
        user_input = input("Enter required stack height: ")
        if user_input.lower() in ['exit', 'quit']:
            return
        try:
            n = int(user_input)
        except:
            print("Input must be an integer.")
            continue
        if n <= 0:
            print("Integer must be greater than 0.")
            continue
        print("Minimum boxes required:", world.get_min_boxes(n))
        print("Final stack:")
        out = [i for i in world.world_space if i != 0]
        print(out)
main()
