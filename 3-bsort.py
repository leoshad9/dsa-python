# Author: Mohd Shadman
# Topic: Bubble Sort

arr = [3,1,5,4,9,2,6,8,7]
l=len(arr)-1
swap=-1                     # For Best Case Time Complexity: O(n)
for i in range(l):
    for j in range(l-i):
        if arr[j] > arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            swap=1
    if swap==-1:
        break
print(arr)
