#problem on hacker rank
#https://www.hackerrank.com/challenges/stockmax/problem

#first we will write a function which will check whether the list is strictly decreasing or not

def chkDecreasing(A):
    for i in range( len(A) - 1 ):
        if A[i] < A[i+1]:
            return False
    return True

def makelist(A,l,r):
    for i in range(A.index(max(A))+1):
        l.append(A[i])
    for i in range(A.index(max(A))+1,len(A)):
        r.append(A[i])
    return l,r

def stockmax(prices):
    profit = 0
    if(len(prices) == 1):
        return 0
    if(chkDecreasing(prices) == True):
        profit = 0
    
    elif(prices[len(prices)-1] == max(prices)):
        profit = (len(prices)*prices[len(prices)-1]) - sum(prices[:len(prices)])
        
    else:
        llist = []
        rlist = []
        llist, rlist = makelist(prices,llist,rlist)    
        profit = profit + stockmax(llist)
        
        profit = profit + stockmax(rlist)
        
    return profit

if __name__ == '__main__':
    n = int(input("Size of prices: ").strip())
    print("Enter the prices")
    prices = list(map(int, input().rstrip().split()))
    memo = []
    prf = 0
    result = stockmax(prices)
    print("result = ",result)

    