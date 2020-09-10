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
for i in sorted(valid_pairs):
	inp = open("in/"+i+".txt", "r", encoding = "utf8").readlines()
	exp = open("exp/"+i+".txt", "r", encoding = "utf8").read()
	is_same = main(inp) == exp
	exec ("def test_"+i+"(): assert success[int(inspect.stack()[0][3].split('test_')[1])]")
	#This creates a function for every test so that pytest recognizes it and debugs per function
	
	success[int(i)]=is_same
	exec ("test_"+str(i))

	
	


