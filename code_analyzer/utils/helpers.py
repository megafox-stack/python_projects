import os

def get_extension(file_path):
    return os.path.splitext(file_path)[1].lower()

def is_supported_file(file_path,extensions):
    return get_extension(file_path) in extensions

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []
    
def clean_line(line):
    return line.strip()

def count_lines(lines):
    count = 0
    for line in lines:
        if clean_line(line):
            count += 1
    return count

def get_filename(file_path):
    return os.path.basename(file_path)

