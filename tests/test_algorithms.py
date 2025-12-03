import unittest
from algorithms import quicksort, linear_search, binary_search
from models import Product

# Setup sample data for testing
P1 = Product(1, "Alpha", 10.0, 4.0)
P2 = Product(2, "Beta", 20.0, 3.5)
P3 = Product(3, "Gamma", 5.0, 5.0)
P4 = Product(4, "Delta", 15.0, 4.5)
TEST_CATALOG = [P1, P2, P3, P4]
TEST_IDS = ["1", "2", "3", "4"] # IDs as strings for binary search

class TestAlgorithms(unittest.TestCase):

    # --- Quicksort Tests ---
    def test_quicksort_price_ascending(self):
        # Expected order: P3 (5.0), P1 (10.0), P4 (15.0), P2 (20.0)
        sorted_catalog = quicksort(TEST_CATALOG, 'price', reverse=False)
        self.assertEqual([p.id for p in sorted_catalog], ["3", "1", "4", "2"])

    def test_quicksort_rating_descending(self):
        # Expected order: P3 (5.0), P4 (4.5), P1 (4.0), P2 (3.5)
        sorted_catalog = quicksort(TEST_CATALOG, 'rating', reverse=True)
        self.assertEqual([p.id for p in sorted_catalog], ["3", "4", "1", "2"])

    def test_quicksort_empty_list(self):
        self.assertEqual(quicksort([], 'price'), [])
        
    # --- Linear Search Tests ---
    def test_linear_search_full_match(self):
        results = linear_search(TEST_CATALOG, "Alpha")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, "1")

    def test_linear_search_partial_match(self):
        # Matches Alpha, Delta
        results = linear_search(TEST_CATALOG, "lta")
        self.assertEqual(len(results), 2)
        self.assertIn("4", [p.id for p in results])
        
    def test_linear_search_no_match(self):
        results = linear_search(TEST_CATALOG, "Zeta")
        self.assertEqual(len(results), 0)

    # --- Binary Search Tests ---
    def test_binary_search_found(self):
        found_id = binary_search(TEST_IDS, "4")
        self.assertEqual(found_id, "4")

    def test_binary_search_not_found(self):
        found_id = binary_search(TEST_IDS, "5")
        self.assertIsNone(found_id)
        
    def test_binary_search_empty_list(self):
        found_id = binary_search([], "1")
        self.assertIsNone(found_id)


if __name__ == '__main__':
    # You can run tests from the command line by navigating to the Add2Cart directory
    # and running: python -m unittest tests.test_algorithms
    unittest.main(argv=['first-arg-is-ignored'], exit=False)