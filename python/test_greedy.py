import unittest
from greedy import justify_greedy   

class TestJustifyGreedy(unittest.TestCase):

    def test_single_short_line(self):
        words = ["hello", "world"]
        result = justify_greedy(words, 20)
        self.assertEqual(result, ["hello world         "])

    def test_exact_fit_line(self):
        words = ["abc", "de", "fgh"]
        result = justify_greedy(words, 11)
        self.assertEqual(result, ["abc de fgh "])

    def test_multiple_lines(self):
        words = ["This", "is", "a", "test"]
        max_width = 10
        result = justify_greedy(words, max_width)

        self.assertEqual(result[0], "This  is a")

        self.assertEqual(result[1], "test      ")

    def test_last_line_left_justified(self):
        words = ["longword", "small", "x"]
        max_width = 15
        result = justify_greedy(words, max_width)

        self.assertEqual(result[0], "longword  small")

        self.assertEqual(result[1], "x" + " " * (15 - 1))

    def test_single_word_line(self):
        words = ["Hello"]
        result = justify_greedy(words, 10)
        self.assertEqual(result, ["Hello     "])

    def test_space_distribution(self):
        words = ["a", "b", "c", "d"]
        max_width = 7
        result = justify_greedy(words, max_width)

        self.assertEqual(result, ["a b c d"])


if __name__ == "__main__":
    unittest.main()
