import os
from problem import main
import unittest
import inspect

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
for i in sorted(valid_pairs, key = lambda x: int(x)):
	inp = open("in/"+i+".txt", "r", encoding = "utf8").readlines()
	exp = open("exp/"+i+".txt", "r", encoding = "utf8").read().rstrip()
	out = main(inp)
	el = exp.rstrip().split("\n")
	ol = out.rstrip().split("\n")
	
	exec ("def test_"+i+"(): assert success[int(inspect.stack()[0][3].split('test_')[1])]")
	#This creates a function for every test so that pytest recognizes it and asserts once per test
	passed = out == exp
	success[int(i)]= passed
	if not passed:
		#print("In:\n"+"\n".join(inp))
		#print("Test "+str(i)+" failed")
		print("\nOut:\n"+out+"")
		print("Expected:\n"+exp)
	
	exec ("test_"+str(i))

print(sum([int(x) for x in list(success.values())]))
print(len(success))

	


