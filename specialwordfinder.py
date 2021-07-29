from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """return a random word from a file if it's not an empty line or line that starts with # 
    Attributes:
    __________ 
        filepath: str
            a path to a file on disk that contains words"""
 
    def randomSpecial(self):
        """calls the random word from a list, check if not an empty string or comment and return it"""
        flag = True
        while  flag:
            word = super().random()
            if (word != "" and word[0] != "#"): 
                flag = False
        return word
    

    

        
      
       
