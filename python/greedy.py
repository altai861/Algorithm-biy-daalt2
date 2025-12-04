
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