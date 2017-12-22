#!/usr/bin/env python3.6
#macass2 Fri Dec 15 11:30 PM
#stable Sat Dec 16 3:48 AM
#py3.6

from ma_head import *
from manager import run

def wrap_string(_str, underline=False, front="", back=""):
	return underlinecode if underline else "" + front + _str + back + endcode

def print_pure_data(width=200):
	loadJSON()
	pprint(data, width = width) #Look in pprint documentation

def print_the_data():
	loadJSON()
	print()
	for i in range(len(data)):
		print('  [{}]'.format(i+1), data[i])

def loadJSON():
	global data, data_values

	try:
		pure_data = json.load(open(data_file_path))
		data = list(pure_data.keys())
		data_values = list(pure_data.values())
		return True
	except Exception as error:
		print("Can't load data file.")
		print(str(error))
		exit(0) #temporary

def early_init():
	system('clear')

	print(main_open_message)

	return loadJSON()

def args_init(printArgs: bool = False):
	try:
		parser = argparse.ArgumentParser()
		parser.add_argument('commandnumber', type=int, nargs='*', help='Command numbers to quickly exceute.')
		args = parser.parse_args()
		if printArgs: print(args.commandnumber)
		return args.commandnumber
	except Exception as e:
		print("Error in args_init")
		print(e)

def safely_strint(_str):
	try: return int(_str)
	except Exception as e:
		print("Error in safely_strint")
		print(e)
		return False

def prompt(command_name, command):
	while True:
		print()
		print('', wrap_string("Command name:", front=Fore.YELLOW) , wrap_string(command_name, front=Fore.CYAN))
		print('', wrap_string("Command:", front=Fore.YELLOW), command)
		print('\n', wrap_string("Do you want to exceute the command? [y/n] [yes]: ", front=Fore.RED), end='')
		user_input = input()
		if user_input == 'no' or user_input == 'n':
			print()
			return False
		else:
			return True

def excer(index):
	user_strint = safely_strint(index)

	if user_strint - 1 in range(len(data)):
		if safely_strint (user_strint):
			command = data_values [user_strint - 1]
			command_name = data [user_strint - 1]
			
			if prompt(command_name, command):
				system(command)
				print()
	else:
		print(wrap_string("Enter a valid number from 1 to {}.".format(len(data)), front=Fore.RED))

def main():
	global data
	early_init()
	args = args_init(printArgs = False)
	if args:
		for i in args:
			strint = int(i)
			excer(strint)
		exit(0)

	print_the_data()
	print("\nFor commands enter 'cmds'.\n")

	while True:
		user_input = input(main_input_message)
		if not user_input: continue

		if user_input.lower() == "cmds":
			print_the_data()
			print()
			continue

		if user_input.lower() == "imanage":
			run(using_index=True, data=data)
			continue

		if user_input.lower() == "manage":
			run()
			continue

		if user_input in 'exit -e e quit -q q ty -ty thankyou'.split() + ['thank you']:
			raise KeyboardInterrupt #Smart move, Amr.

		excer (user_input)

try:
	main()
except KeyboardInterrupt:
	print(wrap_string("\nGoodbye, Amr.", front=Fore.YELLOW + Style.BRIGHT))
	exit(0)