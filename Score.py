##you are given three integers variables a ,b, c each representing the score a student got in three subject. determine and print the highest score . 

##input a = 98
##input b = 85
##input c = 62


score_a = int(input('Enter score a: '))
score_b= int(input('Enter score b: '))
score_c = int(input('Enter score c: '))

highest = max (score_a, score_b, score_c)

print('The highest score is:' , highest)
