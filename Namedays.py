# You are given an integer n between 1 and 7 (inclusive). Print the name of the day of the week that corresponds to that number, where:

#1 -> Monday
#2 -> Tuesday

#......

#7 -> Sunday
#input: n = 5
#Output: Friday

# Monday -> 1
# Tuesday -> 2
# Wednesday -> 3
# Thursday -> 4
# Friday -> 5
# Saturday -> 6
# Sunday ->7



day = int(input('Enter a day selection: '))

if (day == 1):
	print('Monday')

day = int(input('Enter a day selection: '))
if (day == 2):
	print('Tuesday')

day = int(input('Enter a day selection: '))
if (day == 3):
	print('Wednesday')

day = int(input('Enter a day selection: '))
if (day == 4):
	print('Thursday')

day = int(input('Enter a day selection: '))
if (day == 5):
	print('Friday')

day = int(input('Enter a day selection: '))
if (day == 6):
	print('Saturday')

day = int(input('Enter a day selection: '))
if (day == 7):
	print('Sunday')



