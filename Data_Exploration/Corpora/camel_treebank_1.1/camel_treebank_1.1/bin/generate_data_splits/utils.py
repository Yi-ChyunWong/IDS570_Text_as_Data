import os
from pathlib import Path
from typing import List
from .natural_sort import natural_keys

from .File import File

def get_file_names(data_path, endswith='conllx'):
    ret_files = []
    if not os.path.isdir(Path(data_path)):
        raise FileNotFoundError(f'Directory not found: {data_path}')
    for dirpath, _, files in os.walk(data_path):
        # print(f"Found directory: {dirpath}")
        
        if endswith:
            ret_files = [f_name for f_name in files if f_name.endswith(endswith)]
        # done within the os.walk for loop so 
        # it doesn't traverse subdirectories
        return ret_files

def read_files(dir_path: Path, file_name_list: List[str]=None) -> List[File]:
    if not file_name_list:
        file_name_list = get_file_names(dir_path)
    file_name_list.sort(key=natural_keys)
    file_list = []
    for file_name in file_name_list:
        temp_file = File(file_name=file_name, file_path=dir_path)
        temp_file.read_file()
        file_list.append(temp_file)
    return file_list
