from ma_head import data_file_path, json

def append(pairs:dict):
	with open (data_file_path, 'r+') as file:
		pure_data = json.load(file)

		for key, v in pairs.items():
			if v in [None, '']:
				if key in pure_data:
					pure_data.pop(key)
			else:
				pure_data [key] = v

		file.seek(0)

		json.dump(pure_data, file, indent=4)

		file.truncate()

def run(data = None, using_index=False):
	current_data = dict()

	while True:
		user_input = input("Key Value (blank to stop):")
		if not user_input: break

		user_input = user_input.split()
		if using_index:
			user_input[0] = str(data[ int(user_input[0])-1 ])

		current_data.update({user_input[0] : user_input[1] if len(user_input) > 1 else None})

	append(current_data)