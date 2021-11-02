import numpy as np
T = int(input())
for case in range(T):
    
    N = int(input())
    ar = input().split()
    ar = [int(i) for i in ar]
    cost = 0
    for i in range(0,N-1):
        index = ar.index(i+1)
        ar[i:index+1] = reversed(ar[i:index+1])
        cost+=index-i+1
        
    print("Case #"+str(case+1)+": " + str(cost))