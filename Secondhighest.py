##you are given three integers variables x ,y, z each representing the score a student got in three subject. determine and print the second highest score . 

# input x = 62
# input y = 98
# input z = 85

score_x = int(input('Enter score x: '))
score_y = int(input('Enter score y: '))
score_z = int(input('Enter score z: '))

if score_x >= score_y and score_x >= score_z:
    # score_x is the highest
    if score_y >= score_z:
        second_highest = score_y
    else:
        second_highest = score_z
elif score_y >= score_x and score_y >= score_z:
    # score_y is the largest
    if score_x >= score_z:
        second_highest = score_x
    else:
        second_highest = score_z
else:
    # score_z is the largest
    if score_x >= score_y:
        second_highest = score_x
    else:
        second_highest = score_y

print('Second highest score is: ' , second_highest)

