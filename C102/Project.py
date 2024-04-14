import os
import shutil

form_dir = ""
to_dir = ""

list_of_files = os.listdir(form_dir)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    
    if ext == "":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf'] :
        path1 = form_dir + '/' + file_name
        path2 = to_dir + '/' + 'Document_Files'
        path3 = to_dir + '/' + 'Document_Files' + '/' + file_name
        
        if os.path.exists(path2):
            print('moving  ' + file_name + '  .......')
            shutil.move(path1,path3)
            
        else:
            os.makedirs(path2)
            print('moving  ' + file_name + '  .......')
            shutil.move(path1,path3)
        
