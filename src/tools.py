import sys

def readFile(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return (data)
    except OSError as e:
        print(e)
        sys.exit(1)