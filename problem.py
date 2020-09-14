import math
import os
import random
import re
import sys
from collections import Counter
# Complete the abbreviation function below.

def abbreviation(a, b):
	
	ca_upper = Counter([c for c in a if c.isupper()])
	cb = Counter(b)
	try:
		for c in ca_upper.keys():
			if ca_upper[c]>cb[c]:
				return "NO"
	except KeyError:
		return "NO"
	
	m = len(a)
	n = len(b)

	L = [[None]*(n + 1) for i in range(m + 1)] 

	for i in range(m + 1): 
		for j in range(n + 1):
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif a[i-1].upper() == b[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j], L[i][j-1]) 

	if L[m][n] == n:
		return "YES"
				
	return "NO"

	
	


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