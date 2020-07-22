'''This program will return the maximum sub-array with brute force code.
The efficiency of this code is O(n^2) '''
def bruteMaxArr(A):
    cache = []                 #list to store different sub arrays
    for i in range(len(A)): 
        summ = 0
        for j in range(len(A)):
            summ = sum(A[i:len(A)-j])
            cache.append(summ)
    return max(cache)
