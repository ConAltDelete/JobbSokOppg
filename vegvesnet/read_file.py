# Assumtions: file get supplied in commandline, otherwise spesify file_path with promt

import sys,re

def read_print(file: str, pattern: str = r"^\s*ORA-.*") -> None:
    """
        Reads file and prints lines following pattern. Default pattern is '^\\s*ORA-.*', which is any line stating with "ORA-" with or without trailing whitespace.

        Args:
            file str: name of the file.
            pattern str: pattern to be applied onto the line in RegEx format
        
        Returns:
            None
    """
    reg_pattern = re.compile(pattern=pattern)
    for line in open(file, mode = "r"):
        if reg_pattern.match(line):
            print(line[:-1]) # [:-1] to remove the newline character


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input("Give file to read:\n")
    
    read_print(file_name) # uses the default pattern as per task
