import cProfile
import sys
sys.path.insert(1, '../buzz/')
import generator
from inspect import getmembers, isfunction

functions_list = [o for o in getmembers(generator) if isfunction(o[1])]
#print(functions_list[0])
#exit()
for f in functions_list:
	print(cProfile.run("generator."+f[0]+"()"))