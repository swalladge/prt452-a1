from collections import OrderedDict

def load_words(words_file):
    # load a list of words from a file into a list of words

    words = []
    with open(words_file) as f:
        for line in f:
            line = line.strip().lower()
            if line not in words and len(line) > 0:
                words.append(line)

    return words

def find_anagrams(words):
    # process the word list and return a list of lists (grouped by
    # anagrams)

    anagram_dict = OrderedDict()
    anagrams = []

    # iterate through the words, using a normalized version of the word as
    # a key in the dictionary to detect anagrams and build lists
    for w in words:
        w = w.lower().strip()
        k = ''.join(sorted(w))
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
    # note: expects a list as outputted by find_anagrams()
    formatted = []

    # make sure the anagrams list is sorted by number of anagrams in the group
    anagrams.sort(key=lambda x:len(x), reverse=True)

    for l in anagrams:
        formatted.append('{}: {}'.format(
            len(l), ', '.join(l)))

    return formatted


if __name__ == '__main__':

    # parse command line args
    import argparse
    arg_parser = argparse.ArgumentParser(prog="similar_words",
                 description="Similar words finder for Q2, PRT452 Assignment 1")
    arg_parser.add_argument("file",
            help="file from which to load the words list")
    args = arg_parser.parse_args()

    # load the list of words from the file
    words = load_words(args.file)

    # detect anagrams in the words list
    anagrams = find_anagrams(words)

    # format the anagrams for pretty printing
    formatted_output_list = format_anagrams(anagrams)

    # print out each line from the list
    for line in formatted_output_list:
        print(line)


