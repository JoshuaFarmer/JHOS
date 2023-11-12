# version 0.71 Alpha

from random import *
import sys
import os

program = []

def shell():
	inp = ""
	while inp.upper() != "RUN":
		inp = input()
		if "\t" in inp:
			inp = inp.strip("\t")
		if ";" in inp:
			inp = inp.split(";")
			for i in inp:
				program.append(i)
			inp = ""
		else:
			program.append(inp)

if len(sys.argv) > 1:
	file = open(sys.argv[1], "r")
	program_ = file.read().split("\n")
	#index = 0
	#while index != len(program):
	#	program[index] = program[index].strip("\t")
	#	index += 1
	for line in program_:
		if "\t" in line:
			line = line.strip("\t")
		if ";" in line:
			line = line.split(";")
			for line_ in line:
				program.append(line_)
			line = ""
		else:
			program.append(line)
else:
	shell()

class returnLine:
	global value; value = 0

functionLocations = []
functionNames = []

variableNames = ["OUT","PI"]
variableValues = [0,3.14159265359]

if len(sys.argv) > 2:
	variableNames.append("ARG")
	variableValues.append(sys.argv[2])
line = ""
global i; i = 0

def findFunctions():
	j = 0
	while j < len(program):
		if (program[j].split(" ")[0].upper() == "FUNCTION"):
			while (program[j + 1] != "{"):
				j+=1
			functionNames.append(program[j].split(" ")[1].upper())
			functionLocations.append(j + 2)
		j += 1
	return functionLocations[functionNames.index("MAIN")]


i = findFunctions()
def getJHOSVar(nam):
	return variableValues[variableNames.index(nam)]
def setJHOSVar(nam, value):
	variableValues[variableNames.index(nam)] = value


