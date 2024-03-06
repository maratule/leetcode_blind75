import unittest

class Solution:
    def

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        expected_output = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        self.assertEqual(self.solution.reorderLogFiles(logs), expected_output)

    def test_custom_case1(self):
        logs = ["let4 art zero","dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        expected_output = ["let1 art can", "let3 art zero", "let4 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        self.assertEqual(self.solution.reorderLogFiles(logs), expected_output)

    def test_all_digit_logs(self):
        logs = ["dig1 1", "dig2 2", "dig3 3"]
        expected_output = ["dig1 1", "dig2 2", "dig3 3"]
        self.assertEqual(self.solution.reorderLogFiles(logs), expected_output)

    def test_all_letter_logs(self):
        logs = ["let1 a", "let2 b", "let3 c"]
        expected_output = ["let1 a", "let2 b", "let3 c"]
        self.assertEqual(self.solution.reorderLogFiles(logs), expected_output)

    def test_empty_logs(self):
        logs = []
        expected_output = []
        self.assertEqual(self.solution.reorderLogFiles(logs), expected_output)

if __name__ == '__main__':
    unittest.main()
