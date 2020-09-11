import math
import os
import random
import re
import sys
from collections import Counter
# Complete the abbreviation function below.
def abbreviation(a, b):
	cb = Counter(b)
	ca = {}
	i=0
	j=0
	while j < len(b):
		c = a[i]
		if c.isupper():
			try:
				ca[c] +=1
			except KeyError:
				ca[c] = 1

			try:
				assert ca[c]/(j+1) <= cb[c]
			except (AssertionError, KeyError):
				return "NO"
				
		while a[i].upper() != b[j]:
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