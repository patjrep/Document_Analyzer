class LineReader:
    @staticmethod
    def read_line(file_path):
        with open(file_path, encoding='utf-8') as r_lines:
            return r_lines.readlines()
