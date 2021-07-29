"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """open a file and read it line-by-line to create a list of words, then print a random word from the list
    Attributes:
    ___________
        filepath: str
            a path to a file on disk that contains words
    """
    def __init__(self,filepath):
        self.filepath = filepath
       
        self.word_list = []
        with open(self.filepath, "r") as file:
            for line in file:
                self.word_list.append(line.strip())
            print(f"{len(self.word_list)} words read")
        
    def random(self):
       """returns a random word from the list of words"""
       return self.word_list[randint(0,len(self.word_list)-1)]
