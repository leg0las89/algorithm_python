def productOfArray(arr):
    mult = 1
    for i in range(0,len(arr)):
        mult *= arr[i]# * arr[i+1]
        
    return mult

print(productOfArray([1,2,3,4]))