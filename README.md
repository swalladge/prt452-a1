
# PRT452 Assignment 1

Copyright © 2016 Samuel Walladge

## About

This git repo will contain everything for Assignment 1, including:

- [x] the program for Q2
- [x] tests for Q2's program
- [] document presenting the TDD process used for Q2
- [] document answering Q3
- [x] a copy of the questions themselves

## Explanation of files

- README.md - this document
- .gitignore - file listing files/directories that git should ignore
- questions.md - the questions copied from the original assignment document for reference
- tests.py - unittests to run, used for TDD
- anagram_detector.py - the program for question 2
- .travis.yml - [Travis CI](https://travis-ci.org) config file
- tests/ directory - contains various files used for testing


## Notes

- all documents are written as plain text files using markdown markup.


## Question 2 information

- the program is written in python, using the included unit testing framework
- Travis CI is used for running the tests on every push. 

Tests Status:  [![Build Status](https://travis-ci.org/swalladge/prt452-a1.svg?branch=master)](https://travis-ci.org/swalladge/prt452-a1)

The program is run as follows (with `file.txt` the name of a file with a list of words to process):

```
$ python anagram_detector.py <file.txt>
```

To run the tests:

```
$ python tests.py
```

## Question 3 information

TODO

