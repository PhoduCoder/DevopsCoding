import os
path = "/Users/alieninvader/Desktop/Resumes"

entire_path = []
for dirpath,dirname,filename in os.walk(path):
    for file in filename:
        entire_path = os.path.join(dirpath,file)
    print(entire_path)

dir_path = []
for dirpath,dirname,filename in os.walk(path):
    for dir in dirname:
        dir_path.append(dir)
    print(dir_path)

file_path = []
for dirpath,dirname,filename in os.walk(path):
    for file in filename:
        file_path.append(file)
    print(file_path)
