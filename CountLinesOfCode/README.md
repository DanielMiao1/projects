# Lines of code counter
**Counts the line of code for a file, or for each file in a directory**
## Run
Run the `main.py` python script (`python3 main.py`)
## Features
### For a file
Enter the file name (absolute or relative path) as a command-line argument after the file call.

`python3 main.py [FILE-PATH]`

Output

`The file [FILE-PATH] has [LINES] lines.`
### For a directory
Enter the directory (absolute or relative path) as a command-line argument after the file call.

`python3 main.py [DIRECTORY-PATH]`

Output

    [SEARCH-OUTPUT]
    The total amount of lines counted in the directory [DIRECTORY-PATH] is: [LINES]
## Ignore
To ignore a directory (and files within the directory), enter the name of the directory in the `ignore` file.
If a `ignore` file is not present in the current directory, the program will default to the ignore list `".git", "venv", "node_modules", ".idea"`
## File extensions
All files extensions the program searches for lines are in the `include` file.
If a `include` file is not present in the current directory, the program will default to the include list `"py", "cpp", "cs", "c", "rb", "r", "f", "h", "fs", "java", "ts", "tsx", "js", "html", "css", "less", "scss", "php", "asp", "aspx", "sh", "json"`.
