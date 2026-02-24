 #     *
 #    ***
 #   *****
 #  *******
 # *********

row = int(input("Enter your triangle row : "))

for i in range(row): # (start, end, step)
	space = row - i
	steps = 2 * i + 1
	print(" " * space , "*" * (steps))




