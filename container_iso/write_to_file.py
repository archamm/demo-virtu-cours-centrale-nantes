import os
import sys

def write_to_file(filename):
    content = f"Hello from {os.environ.get('CONTAINER_NAME', 'Unknown Container')}\n"
    with open(filename, "a") as file:
        file.write(content)
    print(f"Content written to {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python write_to_file.py <filename>")
    else:
        write_to_file(sys.argv[1])
