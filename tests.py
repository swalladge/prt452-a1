import unittest

import anagram_detector 


class LoadWordsTest(unittest.TestCase):
    """ tests for loading words from a file into a list """

    def test_example_words(self):
        """ test loading words from example in question into a list """
        expected_words_list = ['how','who','here','paw','wap','awp']
        words = anagram_detector.load_words('tests/words_example.txt')
        self.assertEqual(words, expected_words_list)

    def test_phrases(self):
        """ test loading phrases from a file into a list """
        expected_words_list = ['hello world', 'another phrase']
        words = anagram_detector.load_words('tests/words_phrases.txt')
        self.assertEqual(words, expected_words_list)

    def test_file_not_found(self):
        """ make sure loading from a non-existant file throws an error """
        with self.assertRaises(FileNotFoundError):
            anagram_detector.load_words('tests/file_does_not_exist')

    def test_empty_file(self):
        """ make sure loading from an empty file (no lines with words) doesn't
            return any words
        """
        words = anagram_detector.load_words('tests/words_empty.txt')
        self.assertEqual(words, [])

    def test_uppercase(self):
        """ test with a list containing uppercase letters in words
            (case should be ignored, and everything converted to lowercase)
        """
        formatted = anagram_detector.load_words('tests/words_uppercase.txt')
        expected = ['word', 'ordw']
        self.assertEqual(formatted, expected)

    def test_duplicates(self):
        """ test with a list containing duplicate words (including an uppercase)
            (duplicate words should be ignored - only counted once)
        """
        formatted = anagram_detector.load_words('tests/words_dups.txt')
        expected = ['word', 'ordw']
        self.assertEqual(formatted, expected)


class FindAnagramsTest(unittest.TestCase):
    """ tests to make sure it finds all the anagrams correctly """

    def test_example_words(self):
        """ test finding anagrams based on the example """
        words = ['how','who','here','paw','wap','awp']
        anagrams = anagram_detector.find_anagrams(words)
        expected_anagrams = [['paw','wap','awp'],['how','who'],['here']]
        self.assertEqual(anagrams, expected_anagrams)

    def test_no_words(self):
        """ test with empty words list """
        words = []
        anagrams = anagram_detector.find_anagrams(words)
        expected = []
        self.assertEqual(anagrams, expected)

    def test_one_word(self):
        """ test with a single word """
        words = ['hello']
        anagrams = anagram_detector.find_anagrams(words)
        expected = [['hello']]
        self.assertEqual(anagrams, expected)

    def test_single_anagram_group(self):
        """ test with a list where all are anagrams of the same word """
        words = ['abcd','bacd','acdb','dabc']
        anagrams = anagram_detector.find_anagrams(words)
        expected = [['abcd','bacd','acdb','dabc']]
        self.assertEqual(anagrams, expected)

    def test_duplicate_words(self):
        """ test with a list containing duplicate words
            (duplicates should be ignored)
        """
        words = ['hello','hello','world']
        anagrams = anagram_detector.find_anagrams(words)
        expected = [['hello'],['world']]
        self.assertEqual(anagrams, expected)

    def test_phrases(self):
        """ test with a list containing phrases
            (inner spaces should count as letters)
        """
        words = ['hi there','here hit','eerthih']
        anagrams = anagram_detector.find_anagrams(words)
        expected = [['hi there','here hit'],['eerthih']]
        self.assertEqual(anagrams, expected)

    def test_uppercase(self):
        """ test with a list containing uppercase letters in words
            (case should be ignored, and everything converted to lowercase)
        """
        words = ['Word', 'word', 'ordw']
        formatted = anagram_detector.find_anagrams(words)
        expected = [['word', 'ordw']]
        self.assertEqual(formatted, expected)


class FormatAnagramsTest(unittest.TestCase):
    """ tests to make sure the anagrams list gets formatted properly for printing"""

    def test_example_words(self):
        """ test finding anagrams based on the example """
        anagrams = [['paw','wap','awp'],['how','who'],['here']]
        formatted = anagram_detector.format_anagrams(anagrams)
        expected = [ '3: paw, wap, awp', '2: how, who', '1: here']
        self.assertEqual(formatted, expected)

    def test_no_words(self):
        """ test with empty words list """
        anagrams = []
        formatted = anagram_detector.format_anagrams(anagrams)
        expected = []
        self.assertEqual(formatted, expected)

    def test_one_word(self):
        """ test with a single word """
        anagrams = [['hello']]
        formatted = anagram_detector.format_anagrams(anagrams)
        expected = ['1: hello']
        self.assertEqual(formatted, expected)

    def test_single_anagram_group(self):
        """ test with a list where all are anagrams of the same word """
        anagrams = [['abcd','bacd','acdb','dabc']]
        formatted = anagram_detector.format_anagrams(anagrams)
        expected = ['4: abcd, bacd, acdb, dabc']
        self.assertEqual(formatted, expected)

    def test_duplicate_words(self):
        """ test with a list containing duplicate words
            (duplicates should be ignored)
        """
        anagrams = [['hello'],['world']]
        formatted = anagram_detector.format_anagrams(anagrams)
        expected = ['1: hello','1: world']
        self.assertEqual(formatted, expected)

    def test_phrases(self):
        """ test with a list containing phrases
            (inner spaces should count as letters)
        """
        anagrams = [['hi there','here hit'],['eerthih']]
        formatted = anagram_detector.format_anagrams(anagrams)
        expected = ['2: hi there, here hit','1: eerthih']
        self.assertEqual(formatted, expected)


class AllTogetherTest(unittest.TestCase):
    """ tests to bring everything together - to show the three functions working together """

    def test_example_words(self):
        """ test anagrams based on the example """
        words = anagram_detector.load_words('tests/words_example.txt')
        anagrams = anagram_detector.find_anagrams(words)
        formatted = anagram_detector.format_anagrams(anagrams)
        expected = ['3: paw, wap, awp', '2: how, who', '1: here']
        self.assertEqual(formatted, expected)



if __name__ == '__main__':
    unittest.main()
