import unittest
from unittest import result #load built-in testing tools
from Main import find_language #borrows your search function from Main.py

class TestLanguageSearch(unittest.TestCase): #creates a group of tests using Python's testing framework
    def test_find_by_code(self): #define 1 test function
        sample_records = [
            {
                "language_code": "TEST1",
                "language_name": "Example name",
                "language_synonym": "Example alternative"
            }
        ]

        result = find_language(sample_records, "TEST1")

        self.assertEqual(result, sample_records[0]) #checks that the returned result = to the expected record
    def test_find_by_alternative(self):
        sample_records = [
            {
                "language_code": "TEST1",
                "language_name": "Example name",
                "language_synonym": "Example alternative|Second alternative"
            }
        ]
        result = find_language(sample_records, "Second alternative")
        self.assertEqual(result, sample_records[0]) #checks that the returned result = to
 
if __name__ == "__main__":
    unittest.main() #run the test when you start this file directly
