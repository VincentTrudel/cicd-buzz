import math
import os
import random
import re
import sys
# Complete the abbreviation function below.
def abbreviation(a, b):
	a = a.upper()
	i=0
	j=0
	while j < len(b):
		while a[i] != b[j]:
			i+=1
			if i==len(a):
				return "NO"
		j+=1
	return "YES"
	
	
def main(inp):
	output = ""
	q = int(inp[0].rstrip())
	for q_itr in range(q):
		a = inp[q_itr*2+1].rstrip()
		b = inp[q_itr*2+2].rstrip()
		result = abbreviation(a, b)
		output+=result + '\n'

	return output.rstrip()
	
if __name__ == '__main__':
	main()