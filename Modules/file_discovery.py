import os
# import config.py


class FileDiscovery:
    def __init__(self, files):
        self.files = files

    # Gets file directory and file name then adds to file list

    def get_files(self):
        files = []
        for current_file in self.files:
            for document in os.listdir(current_file):
                files.append(current_file + document)
        return files
