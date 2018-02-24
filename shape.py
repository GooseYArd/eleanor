import sys
import random

for i in range (10):
	for j in range (random.Random().randint(0, 100)):
		sys.stdout.write("*")
	print
