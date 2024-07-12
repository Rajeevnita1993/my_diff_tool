import sys
from my_diff import generate_diff

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def main():
    if len(sys.argv) != 3:
        print("Usage: ccdiff <original_file> <new_file>")
        sys.exit(1)

    original_file = sys.argv[1]
    new_file = sys.argv[2]

    original_lines = read_file(original_file)
    new_lines = read_file(new_file)

    diff = generate_diff(original_lines, new_lines)

    for line in diff:
        print(line)

if __name__ == "__main__":
    main()