# Using recursive in Python is not recommended
# This is just an example of how it works

def fact(num):
	if num == 1:
		return 1
	else:
		return num * fact(num - 1)

print(fact(30))
