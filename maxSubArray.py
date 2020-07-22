
def maxCrsgSubArr(A,lo,mid,hi):
    leftsum = -100000                #leftsum == a big negative num
    summ = 0
    for i in reversed(range(lo,mid)):
       
        summ = summ + A[i]
        if(summ > leftsum):
            leftsum = summ
            maxleft = i
    rightsum = -10000                 #rightsum == a big negative num
    summ = 0
    for i in range(mid,hi):
        summ = summ + A[i]
        if(summ > rightsum):
            rightsum = summ
            maxright = i
    return max(rightsum + leftsum, leftsum, rightsum)

#lo hi and mid are lowest highest"(len(A)-1)"and mid indexes of list respectively
def maxSubArr(A,lo,hi):
    if(lo == hi):
        return A[lo]
    else:
        mid = int((lo+hi)//2)
        ls = maxSubArr(A,lo,mid)
        rs = maxSubArr(A,mid+1,hi)
        cs = maxCrsgSubArr(A,lo,mid,hi+1)     #hi+1 will include the last element
        return max(rs,cs,ls)

A = [2,3,4,5,7]
s = maxSubArr(A,0,len(A)-1)
print(s)
