# Author: Mohd Shadman
# Topic: Binary Search

arr = [1,2,3,4,5]
n = int(input())

def bsr(arr,n,L,H):

    while L < H:
        M = (H+L)//2

        if arr[M] == n:
            return 1
            break

        elif arr[M] < n:
            L = M+1

        else:
            H = M-1

if bsr(arr,n,0,len(arr) - 1)==1:
    print("Found")
else:
    print("Not Found")
