# NEED TO SPEND SOME MORE TIME WITH THE CONCEPT

def rec_binarySearch(target,sequence,first,last):
    if first>last:
        return False
    else:
        mid=(first + last)//2
        if sequence[mid]==target:
            return True
        elif target < sequence[mid]:
            return rec_binarySearch(target,sequence,first,mid-1)
        else:
            return rec_binarySearch(target,sequence,mid+1,last)

list = [1, 3, 4, 7, 8, 9, 10, 45, 50, 90, 100, 150, 600, 1000]
n = 8
print(rec_binarySearch(n,list,1,3))

'''Recursion means solving problems by breaking down a complex problem into smaller problems
and then solving it step by step. Binary search means to find an item in a sorted array by
repeatedly dividing the search interval into two halves and recursive binary search means to subdivide
the entire binary search process into smaller problems. Simply put, the recursive solution to a binary search
is known as a recursive binary search. Here is how to implement a recursive binary search using Python:'''

# https://thecleverprogrammer.com/2020/08/28/binary-search-algorithm-with-python/