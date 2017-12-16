import sys
from os import path, system
from colorama import init, Fore, Back, Style
from pprint import pprint #print json keeping its format
import json, argparse

init(autoreset=True) #colorama init

global data_file_path
global data, data_values

underlinecode = '\033[4m'
endcode = '\033[0m'

b_for_yellow = Fore.YELLOW + Style.BRIGHT

main_input_message = underlinecode + ('macass:') + endcode
main_error_message = Fore.RED + 'Please choose a valid number.' + Fore.RESET
main_open_message = b_for_yellow + 'macass2' + Fore.WHITE + ' – Refreshed by amressam for 2018 –'

data_file_path = path.dirname(path.realpath(__file__)) + '/data'
