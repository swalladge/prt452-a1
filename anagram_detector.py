from collections import OrderedDict

def load_words(words_file):
    # load a list of words from a file into a list of words

    words = []
    with open(words_file) as f:
        for line in f:
            words.append(line.strip())

    return words

def find_anagrams(words):
    # process the word list and return a list of lists (grouped by
    # anagrams)

    anagram_dict = OrderedDict()
    anagrams = []

    # iterate through the words, using a normalized version of the word as
    # a key in the dictionary to detect anagrams and build lists
    for w in words:
        k = ''.join(sorted(w.lower()))
        if k not in anagram_dict:
            anagram_dict[k] = [w]
        else:
            if w not in anagram_dict[k]:
                anagram_dict[k].append(w) 

    # transform the anagram dictionary to a list of lists of anagrams,
    # sorted by number of anagrams
    for k in sorted(anagram_dict, key=lambda x:-len(anagram_dict[x])):
        anagrams.append(anagram_dict[k])

    return anagrams

def format_anagrams(anagrams):
    # takes the grouped word list of lists and returns a list of strings,
    # line by line.

    # TODO

    return []


if __name__ == '__main__':
    import argparse
    arg_parser = argparse.ArgumentParser(prog="similar_words",
                 description="Similar words finder for Q2, PRT452 Assignment 1")

    arg_parser.add_argument("file",
            help="file from which to load the words list")

    args = arg_parser.parse_args()

    words = load_words(args.file)

    anagrams = find_anagrams(words)
    formatted_output_list = format_anagrams(anagrams)

    for line in formatted_output_list:
        print(line)


