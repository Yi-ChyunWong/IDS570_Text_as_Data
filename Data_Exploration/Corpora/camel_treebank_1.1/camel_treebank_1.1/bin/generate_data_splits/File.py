
from pathlib import Path

class File:
    def __init__(self, file_name='', file_path=None, file_data=None):
        if file_data is None:
            file_data = []
        if file_path is None:
            file_path = 'data'

        self.file_data = file_data
        self.file_path = file_path
        self.file_name = file_name

    def read_file(self):
        """
        Reads a file. Removes extra whitespaces, newlines, and carriage returns 
        from the end of lines.
        """
        data = []
        # sometimes a character that is not valid in utf8 is used, use this line
        # with open(Path(self.file_path) / self.file_name, encoding='latin-1') as file:
        with open(Path(self.file_path) / self.file_name, encoding='utf-8-sig') as file:
            data = file.readlines()

        data = [x.rstrip() for x in data]
        data = [x+'\n' for x in data if x != '\n']
        self.file_data = data

    def write_file(self, label='', file_name='', file_path='', ignore_hash=False):
        if file_name == '':
            file_name = self.file_name
        if label:
            file_name = f'{label}_{file_name}'

        if not file_path:
            file_path = self.file_path

        with open(Path(file_path) / file_name, 'w') as out_file:
            for dt in self.file_data:
                if ignore_hash and not dt.startswith('#') or not ignore_hash:
                    out_file.write(dt)
        return file_path, file_name

