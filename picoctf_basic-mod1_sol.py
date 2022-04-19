#!/usr/bin/env python3 -u

import string
flag = []

num = [17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 1, 32, 1, 28, 31, 31, 29, 27]


for i in num:
	if i in range(26):
		flag.append(string.ascii_uppercase[i])
	elif i in range(26,35):
		flag.append(string.digits[i-26])
	else:
		flag.append("_")

print("picoCTF{"+("".join(flag))+"}")
