import numpy as np
import math
import copy

T = int(input())
for case in range(0,T):
    helper = (list)(map(int,input().split(" ")))
    numStudents, numQuestions = helper[0],helper[1]
    probT = [0] * numQuestions
    for i in range(0, numStudents):
        helper2 = list(map(str,input().split(" ")))
        answers,score  = helper2[0],helper2[1]
        score = int(score)
        answers = list(answers)
        
        for j in range(0,numQuestions):
            if answers[j] == 'F':
                probT[j] += 1-(score/numQuestions)
            else:
                probT[j]+= score/numQuestions
       
    probT = [prob/numStudents for prob in probT]  
    ans = ""
    for i in range(0,len(probT)):
        if probT[i] > .5:
            ans+="T"
        else:
            probT[i] = 1-probT[i]
            ans+="F"
    
    print(f"Case #{case+1}: {ans} {int(round((np.sum(probT)/numQuestions*numQuestions),0))}/1")
    #doesnt work - good aproximation