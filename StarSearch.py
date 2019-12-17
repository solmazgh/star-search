'''Project 4
star search 
by solmaz gharagozloo
10/21/2018'''

print("\033[0;34m----------------------Welcome To Los Angeles Great Match----------------------\n")
def getJudgeData(score):
    score=float(input("\033[1;30mplease enter your score between 0-10: "))
    if(score<0 or score>10):
          print("\033[1;31m --your input is not in the range--")
      
          score=float(input("\033[1;30mPlease re-enter your score: "))
          
    return score
   
def findLowest(score1, score2, score3, score4, score5):
        min=score1
        if(score2<score1):
            min=score2
        if(score3<score2):
            min=score3
        if(score4<score3):
            min=score4
        if(score5<score4):
            min=score5
            
        return min 
def findhighest(score1, score2, score3, score4, score5):
        max=score1
        if(score2>score1):
            max=score2
        if(score3>score2):
            max=score3
        if(score4>score3):
            max=score4
        if(score5>score4):
            max=score5
            
        return max
        
        
def  calcScore(score1, score2, score3, score4, score5):
    total=(score1+score2+score3+score4+score5-findhighest(score1, score2, score3, score4, score5)-findLowest(score1, score2, score3, score4, score5))
    avg=total/3
    return avg
    
    
print("\033[1;30mjudge1: ") 
judge1 = getJudgeData(1);
print("judge2: ") 
judge2 = getJudgeData(2);
print("judge3: ") 
judge3 = getJudgeData(3);
print("judge4: ") 
judge4 = getJudgeData(4);
print("judge5: ") 
judge5 = getJudgeData(5);
print("\033[0;34m--------------------------------------------------------------------------------------")
print("\033[1;32mThe average of the scores is: ", format(calcScore(judge1,judge2,judge3,judge4,judge5),'.2f'))


            
            