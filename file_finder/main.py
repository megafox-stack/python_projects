from file_finder.find_files import find_files
from file_finder.list_all_files import list_all_files
from file_finder.format_size import format_size  

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
        print(f"{f}:{format_size(size)}", end=",")   

    print(f"\ntotal no of files: {scanned}")
    print(f"matches found: {len(results)}")

    if big_file:
        print(f"Largest file: {big_file}")
        print(f"Size: {format_size(size)}")   
    
   

  

 


