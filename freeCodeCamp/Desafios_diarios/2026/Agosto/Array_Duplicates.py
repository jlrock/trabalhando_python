'''
Array Duplicates

Given an array of integers, return an array of integers that appear more than once in the initial array, 
sorted in ascending order. If no values appear more than once, return an empty array.
Only include one instance of each value in the returned array.

Testes:
1. find_duplicates([1, 2, 3, 4, 5]) 
should return [].

2. find_duplicates([1, 2, 3, 4, 1, 2]) 
should return [1, 2].

3. find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]) 
should return [-6, 0, 2, 4, 5, 23].
'''

def find_duplicates(arr):
    tam = len(arr)
    arr_temp=[]

    for i in range(tam):
        count=0
        for j in range(tam):
            if arr[i]==arr[j] and i!=j:
                count+=1
        if count>0:
            arr_temp.append(arr[i])
    
    arr_temp.sort()
    arr_temp.append('aux')
    
    final_arr=[]
    
    for i in range(len(arr_temp)-1):
        if arr_temp[i]!=arr_temp[i+1]:
            final_arr.append(arr_temp[i])
    
    return final_arr

print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 2, 3, 4, 1, 2]))
print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))