# Lines of code counter
**Counts the line of code for a file, or for each file in a directory**
## Usage
Enter the directory/file (absolute or relative) path as a command-line argument:

    python3 main.py [PATH]

**Output**

    [SEARCH-OUTPUT]
    The total amount of lines counted in the directory [DIRECTORY-PATH] is: [LINES]
## Ignore List
This program also supports a list of files to ignore, in regex format. To add a file to the ignore list, append a regex pattern on a new line to an `ignore.txt` file in the directory where the program is executed. Leading and trailing whitespace, blank lines, and lines starting with `#` are ignored. If an ignore file is not present, the program will default to the ignore list `"venv/", "venv/", ".git/", ".idea/", "__pycache__/", "node_modules/", "build/", "dist/"`.
## Allowed file extensions
Upon finding a file, the program will check if the file ends with a set of allowed extensions. To specify the allowed extensions, append the allowed extensions (one per line, extensions such as `min.js` are allowed), excluding the leading period, to a `extensions.txt` file in the directory where the program is executed. If an allowed extensions file is not present, the program will default to the list `"py", "cpp", "cs", "c", "rb", "r", "f", "h", "fs", "java", "ts", "tsx", "js", "html", "css", "less", "scss", "sass", "php", "asp", "aspx", "sh", "zsh", "fish", "bash", "bat", "ps1", "xsh", "csh", "tcsh", "ksh", "jl", "lua"`.
