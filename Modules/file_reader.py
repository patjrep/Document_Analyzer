class FileReader:
    @staticmethod
    def read_file(file_path):
        with open(file_path, encoding='utf-8') as r_file:
            # return r_file.readlines()
            return r_file.read()
