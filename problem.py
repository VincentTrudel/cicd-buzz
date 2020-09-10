import math
import os
import random
import re
import sys
# Complete the abbreviation function below.
def abbreviation(a, b):
	#print(a)
	a = "".join([c for c in list(a) if c.isupper() or (c.lower() in b.lower())])
	if a.upper() == b.upper():
		ret = "YES"
	else:
		ret = "NO"
	return ret
	
	
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