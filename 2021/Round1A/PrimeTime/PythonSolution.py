import numpy as np
import math
import copy
def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2),
        n = n / 2
    
  
    for i in range(3,int(math.sqrt(n))+1,2):
     
        while (n % i == 0):
            factors.append(int(i))
            n = n / i
    
    if n > 2:
        factors.append(int(n))
    return factors
def checkArr(facs, nums,counts):
    nums2, counts2 = copy.deepcopy(nums), copy.deepcopy(counts)
   
    for num in facs:
        
        if num not in nums2:
            return False
        index = nums2.index(num)
        counts2[index]-=1
        if counts2[index] == -1:
            
                
            return False
    return True
T = int(input())
for case in range(0,T):
    N = int(input())
    
    nums, counts = [],[]
    maxSum = 0
    for i in range(0,N):
        helper = (list)(map(int,input().split(" ")))
        nums.append(helper[0]) 
        counts.append(helper[1]) 
        maxSum += helper[0]*helper[1]
    
           
    ans = 0
    
    for value in range(maxSum,2, -1):
        
        facs = primeFactors(value)
        
        if len(facs) == 0 or not all(i <= 499 for i in facs):
            continue
        m = np.sum(facs)
        if maxSum - m == value:
            if not checkArr(facs,nums,counts):
                
                continue
            ans = value
            break
    print(f"Case #{case+1}: {ans}")