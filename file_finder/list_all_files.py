import os
def list_all_files(folder_path):
    files_list = []
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            files_list.append(file)
    return files_list 