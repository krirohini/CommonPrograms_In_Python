'''
Created on Feb 13, 2019

@author: r.kumari
'''

class FindAllPairs_ForGivenSum:
    
    def findAllPairs(self, givenArray, givenSum):
        
        length = len(givenArray)
        
        print (">>>> givenArray >>>> ", givenArray)
        print (">>>> givenSum >>>> ", givenSum)
        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
        count = 0
        i = 0
        set = []
        dict = {}
        if length == 1:
            print (">>>> Array is having only one element >>>> ", givenArray)
        else:
            while i < length - 1:
                j = 1
                
                while j < length:
                    if givenArray[i] + givenArray[j] == givenSum:
                        
                        if givenArray[i] in set and givenArray[j] in set:
                            print (">>>> Same Pair Found >>>> ", givenArray[i] , " And  >>>> ", givenArray[j])
                        else:
                            print (">>>> New Pair Found >>>> ", givenArray[i] , " And  >>>> ", givenArray[j])
                            set.append(givenArray[i])
                            set.append(givenArray[j])
                            count = count + 1
                            dict[count] = [givenArray[i], givenArray[j]]
                    else:
                        pass
                    j = j + 1 
                i = i + 1
        print ("\n>>>> Number of Pairs are >>>> ", count)   
        print (">>>> Paired Numbers are >>>> ", dict)   
             
        
obj = FindAllPairs_ForGivenSum()
obj.findAllPairs([1,4, 2, 9, 0, -5, -2, 555, -21, 5, 13, 11], 13)