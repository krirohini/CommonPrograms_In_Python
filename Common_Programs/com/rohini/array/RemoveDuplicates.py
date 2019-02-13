'''
Created on Feb 13, 2019

@author: r.kumari
'''
class RemoveDuplicates:
    
    def removeDuplicates(self, givenArray):
        
        length = len(givenArray)
        
        print (">>>> givenArray >>>> ", givenArray)
        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
        i = 0
        set = []
        duplicates = []
        
        if length == 1:
            print (">>>> Array is having only one element >>>> ", givenArray)
        else:
            while i < length :
                if givenArray[i] in set:
                    print (">>>> Duplicate Number Found >>>> ", givenArray[i] )
                    duplicates.append(givenArray[i])
                else:
                    print (">>>> New Pair Found >>>> ", givenArray[i] )
                    set.append(givenArray[i])
                    
                i = i + 1
        print (">>>> Duplicate Numbers are >>>> ", duplicates)   
        print (">>>> After Removing Duplicate Numbers >>>> ", set)   
             
        
obj = RemoveDuplicates()
obj.removeDuplicates([1,4, 2, 9, 0, -5, -2, 555, -21, -5, 5, 13, 11, 4, 5, 2])