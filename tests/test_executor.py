import os
import re
import sys
sys.path.insert(1, '..')
from problem.problem import main

def execute_tests(input, output):
	valid_pairs = input.intersection(output)
	n = len(valid_pairs)
	passed = 0
	for i in sorted(valid_pairs):
		inp = open("in/"+str(i)+".txt", "r", encoding = "utf8").readlines()
		exp = open("exp/"+str(i)+".txt", "r", encoding = "utf8").read()
		is_same = main(inp) == exp
		passed += int(is_same)
		assert is_same
	print(str(passed)+"/"+str(n)+" tests passed")
def allo():
	assert "1"=="2"
#allo()
			
#if __name__ == '__main__':
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

execute_tests(input, output)