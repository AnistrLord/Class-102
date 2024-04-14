import os
import shutil 

from_dir = "C:/Users/DELL/Pictures"
to_dir = "C:/Users/DELL/Music"

list_of_file = os.listdir(from_dir)

for file_name in list_of_file :
    name,extension = os.path.splitext(file_name)
    
    if extension == "":
        continue
    if extension in ['.gif','.png','.jpg','jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Image_Files'
        path3 = to_dir + '/' + 'Image_Files' + '/' + file_name
        
        if os.path.exists(path2):
            print('moving ' + file_name + ' .......')
            shutil.move(path1,path3)
            
        else:
            os.makedirs(path2)
            print('moving ' + file_name + ' .......')
            shutil.move(path1,path3)


        