from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """return a random word from a file without any special symbols"""
    def __init__(self,filepath):
        super().__init__(filepath)
        
    def randomSpecial(self):
    """calls the random word from a list, check if it's a word and not an empty string or comment and return it"""
        flag = True
        while  flag:
            word = super().random()
            if (word != "" and word[0] != "#"): 
                flag = False
        return word
    
    def describe(self):
        return f"I am read a file {self.filepath} and return a random word from it without any special symbols"
    

        
      
       
