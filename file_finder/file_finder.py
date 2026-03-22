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

def list_all_files(folder_path):
    files_list = []
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            files_list.append(file)
    return files_list 

def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f}KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f}MB"       




if __name__ == "__main__":
    folder = input("enter the folder name:").strip('"')
    word = input("enter the file extension:")

    total = list_all_files(folder)
    results, scanned, big_file, size = find_files(folder, word)
    
    if results:
        print("Matching files:")
        for f in results:
            print(f)
    else:
        print("no file found") 
    
    print()
    for f in total:
        print(f"{f}:{format_size(size)}",end = ",")

    print(f"\ntotal no of files: {scanned}")
    print(f"matches found: {len(results)}")

    if big_file:
        print(f"Largest file: {big_file}")
        print(f"Size: {format_size(size)}")
    
   

  

 


