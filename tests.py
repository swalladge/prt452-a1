import unittest

import anagram_detector 


class LoadWordsTest(unittest.TestCase):
    """ tests for loading words from a file into a list """

    def test_example_words(self):
        """ test loading words from example in question into a list """
        expected_words_list = ['how','who','here','paw','wap','awp']
        words = anagram_detector.load_words('tests/words_example.txt')
        self.assertEqual(words, expected_words_list)

    def test_file_not_found(self):
        """ make sure loading from a non-existant file throws an error """
        with self.assertRaises(FileNotFoundError):
            anagram_detector.load_words('tests/file_does_not_exist')


if __name__ == '__main__':
    unittest.main()
