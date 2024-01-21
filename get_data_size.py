
import os

def get_total_directory_size(directory):
	total_size = 0
	for root, dirs, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root, file)
			if os.path.isfile(file_path):
				total_size += os.path.getsize(file_path)
	return total_size

directory_path = './data'
total_size = get_total_directory_size(directory_path)
data_size = f'{total_size/1e6} MB'
# print(f"Total size of files in '{directory_path}': {total_size} bytes")

with open('data_size.txt','w') as fp:
	fp.write(data_size + '\n')

