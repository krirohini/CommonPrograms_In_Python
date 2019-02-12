'''
Created on Feb 12, 2019

@author: r.kumari
'''
class FirstNonRepeatingChar:
    
    def firstCharNonRepeating_ForString(self, givenString):
        
        
        
        if len(givenString) == 0:
            print(">>>> String length is - 0")
        else:
            charDict = {}
            i = 0
            #count = 1
            while i < len(givenString):
                
                if charDict.__contains__(givenString[i]):
                    value = charDict.get(givenString[i])
                    charDict[givenString[i]] = value + 1
                else:
                    charDict[givenString[i]] = 1
                
                i = i + 1
            print (" >>>> charDict >>>> ", charDict)
            
            #k for (k, v) in charDict.iteritems() if v == 1:
            
            
            for n in charDict:
                if charDict.get(n) == 1:
                    #print (">>>> The First Non Repeating Character is >>>>  ", charDict.keys().__getattribute__(n))
                    #print (">>>> The First Non Repeating Character is >>>>  ", charDict.__getitem__(n)). 
                    print (">>>> The First Non Repeating Character Found >>>>  ", charDict.keys())
                    break
                else:
                    print (">>>> charDict.get(n) >>>> ", charDict.get(n))
                    continue
                    
obj = FirstNonRepeatingChar()
obj.firstCharNonRepeating_ForString("RohiniKumari")                    
