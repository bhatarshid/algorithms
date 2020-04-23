#problem on hacker rank
#https://www.hackerrank.com/challenges/stockmax/problem

#first we will write a function which will check whether the list is strictly decreasing or not

def chkDecreasing(A):
    for i in range( len(A) - 1 ):
        if A[i] < A[i+1]:
            return False
    return True

def chkIncreasing(A):
    for i in range( len(A) - 1 ):
        if A[i] > A[i+1]:
            return False
    return True

def makelist(A,l,r):
    for i in range(A.index(max(A))+1):
        l.append(A[i])
    for i in range(A.index(max(A))+1,len(A)):
        r.append(A[i])
    return l,r

def stockmax(prices,profit,l):
    if(len(prices) == 1):
        return 0
    if(chkDecreasing(prices) == True):
        profit = 0
        prices.append(profit)
        l.append(prices)
    elif(prices[len(prices)-1] == max(prices)):
        profit = (len(prices)*prices[len(prices)-1]) - sum(prices[:len(prices)])
        prices.append(profit)
        l.append(prices)
    else:
        llist = []
        rlist = []
        llist, rlist = makelist(prices,llist,rlist)    
        if(llist in l):
            profit = profit + l[l.index(llist)][len(llist)-1]
        else:
            profit = profit + stockmax(llist,profit,l)
        if(rlist in l):
            profit = profit + l[l.index(rlist)][len(rlist)-1]
        else:
            profit = profit + stockmax(rlist,profit,l)
    return profit

if __name__ == '__main__':
    n = int(input("Size of prices: ").strip())
    print("Enter the prices")
    prices = list(map(int, input().rstrip().split()))
    dlist = []
    prf = 0
    result = stockmax(prices,prf,dlist)
    print("result = ",result)

    