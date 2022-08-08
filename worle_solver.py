class solver:
    def __init__(self, starter = 'stray'):
        self.__guess = starter

    def getGuess(self):
        return self.__guess
    
    def setGuess(self, word):
        self.__guess = word


