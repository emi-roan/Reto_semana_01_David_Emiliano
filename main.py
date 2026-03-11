import sys

def process_line(line):
    valid_chars = "0123456789.-"
    cleaned = "".join(c for c in line if c in valid_chars)
    
    if not cleaned or cleaned == "." or cleaned == "-":
        return 0
    
    try:
        return int(float(cleaned))
    except ValueError:
        return 0

def main():
    total = 0
    for line in sys.stdin:
        total += process_line(line)
    print(total)

if __name__ == "__main__":
    main()