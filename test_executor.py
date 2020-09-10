import os
from problem import main
import unittest


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
	success[int(i)]=is_same

def test_0():
	assert success[0]
def test_1():
	assert success[1]
def test_2():
	assert success[2]
def test_3():
	assert success[2]
def test_10():
	assert success[10]
def test_15():
	assert success[15]

