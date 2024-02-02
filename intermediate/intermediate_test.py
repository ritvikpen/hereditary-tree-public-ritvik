import unittest
from unittest.mock import patch

from io import StringIO
import csv
import itertools
import sys
import argparse
from heredity_intermediate import *

class TestHeredity(unittest.TestCase):

    def test_arg_parser(self):
        # Test arg_parser function
        with patch('sys.argv', ['heredity.py', 'test.csv']):
            args = arg_parser()
            self.assertEqual(args.i, 'test.csv')
    
    def test_file_type_checker(self):
        # Test file_type_checker function
        extension_checker = file_type_checker('.csv')
        valid_file_name = 'test.csv'
        invalid_file_name = 'test.txt'
        self.assertEqual(extension_checker(valid_file_name), valid_file_name)
        self.assertEqual(extension_checker(invalid_file_name), invalid_file_name)
    
    def test_load_data(self):
        # Test load_data function
        csv_data = "name,mother,father,trait\nJohn,Mary,Robert,1\nAlice,,John,0\nBob,Jane,,\n"
        with patch('builtins.open', return_value=StringIO(csv_data)):
            loaded_data = load_data('test.csv')

        expected_data = {
            'John': {'name': 'John', 'mother': 'Mary', 'father': 'Robert', 'trait': 1},
            'Alice': {'name': 'Alice', 'mother': None, 'father': 'John', 'trait': 0},
            'Bob': {'name': 'Bob', 'mother': 'Jane', 'father': None, 'trait': None}
        }
        self.assertEqual(loaded_data, expected_data)

    def test_calculate_trait(self):
        # Test calculate_trait function
        probabilities = {'Arthur': {'gene': {2: 1, 1: 0, 0: 0}, 'trait': 1.0}, 'Molly': {'gene': {2: 0, 1: 0, 0: 1}, 'trait': 0.0}, 'Jane': {'gene': {2: 1, 1: 0, 0: 0}, 'trait': 1.0}, 'Tiffany': {'gene': {2: 0, 1: 0, 0: 1}, 'trait': 0.0}, 'Charlie': {'gene': {2: 0, 1: 0, 0: 0}, 'trait': None}, 'Fred': {'gene': {2: 0, 1: 0, 0: 0}, 'trait': None}, 'Sarah': {'gene': {2: 0, 1: 0, 0: 0}, 'trait': None}, 'Ritvik': {'gene': {2: 0, 1: 0, 0: 0}, 'trait': None}, 'Wonka': {'gene': {2: 0, 1: 0, 0: 0}, 'trait': None}}
        people = {'Arthur': {'name': 'Arthur', 'mother': None, 'father': None, 'trait': True}, 'Molly': {'name': 'Molly', 'mother': None, 'father': None, 'trait': False}, 'Jane': {'name': 'Jane', 'mother': None, 'father': None, 'trait': True}, 'Tiffany': {'name': 'Tiffany', 'mother': None, 'father': None, 'trait': False}, 'Charlie': {'name': 'Charlie', 'mother': 'Molly', 'father': 'Arthur', 'trait': None}, 'Fred': {'name': 'Fred', 'mother': 'Molly', 'father': 'Arthur', 'trait': None}, 'Sarah': {'name': 'Sarah', 'mother': 'Jane', 'father': 'Charlie', 'trait': None}, 'Ritvik': {'name': 'Ritvik', 'mother': 'Tiffany', 'father': 'Fred', 'trait': None}, 'Wonka': {'name': 'Wonka', 'mother': 'Sarah', 'father': 'Ritvik', 'trait': None}}

        calculate_trait(probabilities, people)
        
        # Adjust the expected probabilities based on your specific implementation
        expected_probabilities = {'Arthur': {'gene': {2: 1, 1: 0, 0: 0}, 'trait': 1.0}, 'Molly': {'gene': {2: 0, 1: 0, 0: 1}, 'trait': 0.0}, 'Jane': {'gene': {2: 1, 1: 0, 0: 0}, 'trait': 1.0}, 'Tiffany': {'gene': {2: 0, 1: 0, 0: 1}, 'trait': 0.0}, 'Charlie': {'gene': {2: 0.0, 1: 1.0, 0: 0.0}, 'trait': 0.0}, 'Fred': {'gene': {2: 0.0, 1: 1.0, 0: 0.0}, 'trait': 0.0}, 'Sarah': {'gene': {2: 0.5, 1: 0.5, 0: 0.0}, 'trait': 0.5}, 'Ritvik': {'gene': {2: 0.0, 1: 0.5, 0: 0.5}, 'trait': 0.0}, 'Wonka': {'gene': {2: 0.1875, 1: 0.625, 0: 0.1875}, 'trait': 0.1875}}
        
        self.assertEqual(probabilities, expected_probabilities)
    

if __name__ == '__main__':
    unittest.main()
