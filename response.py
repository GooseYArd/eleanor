import sys
import random

responses = ["Yes", "No", "Talk to me later", "Thats terrible!", "Possibly", "Maybe", "I cannot tell you!",  "You suck", "I dont know", "Definetley"]
sys.stdout.write ("What is your name?")
name = sys.stdin.readline().strip("\n")
while True:
	sys.stdout.write("Hello, %s , ask me any question you like!" %name)
	question = sys.stdin.readline()
	sys.stdout.write ("ooohhhh.... that's a hard one! lets see....\n")
	print random.choice(responses)


