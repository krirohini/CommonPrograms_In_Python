'''
Created on Feb 12, 2019

@author: r.kumari
'''

class SmallestAndLargest_In_UnsortedArray:

    def smallestAndLargest(self, givenArray):
        
        length = len(givenArray)
        
        smallest = 0
        largest = 0
        
        i = 0
        while i < length:
            print(">>>> i >>>>", i)
            if givenArray[i] < smallest:
                smallest = givenArray[i]
            else:
                smallest = smallest
                
            if givenArray[i] > largest:
                largest = givenArray[i]
            else:
                largest = largest
            
            i = i + 1
            
        print (">>>> givenArray >>>> ", givenArray)
        print (">>>> smallest >>>> ", smallest)
        print (">>>> largest >>>> ", largest)
        
obj = SmallestAndLargest_In_UnsortedArray()
obj.smallestAndLargest([1,4, 2, 9, 0, -5, -2, 555, -21])