# -*- coding: utf-8 -*-
from os import path, listdir
from re import findall
from sys import argv

import typing

file_extensions: typing.List[str]

try:
	file_extensions = []
	for i in open("extensions.txt", "r").read().splitlines():
		if i.strip():
			file_extensions.append(i.strip())
except FileNotFoundError:
	file_extensions = ["py", "cpp", "cs", "c", "rb", "r", "f", "h", "fs", "java", "ts", "tsx", "js", "html", "css", "less", "scss", "sass", "php", "asp", "aspx", "sh", "zsh", "fish", "bash", "bat",
	                   "ps1", "xsh", "csh", "tcsh", "ksh", "jl", "lua"]

if len(argv) == 1:
	exit("No command-line arguments provided. For more information, refer to the 'Features' section in the README.md file.")
if not path.exists(path.abspath(argv[1])):
	exit("Invalid path")

try:
	ignore = []
	for i in open("ignore.txt", "r").read().splitlines():
		if i.strip() and not i.lstrip().startswith("#"):
			ignore.append(i.strip())
except FileNotFoundError:
	ignore = ["venv/", "venv/", ".git/", ".idea/", "__pycache__/", "node_modules/", "build/", "dist/"]


def pathValid(_path: str, extensions: bool = True) -> bool:
	return (not extensions or ".".join(_path.split(".")[1:]) in file_extensions) and not any((lambda: [findall(exp, _path) for exp in ignore])())


def countLines(_path: str, tab: typing.Union[str, bool] = "\t") -> int:
	if path.isfile(_path) and pathValid(_path):
		try:
			count = len(open(_path, "r").read().splitlines()) + 1
			print(f"{tab if tab else ''}The file {_path} has {count} lines.")
			return count
		except Exception as _exception:
			print(f"\033[91m\tThe file {_path} raised exception: {_exception}.\033[0m")
			return 0
	return 0


if path.isfile(path.abspath(argv[1])):
	exit(countLines(path.abspath(argv[1]), False) * 0)


def getDirectoryItems(_path: str) -> int:
	if not pathValid(_path, False):
		return 0
	print(f"Searching directory: {path.abspath(_path)}")
	total = 0
	try:
		for x in listdir(path.abspath(_path)):
			if path.isfile(path.abspath(f"{path.abspath(_path)}/{x}")):
				total += countLines(_path + "/" + x)
			else:
				total += getDirectoryItems(f"{_path}/{x}")
	except Exception as _exception:
		print(f"\033[91mException: {_exception}\033[0m")
	return total


print(f"\n\033[96mThe total amount of lines counted in the directory {path.abspath(argv[1])} is: {getDirectoryItems(path.abspath(argv[1]))}\033[0m")