def parser(i):
	## added by joshua, 11/11/2023 ##
	if line.split(" ")[0].upper() == "USING":
		importedFile = open(line.split(" ")[1], "r")
		for importedLine in importedFile.read().split("\n"):
			program.append(importedLine)
		findFunctions()

	elif line.split(" ")[0].upper() == "UNDEFINE":
		variableValues.pop(variableNames.index(line.split(" ")[1]))
		variableNames.pop(variableNames.index(line.split(" ")[1]))
	
	elif line.split("(")[0].upper() == "IF":
		if line.split("(")[1].split(" ")[0].isnumeric():
			a = line.split("(")[1].split(" ")[0]
		else:
			a = variableValues[variableNames.index(line.split("(")[1].split(" ")[0])]
			
		if line.split(")")[0].split(" ")[2].isnumeric():
			b = line.split(")")[0].split(" ")[2]

		elif line.split(" ")[3] == "(STR)":
			b = line.split(")")[0].split(" ")[2]
		else:
			b = variableValues[variableNames.index(line.split(")")[0].split(" ")[2])]
				
		if line.split(" ")[1].upper() == "EQUAL_TO":
			if a == b:
				return i + 1
			else:
				while program[i] != "}":
					i += 1
				return i
		elif line.split(" ")[1].upper() == "NOT_EQUAL_TO":
			if a != b:
				return i + 1
			else:
				while program[i] != "}":
					i += 1
				return i
			
		elif line.split(" ")[1].upper() == "LESS_THAN":
			if float(a) < float(b):
				return i + 1
			else:
				while program[i] != "}":
					i += 1
				return i
			
		elif line.split(" ")[1].upper() == "GREATER_THAN":
			if float(a) > float(b):
				return i + 1
			else:
				while program[i] != "}":
					i += 1
				return i
	
	elif line.split(" ")[0].upper() == "SKIP":
		return i + 1
	
	elif line.split(" ")[0].upper() == "LOOP":
		times = 1
		while program[i] != "{" and times != 0:
			if program[i] == "}":
				times += 1
			elif program[i] == "{":
				times -= 1
			i -= 1
		return i
	####################################################
	elif line.split(" ")[0] == "//":
		return i
	
	elif line.split(" ")[0].upper() == "DECLARE" or line.split(" ")[0].upper() == "DEFINE":
		nam = line.split(" ")[1]
		val = line.split('as"')[1].split('"')[0]
		variableNames.append(nam)
		if line.split('as"')[1].split('"')[1] == "(STR)" or val.isnumeric() or line.split('as"')[1].split('"')[1] == "(NUM)":
			variableValues.append(val)
		elif line.split('as"')[1].split('"')[1] == "(NULL)":
			variableValues.append("")
		else:
			variableValues.append(variableValues[variableNames.index(val)])
	
	elif line.split(" ")[0].upper() == "REDEFINE":
		nam = line.split(" ")[1]
		val = line.split('as"')[1].split('"')[0]
		if line.split('as"')[1].split('"')[1] == "(STR)" or val.isnumeric() or line.split('as"')[1].split('"')[1] == "(NUM)":	
			variableValues[variableNames.index(nam)] = val
		elif line.split('as"')[1].split('"')[1] == "(NULL)":
			variableValues[variableNames.index(nam)] = ""
		else:
			variableValues[variableNames.index(nam)] = variableValues[variableNames.index(val)]

	elif line.split('"')[0].upper() == "SYS":
		if line.split('"')[2].upper() == "(VAR)":
			os.system(variableValues[variableNames.index(line.split('"')[1])])
		else:
			os.system(line.split('"')[1])
	##### MATH #####
	elif line.split(" ")[0].upper() == "ADD":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		if line.split(" ")[2].isnumeric():
			b = float(line.split(" ")[2])
		else:
			b = float(variableValues[variableNames.index(line.split(" ")[2])])

		variableValues[0] = a + b
	
	elif line.split(" ")[0].upper() == "SUBTRACT":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		if line.split(" ")[2].isnumeric():
			b = float(line.split(" ")[2])
		else:
			b = float(variableValues[variableNames.index(line.split(" ")[2])])

		variableValues[0] = a - b

	elif line.split(" ")[0].upper() == "MULTIPLY":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		if line.split(" ")[2].isnumeric():
			b = float(line.split(" ")[2])
		else:
			b = float(variableValues[variableNames.index(line.split(" ")[2])])

		variableValues[0] = a * b
	
	elif line.split(" ")[0].upper() == "DIVIDE":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		if line.split(" ")[2].isnumeric():
			b = float(line.split(" ")[2])
		else:
			b = float(variableValues[variableNames.index(line.split(" ")[2])])

		variableValues[0] = a / b

	elif line.split(" ")[0].upper() == "MODULO":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		if line.split(" ")[2].isnumeric():
			b = float(line.split(" ")[2])
		else:
			b = float(variableValues[variableNames.index(line.split(" ")[2])])

		variableValues[0] = a % b

	elif line.split(" ")[0].upper() == "INT":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		variableValues[0] = int(a)
	
	elif line.split(" ")[0].upper() == "COMPARE":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		if line.split(" ")[2].isnumeric():
			b = float(line.split(" ")[2])
		else:
			b = float(variableValues[variableNames.index(line.split(" ")[2])])

		if a == b:
			variableValues[0] = "EQUAL"
		elif a > b:
			variableValues[0] = "LESS"
		elif a < b:
			variableValues[0] = "GREATER"
	elif line.split(" ")[0].upper() == "IS":
		if line.split(" ")[4] != "(STR)":
			if line.split(" ")[1].isnumeric():
				a = float(line.split(" ")[1])
			else:
				a = float(variableValues[variableNames.index(line.split(" ")[1])])
			
			if line.split(" ")[3].isnumeric():
				b = float(line.split(" ")[3])
			else:
				b = float(variableValues[variableNames.index(line.split(" ")[3])])
				
			if line.split(" ")[2].upper() == "EQUAL_TO":
				variableValues[0] = a == b
			if line.split(" ")[2].upper() == "LESS_THAN":
				variableValues[0] = a < b
			if line.split(" ")[2].upper() == "GREATER_THAN":
				variableValues[0] = a > b
		else:
			a = variableValues[variableNames.index(line.split(" ")[1])]
			b = variableValues[variableNames.index(line.split(" ")[3])]
			if line.split(" ")[2].upper() == "EQUAL_TO":
				variableValues[0] = a == b

	elif line.split("OF")[0].split(" ")[0].upper() == "GET_ITEM":
		value = int(line.split("OF")[0].split(" ")[1])
		seperator = line.split("OF")[1].split(" SPLIT_BY:")[1]
		variableValues[0] = variableValues[variableNames.index(line.split("OF")[1].split(" SPLIT_BY:")[0].split(" ")[1])].split(seperator)[value]
	
	elif line.split("AND")[0].split(" ")[0].upper() == "CONCAT":
		variableValues[0] = variableValues[variableNames.index(line.split("AND")[0].split(" ")[1])] + variableValues[variableNames.index(line.split("AND")[1].split(" ")[1])]
		
	elif line.split(" ")[0].upper() == "RANDOM":
		if line.split(" ")[1].isnumeric():
			a = float(line.split(" ")[1])
		else:
			a = float(variableValues[variableNames.index(line.split(" ")[1])])
		if line.split(" ")[2].isnumeric():
			b = float(line.split(" ")[2])
		else:
			b = float(variableValues[variableNames.index(line.split(" ")[2])])
		
		variableValues[0] = randint(a*100, b*100) / 100
	########################################
	elif line.split('"')[0].upper() == "INPUT":
		if line.split(':')[1].upper() == "(VAR)":
			variableValues[variableNames.index(line.split('"')[2].split(':')[0])] = input(variableValues[variableNames.index(line.split(" ")[1])])
		else:
			variableValues[variableNames.index(line.split('"')[2].split(':')[0])] = input(line.split('"')[1])

	elif line.split(" ")[0].upper() == "PRINT":
		if line.split(" ")[len(line.split(" ")) - 1] == "(STR)":
			print(line.split('"')[1])
		else:
			print(variableValues[variableNames.index(line.split(" ")[1])])

	elif line.upper() == "END PROGRAM":
		return i
	
	elif line.split(":")[0].upper() == "FUNCTION CALL":
		returnLine.value = i
		i = functionLocations[functionNames.index(line.split(":")[1].upper())] - 1

	elif line.split(":")[0].upper() == "FUNCTION CALL IF":
		if line.split(":")[1] == "T" or line.split(":")[1] == "TRUE":
			if variableValues[0]:
				returnLine.value = i
				i = functionLocations[functionNames.index(line.split(":")[2].upper())] - 1
		else:
			if not variableValues[0]:
				returnLine.value = i
				i = functionLocations[functionNames.index(line.split(":")[2].upper())] - 1

	elif line.split("@")[0].upper() == "PYTHON":
		i += 1
		while program[i] != "@":
			exec(program[i])
			i += 1
		return i
	elif line.upper() == "RETURN":
		i = returnLine.value
	elif line == "":
		pass
	else:
		print("SYNTAX ERROR: "+line)
	return i

while line != "}" or line.upper() == "END PROGRAM":
	line = program[i]
	if line != "}" or line.upper() == "END PROGRAM":
		i = parser(i)
		i += 1
	else:
		break
