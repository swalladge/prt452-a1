import unittest

import similar_words 

class WordsTest(unittest.TestCase):

    def setUp(self):
        self.process_words = similar_words.process_words

    def tearDown(self):
        del self.process_words

    def test_example(self):
        """ test based on the example in the question """

        words_list = ['how','who','here','paw','wap','awp']
        processed_words = self.process_words(words_list)

        # should be 3 groups
        self.assertTrue(len(processed_words) == 3)


if __name__ == '__main__':
    unittest.main()
