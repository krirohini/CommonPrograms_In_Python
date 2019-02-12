'''
Created on Feb 11, 2019

@author: r.kumari
'''

class CheckSubString:
    

    
    def isSubString(self, givenString, givenSubString):
        
        
        listOfIndex = self.indexOf_FirstChar_Of_Substring(givenSubString, givenString)
        print(">>>> listOfIndex >>>> ", listOfIndex)
        
        print ("\n >>>> Given String ", givenString)
        print (">>>> Given SubString ", givenSubString)
        print ()
        
        length = len(givenSubString)
        
        for i in listOfIndex:
            currentIndex = i
            j = 1
            insideIteratorIndex = i + 1 
            while j < length:
                # codition - if last index is same as same size of the string 
                if currentIndex + 1  == len(givenString):
                    print("Reached to last Index")
                    break;
                else:
                    print (">>>> givenString[", insideIteratorIndex, "] >>>>", givenString[insideIteratorIndex]) 
                    print (">>>> givenSubString[", j, "] >>>>", givenSubString[j]) 
                    
                    if givenString[insideIteratorIndex] == givenSubString[j]:
                        print(" >>>> Character Matched >>>> ")
                        
                        print ("j + 1 >>>> ", j+1)
                        print ("length >>>> ", length)
                        
                        if j + 1 == length:
                            print(">>>> Substring Found at Index >>>> " , i)
                            break
                            
                        else:
                            j = j + 1
                            insideIteratorIndex = insideIteratorIndex + 1 
                            #pass
                    else:
                        print("Substring NOT Found At The index" , currentIndex)
                        break
            
            break
        
    def indexOf_FirstChar_Of_Substring(self , givenSubString, givenString):
        listOfIndex = []
        
        i = 0
        while i < len(givenString):
            if givenString[i] == givenSubString[0]:
                listOfIndex.append(i)
            else:
                pass
            i = i + 1
        return listOfIndex
    
obj = CheckSubString()
obj.isSubString("Rohini Kumiri", "ini")
    
    