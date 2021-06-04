class FileReader:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as r_file:
            return r_file.readlines()
