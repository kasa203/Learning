#sys.argv - list of command line arguments for the python script

import sys

if len(sys.argv) != 3:
    print('Usage:')
    print(f'{sys.argv[0]} <your_req_string> <lower|upper|title>')
    sys.exit()

user_input_string = sys.argv[1] #input('Please enter your string:\n')
user_input_string_type = sys.argv[2] #input('Please enter your string type - lower/upper/title:\n')

if user_input_string_type == 'lower':
    print(user_input_string.lower())

elif user_input_string_type == 'upper':
    print(user_input_string.upper())

elif user_input_string_type == 'title':
    print(user_input_string.title())

else:
    print(f"Your {user_input_string_type} is invalid!")