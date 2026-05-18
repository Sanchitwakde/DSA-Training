#divide the list into smaller parts
# sort each smaller part
#merge them back together 

class MergeSort:
    
    def mergearr(self,arr):
    
        if len(arr) <=1:
            return arr #this is imp because it should stop recursive funtion at one point else it will be in loop and not run 
        
        mid = len(arr)//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]

        arr1 = self.mergearr(arr1)
        arr2 = self.mergearr(arr2)

        return self.merge_sort(arr1,arr2)
    
    def merge_sort(self,arr1,arr2):
        arr3= []
        i=0
        j=0
        k=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr3.append(arr1[i])
                i+=1
                k+=1
            else:
                arr3.append(arr2[j])
                j+=1
                k+=1
            
        while len(arr1)>i:
            arr3.append(arr1[i])
            i +=1
            k +=1
        while len(arr2)>j:
            arr3.append(arr2[j])
            j+=1
            k+=1
        return arr3
    
if __name__ == "__main__":
    obj=MergeSort()
    arr=[1,5,2,34,21,19,16,45,36]
    obj.mergearr(arr)
    print(arr)