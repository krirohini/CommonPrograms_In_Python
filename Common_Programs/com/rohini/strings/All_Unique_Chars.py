'''
Created on Feb 11, 2019

@author: r.kumari
'''

class All_Unique_Chars:
    
    
    def unique_Chars(self, givenString):
        if len(givenString) == 0:
            print("Length of Given String is 0.")
        elif len(givenString) == 1:
            print("Given String is having all unique characters.")
        else:
            length = len(givenString)
            print(">>>> givenString >>>> " , givenString)
            
            char_count_dict = { }
            i = 0
            
            # counting of each characters of given string in a dictionary (Key-value).
            while i < length:
                count = 1
                if i < length:
                    #print (">>>> i >>>>", i)
                    #print(">>>> givenString[",i,"] >>>>" , givenString[i])
                    if char_count_dict.__contains__(givenString[i]):
                        count = count + 1
                        char_count_dict[givenString[i]] = count
                        #print(char_count_dict)
                    else:
                        char_count_dict[givenString[i]] = count

                    count = 0;
                    i = i + 1
                else:
                    print("Done") 
            
            print(char_count_dict)
            
            if char_count_dict.__sizeof__() == length:
                print("Given String is having all unique characters.")
            else:
                print(" Thus, Given String is NOT having all unique characters.")
            
obj = All_Unique_Chars()
obj.unique_Chars("Rohini")
#obj.unique_Chars("R")
#obj.unique_Chars("Ro")
#obj.unique_Chars("Rooo")
#obj.unique_Chars("")