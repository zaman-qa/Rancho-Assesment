from word_count import word_count
from highest_count import highest_count
import unittest

file_path = 'sample.txt'

class TestWordCount(unittest.TestCase):
    
    def test_null_input(self):
        self.assertEqual(word_count(None), None)
        
    def test_empty_input(self):
        self.assertEqual(word_count(''), None)
        
    def test_invalid_input(self):
        with self.assertRaises(FileNotFoundError):
            word_count('file_does_not_exist.txt')
            
    def test_valid_input(self):
        self.assertEqual(type(word_count(file_path)), dict)
        
    def test_word_with_highest_count(self):
        expected_output = {'non': 12}
        words = word_count(file_path)
        self.assertEqual(highest_count(words), expected_output)
        
if __name__ == '__main__':
    unittest.main()