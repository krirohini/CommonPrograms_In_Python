'''
Created on Feb 12, 2019

@author: r.kumari
'''

class LongestSubString:
    
    def longestSubString_ForGivenString(self, givenString): 
        
        if len(givenString) == 0:
            print (">>>> Given String have size - 0")
        elif len(givenString) == 1:
            print (">>>> Given String is having only one letter ")
        else:
            
            index = []
            index.append(0)
            
            difference = 1
            startIndex = 0
            endIndex = 0
            
            i = 0
            while i < len(givenString):
                if givenString[i] == " ":
                    print ("Found " " space at index >>> ", i)
                    index.append(i)
                i = i + 1
            
            j = 0
            
            while j < len(index):
                if j + 1 <  len(index):
                    nextIndex = j + 1
                    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print (">>> For  index[", j , "] >>>>  of ", index)
                    currentDifference = index[nextIndex] - index[j]
                    print (">>>> currentDifference  - ", currentDifference)
                    print (">>>> difference  - ", difference)
                    
                    if currentDifference > difference :
                        difference = currentDifference 
                        startIndex = j
                        endIndex = j + 1
                        print (">>> startIndex >>>> ", j)
                        print (">>> endIndex >>>> ", j+1)
                        
                    else:
                        difference = difference
                    j = j + 1
                else:
                    break
                
            print ("Given String is - ", givenString)
            print ("Longest SubString is - ", givenString[index[startIndex]:index[endIndex]])
                    
obj = LongestSubString()
obj.longestSubString_ForGivenString("RohiniKumari Sanjose ca usa RohiniKumariRohini a is are")
              
                
                    