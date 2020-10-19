import unittest
import O1

class TestNumbersWithinRange(unittest.TestCase):

    test_numbers = [0, 5, 10, 55, 69, 110]

    def test_between_0_and_10_has_3(self):
        correct_count: int = 3 # assuming inclusive range
        res: int = O1.count_numbers_between_range((0, 10), self.test_numbers)
        self.assertEqual(correct_count, res)

    def test_between_50_and_100_has_2(self):
        correct_count: int = 2 # assuming inclusive range
        res: int = O1.count_numbers_between_range((50, 100), self.test_numbers)
        self.assertEqual(correct_count, res)

    def test_between_67_and_75_has_1(self):
        correct_count: int = 1 # assuming inclusive range
        res: int = O1.count_numbers_between_range((67, 75), self.test_numbers)
        self.assertEqual(correct_count, res)

    def test_between_0_and_10_with_negative_inputs_has_0(self):
        correct_count: int = 0 # assuming inclusive range
        res: int = O1.count_numbers_between_range((0, 10), [-15, -8, -2])
        self.assertEqual(correct_count, res)

    def test_returns_zero_for_empty_list(self):
        self.assertEqual(0, O1.count_numbers_between_range((0, 11), []))

    def test_works_with_passed_in_predicate_func(self):
        correct_count: int = 1 # assuming exclusive range
        res: int = O1.count_numbers_between_range((0, 10), self.test_numbers, \
            range_func_partial=lambda l, u, v: int(l < v and v < u))
        self.assertEqual(correct_count, res)

if __name__ == "__main__":
    unittest.main()