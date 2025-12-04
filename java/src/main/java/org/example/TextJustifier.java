package org.example;

import java.util.*;

public class TextJustifier {

    private static int badness(int slack) {
        return slack * slack * slack;
    }

    public static List<String> justifyGreedy(List<String> words, int maxWidth) {
        List<String> res = new ArrayList<>();
        int n = words.size();
        int i = 0;

        while (i < n) {
            int lineLen = words.get(i).length();
            int j = i + 1;

            while (j < n && lineLen + 1 + words.get(j).length() <= maxWidth) {
                lineLen += 1 + words.get(j).length();
                j++;
            }

            int numWords = j - i;
            StringBuilder line = new StringBuilder();

            if (j == n || numWords == 1) {
                for (int k = i; k < j; k++) {
                    if (k > i) line.append(" ");
                    line.append(words.get(k));
                }
                while (line.length() < maxWidth) line.append(" ");

            } else {
                int totalSpaces = maxWidth - words.subList(i, j).stream()
                        .mapToInt(String::length).sum();
                int gaps = numWords - 1;
                int space = totalSpaces / gaps;
                int extra = totalSpaces % gaps;

                for (int k = i; k < j - 1; k++) {
                    line.append(words.get(k));
                    line.append(" ".repeat(space));
                    if (extra > 0) {
                        line.append(" ");
                        extra--;
                    }
                }
                line.append(words.get(j - 1));
            }

            res.add(line.toString());
            i = j;
        }

        return res;
    }

    public static List<String> justifyDP(List<String> words, int maxWidth) {
        int n = words.size();
        int[] lens = words.stream().mapToInt(String::length).toArray();

        int INF = Integer.MAX_VALUE / 4;
        int[][] cost = new int[n][n];

        for (int[] row : cost) Arrays.fill(row, INF);

        for (int i = 0; i < n; i++) {
            int length = lens[i];
            for (int j = i; j < n; j++) {
                if (j > i) length += 1 + lens[j];
                if (length <= maxWidth) {
                    int slack = maxWidth - length;
                    if (j == n - 1) {
                        cost[i][j] = 0;
                    } else {
                        cost[i][j] = badness(slack);
                    }
                } else {
                    break;
                }
            }
        }

        int[] dp = new int[n + 1];
        int[] nextBreak = new int[n];
        Arrays.fill(dp, INF);
        dp[n] = 0;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (cost[i][j] == INF) break;
                int val = cost[i][j] + dp[j + 1];
                if (val < dp[i]) {
                    dp[i] = val;
                    nextBreak[i] = j + 1;
                }
            }
        }

        List<String> res = new ArrayList<>();
        int i = 0;

        while (i < n) {
            int j = nextBreak[i];
            List<String> lineWords = words.subList(i, j);

            StringBuilder line = new StringBuilder();

            if (j == n) {
                // Last line: left justify
                for (int k = 0; k < lineWords.size(); k++) {
                    if (k > 0) line.append(" ");
                    line.append(lineWords.get(k));
                }
                while (line.length() < maxWidth) line.append(" ");

            } else {
                int totalSpaces = maxWidth - lineWords.stream()
                        .mapToInt(String::length)
                        .sum();

                int gaps = lineWords.size() - 1;

                if (gaps > 0) {
                    int space = totalSpaces / gaps;
                    int extra = totalSpaces % gaps;

                    for (int k = 0; k < lineWords.size() - 1; k++) {
                        line.append(lineWords.get(k));
                        line.append(" ".repeat(space));
                        if (extra > 0) {
                            line.append(" ");
                            extra--;
                        }
                    }
                    line.append(lineWords.get(lineWords.size() - 1));

                } else {
                    // Only one word
                    line.append(lineWords.get(0));
                    while (line.length() < maxWidth) line.append(" ");
                }
            }

            res.add(line.toString());
            i = j;
        }

        return res;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Text Justification (Greedy & DP) ===");

        System.out.print("Enter text: ");
        String text = sc.nextLine().trim();

        System.out.print("Enter max line width: ");
        int width = Integer.parseInt(sc.nextLine());

        System.out.print("Choose algorithm (greedy/dp): ");
        String algo = sc.nextLine().trim().toLowerCase();

        List<String> words = Arrays.asList(text.split("\\s+"));
        List<String> result;

        if (algo.equals("greedy")) {
            result = justifyGreedy(words, width);
        } else if (algo.equals("dp")) {
            result = justifyDP(words, width);
        } else {
            System.out.println("Invalid choice.");
            sc.close();
            return;
        }

        System.out.println("\n=== Justified Text ===");
        for (String line : result) {
            System.out.println(line);
        }

        System.out.println("\n=== DONE ===");
        sc.close();
    }
}
