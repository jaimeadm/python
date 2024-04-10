from pathlib import Path

FILE = Path(__file__).parent / 'arquivo2123.txt'

try:
    file = open(FILE, "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
