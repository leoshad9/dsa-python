# Author: Mohd Shadman
# Topic: Linear Search

arr = [1,2,3,4,5]
n = int(input())

def lsr(arr,n,L,H):

    for L in range(H):
        if arr[L] == n:
            return 1

if lsr(arr,n,0,len(arr) - 1)==1:
    print("Found")
else:
    print("Not Found")
