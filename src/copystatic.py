
import os
import shutil

def copy_files(path_from, path_to):
    
    if not os.path.exists(path_from):
        raise Exception(f"Directory {path_from} does not exist")
    
    if os.path.isfile(path_from):
        shutil.copy(path_from,path_to)
        return
    
    if not os.path.exists(path_to):
        os.mkdir(path_to)
    
    
    dir_list = os.listdir(path_from)
    # print(dir_list)
    for object in dir_list:
        source = os.path.join(path_from, object)
        destination = os.path.join(path_to, object)
        # print(source)
        # print(destination)
        copy_files(source, destination)
    
        
    
    
    