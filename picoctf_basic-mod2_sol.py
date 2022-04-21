#!/usr/bin/env python3 -u

import string
flag = []


with open("message.txt") as file:
	contents = file.read()
	lst = [int(i) for i in contents.split()]
	

	for num in lst:
		i = pow(num,-1, 41)
		
		if i in range(1,27):
			flag.append(string.ascii_uppercase[i-1])
		elif i in range(27,37):
			flag.append(string.digits[i-27])
		else:
			flag.append("_")

print("picoCTF{"+("".join(flag))+"}")
