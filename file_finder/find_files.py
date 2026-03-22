import os 
def find_files(folder_path, keyword):
    matches = []
    total_files = 0
    largest_file = None
    largest_size = 0  
    
    extension = keyword.lower()
    if not extension.startswith("."):
        extension = "."+ extension 

    for root,dirs,files in os.walk(folder_path):
        for file in files:
            total_files += 1
            full_path = os.path.join(root, file)

            try:                      
                size = os.path.getsize(full_path)
            except OSError:
                continue

            if size > largest_size:    
                largest_size = size
                largest_file = full_path

            if file.lower().endswith(extension): 
                matches.append(full_path)

    return matches, total_files, largest_file, largest_size