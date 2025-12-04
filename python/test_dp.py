from dp import justify_dp
import unittest

class TestJustifyDP(unittest.TestCase):

    def test_single_line_exact_fit(self):
        words = ["hello", "world"]
        max_width = 11  
        result = justify_dp(words, max_width)
        self.assertEqual(result, ["hello world"])

    def test_single_line_padded(self):
        words = ["hello"]
        max_width = 10
        result = justify_dp(words, max_width)
        self.assertEqual(result, ["hello     "])

    def test_multiple_lines(self):
        words = ["This", "is", "a", "test"]
        max_width = 10
        result = justify_dp(words, max_width)

        self.assertEqual(result[0], "This  is a")
        self.assertEqual(result[1], "test      ")

    def test_last_line_left_justified(self):
        words = ["longword", "small", "x"]
        max_width = 15
        result = justify_dp(words, max_width)

        self.assertEqual(result[0], "longword  small")

        self.assertEqual(result[1], "x" + " " * (15 - 1))

    def test_single_word_lines(self):
        words = ["A", "B", "C"]
        max_width = 5
        result = justify_dp(words, max_width)

        self.assertEqual(result[0], "A B C")

    def test_dp_vs_greedy_difference(self):
       
        words = ["aaa", "b", "c", "ddd"]
        max_width = 6


        result = justify_dp(words, max_width)

        self.assertEqual(result[0], "aaa  b")  
        self.assertEqual(result[1], "c ddd ")   

    def test_long_last_line(self):
        words = ["a", "b", "c", "d", "e"]
        max_width = 10
        result = justify_dp(words, max_width)

        self.assertEqual(result[0], "a b c d e ")


if __name__ == "__main__":
    unittest.main()