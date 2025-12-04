from greedy import justify_greedy
from dp import justify_dp


def main():
    print("=== Text Justification (Greedy & DP) ===")
    text = input("Enter text: ").strip()
    width = int(input("Enter max line width: "))
    algo = input("Choose algorithm (greedy/dp): ").strip().lower()

    words = text.split()

    if algo == "greedy":
        lines = justify_greedy(words, width)
    elif algo == "dp":
        lines = justify_dp(words, width)
    else:
        print("Invalid choice")
        return

    print("\n=== Justified Text ===")
    for line in lines:
        print(line)

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
