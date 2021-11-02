T = int(input())
for case in range(0,T):
    N = int(input())
    
    total = 0
    ar = (list)(map(int, input().split(" ")))
   
    for i in range(1,len(ar)):
        ans = 0
        while ar[i] <= ar[i-1]:
            
            ar[i]*=10
            ans+=1
        if ans > 1 and (ar[i]//10) + ( 10**(ans-1))-1 > ar[i-1]:
            ans-=1
            ar[i] = ar[i-1]+1
        total+=ans  
           
            
                    
           
        
    
    print("Case #{}: {}".format(case+1, total))