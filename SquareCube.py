# Take numbers from 1 to 50, square the even numbers, and cube the odd numbers using loop.....
# declare if statement for even number if num int input % 2(even divisor) is equal to no remainder(0)
# print result
# else print result xx 3 using arithmetic operator

for num in range(1, 51):
    if num % 2 == 0:
        result = num ** 2

        print(f"Square of even number {num} is {result}")
	
    else:
        result = num ** 3
        print(f"Cube of odd number {num} is {result}")