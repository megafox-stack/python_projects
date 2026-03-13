
import os # operating system module
import shutil #file moving module

#folder_path = input("enter the folder path").strip().strip('"')

def organise_files(folder_path):
    # a dictonary to store different types of files along with extensions
    files_type = {"images":[".jpg",".jpeg",".png"],
                "Docs": [".pdf", ".txt", ".docx"],
                "Videos": [".mp4", ".mkv"]
    }
    
    #checking if the folder path exists
    if not os.path.exists(folder_path):
        print("ERROR: Folder path does not exist")
        exit()


    files = os.listdir(folder_path)  

    # loop through the files in the folder
    for file in files:
            print("found!",file)
            file_path = os.path.join(folder_path, file)

            if os.path.isdir(file_path):
                continue

            extension = os.path.splitext(file)[1].lower()
            print("extension:",extension)
            moved = False

        # match extension with the folder
            for folder_name, extensions in files_type.items():
                if extension in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)

                    destination = os.path.join(target_folder, file)

                    if os.path.exists(destination):
                        print(f"SKIPPED (already exists): {file}")
                    else:
                        shutil.move(file_path, destination)
                        print(f"MOVED: {file} → {folder_name}")

                    moved = True
                    break

            if not moved:
                print(f"NO CATEGORY: {file}")
        



       


