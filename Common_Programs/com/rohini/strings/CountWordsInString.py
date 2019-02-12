'''
Created on Feb 12, 2019

@author: r.kumari
'''

class CountWordsInString:
    
    def countWords(self, givenString):
        if len(givenString) == 0:
            print (">>>> String length is - 0")
        else:
            countWords = 1
            i = 0
            while i < len(givenString):
                
                if givenString[i] == ' ':
                    print (" >>>> Found " " space at index - ", i)
                    countWords = countWords + 1
                else:
                    print (" >>>> " " space NOT Found")
                
                i = i + 1
            print("Total Words are - ", countWords , " - for given string - ", givenString)

obj = CountWordsInString()
obj.countWords("Rohini")
#obj.countWords("Rohini Kumari Sanjose California")
            