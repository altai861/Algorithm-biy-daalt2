import math

def justify_greedy(words, max_width):
    res = []
    i = 0
    n = len(words)

    while i < n:
        line_len = len(words[i])
        j = i + 1
        while j < n and line_len + 1 + len(words[j]) <= max_width:
            line_len += 1 + len(words[j])
            j += 1

        num_words = j - i

        if j == n or num_words == 1:
            line = " ".join(words[i:j])
            line += " " * (max_width - len(line))
        else:
            total_spaces = max_width - sum(len(w) for w in words[i:j])
            gaps = num_words - 1
            space, extra = divmod(total_spaces, gaps)

            line = ""
            for k in range(i, j - 1):
                line += words[k] + " " * space
                if extra > 0:
                    line += " "
                    extra -= 1
            line += words[j - 1]

        res.append(line)
        i = j

    return res


def badness(slack):
    return slack ** 3


def justify_dp(words, max_width):
    n = len(words)
    lens = [len(w) for w in words]

    INF = float('inf')
    cost = [[INF] * n for _ in range(n)]

    for i in range(n):
        length = lens[i]
        for j in range(i, n):
            if j > i:
                length += 1 + lens[j]
            if length <= max_width:
                slack = max_width - length
                if j == n - 1:
                    cost[i][j] = 0 
                else:
                    cost[i][j] = badness(slack)
            else:
                break

    dp = [INF] * (n + 1)
    next_break = [-1] * n
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if cost[i][j] == INF:
                break
            if cost[i][j] + dp[j + 1] < dp[i]:
                dp[i] = cost[i][j] + dp[j + 1]
                next_break[i] = j + 1

    res = []
    i = 0
    while i < n:
        j = next_break[i]
        line_words = words[i:j]
        if j == n: 
            line = " ".join(line_words)
            line += " " * (max_width - len(line))
        else:
            total_spaces = max_width - sum(len(w) for w in line_words)
            gaps = len(line_words) - 1
            if gaps > 0:
                space, extra = divmod(total_spaces, gaps)
                line = ""
                for k in range(len(line_words) - 1):
                    line += line_words[k] + " " * space
                    if extra > 0:
                        line += " "
                        extra -= 1
                line += line_words[-1]
            else:
                line = line_words[0] + " " * (max_width - len(line_words[0]))

        res.append(line)
        i = j

    return res


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
