import os
from problem import main
import unittest
import inspect

def lcs(X, Y): 

    m = len(X) 
    n = len(Y) 

    L = [[None]*(n + 1) for i in range(m + 1)] 

    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 

    return L[m][n]

input = set()
output = set()

for r, d, f in os.walk("in"):
	for file in f:
		if '.txt' in file:
			input.add(file.replace(".txt", ""))

for r, d, f in os.walk("exp"):
	for file in f:
		if '.txt' in file:
			output.add(file.replace(".txt", ""))

valid_pairs = input.intersection(output)
success = {}
for i in sorted(valid_pairs):
	inp = open("in/"+i+".txt", "r", encoding = "utf8").readlines()
	exp = open("exp/"+i+".txt", "r", encoding = "utf8").read()
	out = main(inp)
	#exp_lines = exp.split("\n")
	#out_lines = out.split("\n")

	#pct_same = lcs(exp, out)/max(len(exp), len(out))
	
	exec ("def test_"+i+"(): assert success[int(inspect.stack()[0][3].split('test_')[1])]")
	#This creates a function for every test so that pytest recognizes it and asserts once per test

	
	success[int(i)]= out == exp
	'''if not passed:
		print(lcs(exp_lines, out_lines), max(len(exp_lines), len(out_lines)))
		print("In:\n"+"\n".join(inp))
		print("Test "+str(i)+" failed")
		print("Out:\n"+out)
		print("Expected:\n"+exp)
		'''
	exec ("test_"+str(i))

print(sum([int(x) for x in list(success.values())]))
print(len(success))
	
	


