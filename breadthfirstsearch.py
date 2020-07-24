#representing graph in dictionary 
Dict = {
        1: [2,3,4,0],
        2: [1,3,4,7],
        3: [1,2,7],
        4: [1,2],
        5: [6,8],
        6: [5,8],
        7: [2,3,8],
        8: [6,7,5],
        'v' : [1,2,3,4,5,6,7,8]}

#BFS algorithm
def BFS(Dict,s):
    if( 0 not in Dict['v']):
        vstd = [None]
    else:
        vstd = []
    
    for i in Dict['v']:
        if(Dict[i] == None):
            vstd.insert(i,-1)
        else:
            vstd.insert(i,0)
    que = []
    vstd[s] = 'no dist'
    head = 0
    tail = 0
    que.insert(head,s)
    weight = 0
    while(len(que) != 0):
        z = que[head]
        que.pop(head)
        for n in Dict[z]:
            if(vstd[n] == 0):
                weight = weight + 6             #if weight of each node is 6
                break

        for n in Dict[z]:
            if(vstd[n] == 0):
                vstd[n] = weight
                tail = tail + 1
                que.insert(tail,n)
    return vstd

print("BFS by Dict: ")
s = 7
print(BFS(Dict,s))
