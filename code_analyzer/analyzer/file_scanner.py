import os
from utils.helpers import is_supported_file 

extensions = ['.py', '.js', '.java', '.cpp', '.c']

def scan_files(path):
    code_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if is_supported_file(file, extensions):
                full_path = os.path.join(root, file)
                code_files.append(full_path)

    return code_files




    
