"""Generate data splits and save them data/data_splits.
"""
from dataclasses import dataclass
import pathlib
from typing import List

import pandas as pd
from File import File
from natural_sort import natural_keys
from selection import get_choices
from utils import get_file_names, read_files

@dataclass
class FileType:
    path: pathlib.Path
    extension: str
@dataclass
class Splits:
    split_types: List[str]
    file_name_splits: dict # dictionary keys are split_types

def tsv_to_splits(df):
    split_types = df['split_type'].unique().tolist()
    splits = {split_type: df[df['split_type'] == split_type]['file_name'].tolist() for split_type in split_types}

    return Splits(split_types, splits)

def get_files_of_type(selected_files, file_names, extension):
    return [file_name for file_name in file_names if file_name.replace(extension,'') in selected_files]

def split_data(file_name_list, extension, splits): 
    data = {}
    for split_type in splits.split_types:
        # sort using natural keys
        temp_file_names = get_files_of_type(splits.file_name_splits[split_type], file_name_list, extension)
        temp_file_names.sort(key=natural_keys)
        data[split_type] = temp_file_names
    return data

def get_splits_data(dir_path, new_splits):
    data = {}
    for k, v in new_splits.items():
        conllx_files = read_files(dir_path, v)
        new_file_data = [sentence for conllx in conllx_files for sentence in conllx.file_data]
        data[k] = new_file_data
    return data

def get_data(file_type, subcorpus, splits):
    # import pdb; pdb.set_trace()
    dir_path = file_type.path / subcorpus
    # read files (default extension: conllx)
    file_name_list = get_file_names(dir_path, file_type.extension)
    # pdb.set_trace()
    # get new file name lists based on file name split lists
    new_splits = split_data(file_name_list, file_type.extension, splits)
    
    return get_splits_data(dir_path, new_splits)

def save_splits(data, subcorpus_out_path, subcorpus_name, extension):
    # import pdb; pdb.set_trace()
    for k, v in data.items():
        temp_file = File(file_name=f'{subcorpus_name}_{k}{extension}', file_path=subcorpus_out_path, file_data=v)
        temp_file.write_file()

def read_and_save_data(choices, save_each, save_all, file_types: FileType):
    # iterate over annotated, sent, and raw
    for file_type in file_types:
        # to store all data (if full corpus was chosen)
        subcorpora_data = { 'dev': [], 'train': [], 'test': []}
        out_path = pathlib.Path(OUT_PATH)
        
        for subcorpus in choices:
            # read the tsv file of each selected subcorpus
            tsv_file = pd.read_csv(TSV_PATH/f'{subcorpus}.tsv', sep='\t')
            # convert tsv file into lists by split type (dev/train/test)
            splits = tsv_to_splits(tsv_file)
        
            # get a dictionary of data ready to be saved
            data = get_data(file_type, subcorpus, splits)
            
            subcorpora_data['dev'] += data['dev']
            subcorpora_data['train'] += data['train']
            subcorpora_data['test'] += data['test']
            # import pdb; pdb.set_trace()
            # if data_splits directory doesn't exist, create it
            out_path.mkdir(exist_ok=True)
            # create data_splits/[file_type] directory
            file_type_out_path = out_path/file_type.path.name
            file_type_out_path.mkdir(exist_ok=True)
            if save_each:
                subcorpus_out_path = file_type_out_path/subcorpus
                subcorpus_out_path.mkdir(exist_ok=True)
                # import pdb; pdb.set_trace()
                save_splits(data, subcorpus_out_path, subcorpus, file_type.extension)
        if save_all:
            subcorpus_out_path = file_type_out_path/'camel_treebank'
            subcorpus_out_path.mkdir(exist_ok=True)
            save_splits(subcorpora_data, subcorpus_out_path, 'camel_treebank', file_type.extension)
        # print(f'Data saved in {file_type.path}')
        
OUT_PATH = '../../data/data_splits'
ANNOT_PATH = pathlib.Path('../../data/annotated')
SENT_PATH = pathlib.Path('../../data/sent')
RAW_PATH = pathlib.Path('../../data/raw')
TSV_PATH = pathlib.Path('../../data/splits/')
    
SCRIPT_DESCRIPTION = 'Generate dev/train/test splits'
if __name__ == "__main__":
    
    subcorpora = ['1001', 'ALC', 'BTEC', 'Hadith', 'Hayy', 'NT', 'OT', 'Odes', 'QALB', 'Quran', 'Sara', 'WikiNews', 'ZAEBUC']
    extra_options = ['Full subcorpora (in splits)', 'All of the above (each subcorpus + full subcorpora)!']
    file_types = [FileType(ANNOT_PATH, '.conllx'),
        FileType(SENT_PATH, '.sent'),
        FileType(RAW_PATH, '.raw')]

    choices, save_each, save_all = get_choices(subcorpora, extra_options)
    
    read_and_save_data(choices, save_each, save_all, file_types)
    print(f'Split data saved in data/data_splits')