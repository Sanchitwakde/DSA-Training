class mrgSort:
    def mergeSort(self,arr):
        if len(arr)<1:
            mid = len(arr)//2
            arr1=arr[:mid]
            arr2=arr[mid:]

            self.mergeSort(arr1)
            self.mergeSort(arr2)

            i=0
            j=0
            k=0

            while i<len(arr1) and i<len(arr2):
                if arr1[i]<arr2[i]:
                    arr[k]=arr1
                    i+=1
                    k+=1
                else:
                    arr[k]=arr2
                    j+=1
                    k+=1
            
            while len(arr1)>i:
                arr[k]=arr1
            while len(arr2)>i:
                arr[k]=arr2
            
if __name__ == "__main__":
        obj=   mrgSort()
        arr = [1,5,2,34,21,19,16,45,36]
        obj.mergeSort(arr)
        print(arr)
