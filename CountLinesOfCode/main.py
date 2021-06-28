from os import path, listdir
from sys import argv

file_extensions: list = ["py", "cpp", "cs", "c", "rb", "r", "f", "h", "fs", "java", "ts", "tsx", "js", "html", "css", "less", "scss", "php", "asp", "aspx", "sh"]

if len(argv) == 1: exit("No command-line arguments provided. For more information, refer to the 'Features' section in the README.md file.")
if not path.exists(path.abspath(argv[1])): exit("Invalid path")
if path.isfile(path.abspath(argv[1])):
	print(f"\033[96mThe file {path.abspath(argv[1])} has {len(open(path.abspath(argv[1]), 'r').read().splitlines()) + 1} lines.\033[0m")
	exit()

total_lines: int = 0

def getDirectoryItems(_path: str) -> None:
	print(f"Searching directory: {path.abspath(_path)}")
	try:
		for x in listdir(path.abspath(_path)):
			if path.isfile(path.abspath(f"{path.abspath(_path)}/{x}")):
				if len(x) < 4:
					try:
						print(f"\tThe file {f'{path.abspath(_path)}/{x}'} has {len(open(f'{path.abspath(_path)}/{x}', 'r').read().splitlines()) + 1} lines.")
						globals()["total_lines"] += (len(open(f'{path.abspath(_path)}/{x}', 'r').read().splitlines()) + 1)
					except Exception as _exception: print(f"\033[91m\tThe file {f'{path.abspath(_path)}/{x}'} raised exception: {_exception}.\033[0m")
				elif x.split(".")[-1] in file_extensions:
					try:
						print(f"\tThe file {f'{path.abspath(_path)}/{x}'} has {len(open(f'{path.abspath(_path)}/{x}', 'r').read().splitlines()) + 1} lines.")
						globals()["total_lines"] += (len(open(f'{path.abspath(_path)}/{x}', 'r').read().splitlines()) + 1)
					except Exception as _exception: print(f"\033[91m\tThe file {f'{path.abspath(_path)}/{x}'} raised exception: {_exception}.\033[0m")
			else: getDirectoryItems(f"{_path}/{x}")
	except Exception as _exception: print(f"\033[91mException: {_exception}\033[0m")


print(f"Searching directory: {path.abspath(argv[1])}")
try:
	for i in listdir(path.abspath(argv[1])):
		if path.isfile(path.abspath(f"{path.abspath(argv[1])}/{i}")):
			if len(i) < 4:
				try:
					print(f"\tThe file {f'{path.abspath(argv[1])}/{i}'} has {len(open(f'{path.abspath(argv[1])}/{i}', 'r').read().splitlines()) + 1} lines.")
					total_lines += len(open(f'{path.abspath(argv[1])}/{i}', 'r').read().splitlines()) + 1
				except Exception as exception: print(f"\033[91m\tThe file {f'{path.abspath(argv[1])}/{i}'} raised exception: {exception}.\033[0m")
			elif i.split(".")[-1] in file_extensions:
				try:
					print(f"\tThe file {f'{path.abspath(argv[1])}/{i}'} has {len(open(f'{path.abspath(argv[1])}/{i}', 'r').read().splitlines()) + 1} lines.")
					total_lines += len(open(f'{path.abspath(argv[1])}/{i}', 'r').read().splitlines()) + 1
				except Exception as exception: print(f"\033[91m\tThe file {f'{path.abspath(argv[1])}/{i}'} raised exception: {exception}.\033[0m")
		else: getDirectoryItems(f"{argv[1]}/{i}")
except Exception as exception: print(f"\033[91mException: {exception}\033[0m")

print(f"\n\033[96mThe total amount of lines counted in the directory {path.abspath(argv[1])} is: {total_lines}\033[0m")
