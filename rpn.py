#!/usr/bin/env python3

def calculate(input):
	stack = list()
	for token in input.split():
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg2 - arg1
			stack.append(result)
		elif token == '*':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 * arg2
			stack.append(result)
		else:
			stack.append(int(token))

	if len(stack) != 1:
		raise TypeError
	return stack[0]

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()
