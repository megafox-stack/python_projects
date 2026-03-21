import os

extensions = ['.py', '.js', '.java', '.cpp', '.c']

def scan_files(path):
    code_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    full_path = os.path.join(root, file)
                    code_files.append(full_path)
                    break

    return code_files




    
