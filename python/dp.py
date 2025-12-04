
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
