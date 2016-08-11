
def load_words(words_file):
    # load a list of words from a file into a list of words

    # TODO

    return []

def find_anagrams(words):
    # process the word list and return a list of lists (grouped by similar
    # words)
    # TODO

    return []

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


