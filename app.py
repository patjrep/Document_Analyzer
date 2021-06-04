import Modules
import config


# class MainApp():
def processor():
    reader = Modules.FileDiscovery(config.DIRECTORIES)
    parsed_files = Modules.FileParser()
    files = Modules.FileReader()
    counted_words = Modules.WordCounter(parsed_files)
    print(parsed_files)
    for file in reader.get_files():
        # print(file)
        for line in files.read_file(file):
            # print(line)
            for sentence in parsed_files.split_to_sentences(line):
                counted_words.word_counter_processor(sentence, file)
    print(counted_words.get_word_count())


def main():
    processor()


if __name__ == "__main__":
    main()
