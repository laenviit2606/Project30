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
    def test_find_by_name(self):
        sample_records = [
            {
                "language_code": "TEST1",
                "language_name": "Example name",
                "language_synonym": "First alternative|Second alternative"
            }
        ]
        result = find_language(sample_records, "Example name")
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
        self.assertEqual(result, sample_records[0]) #checks that the returned result = to the expected record
    def test_case_and_spaces(self):
        sample_records = [
            {
                "language_code": "TEST1",
                "language_name": "Example name",
                "language_synonym": ""
            }
        ]
        result = find_language(sample_records, " eXaMpLe NaMe ")
        self.assertEqual(result, sample_records[0]) 
    def test_unknown_input(self):
        sample_records = [
            {
                "language_code": "TEST1",
                "language_name": "Example name",
                "language_synonym": ""
            }
        ]
        result = find_language(sample_records, "UNKNOWN999")
        self.assertIsNone(result)
    def test_blank_input(self):
        sample_records = [
            {
                'language_code': "TEST1",
                'language_name': "Example name",
                'language_synonym': ""
            }
        ]
        result = find_language(sample_records, " ")
        self.assertIsNone(result)
    def test_empty_dataset(self):
        result = find_language([], "TEST1")
        self.assertIsNone(result)
    def test_find_second_record(self):
        sample_records = [
            {
                "language_code": "TEST1",
                "language_name": "Example name",
                "language_synonym": ""
            },
            {
                "language_code": "TEST2",
                "language_name": "Second example",
                "language_synonym": ""
            }
        ]
        result = find_language(sample_records, "TEST2")
        self.assertEqual(result, sample_records[1])
if __name__ == "__main__":
    unittest.main() #run the test when you start this file directly
