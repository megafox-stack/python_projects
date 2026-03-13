import os
#creation of the test folder
base_path = r"C:\Family\Archit\Projects\test for programs"
new_folder = "test_folder"
full_path = os.path.join(base_path,new_folder)
os.makedirs(full_path,exist_ok = True)
print("folder created successfully")
test_folder = r"C:\Family\Archit\Projects\test for programs\test_folder"
os.makedirs(test_folder,exist_ok=True)


# creation of dummy files
dummy_files = [
    "a.jpg",
    "b.pdf",
    "c.txt",
    "d.mp4",
    "e.jpeg"
]
for file in dummy_files:
      path = os.path.join(test_folder,file)
      with open(path,"w") as f:
            f.write("dummy content")
print("dummy files created!")

      
