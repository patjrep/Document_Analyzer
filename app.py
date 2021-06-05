import Modules
import config


# class MainApp():
def processor():
    reader = Modules.FileDiscovery(config.DIRECTORIES)
    parsed_files = Modules.FileParser()
    files = Modules.FileReader()
    counted_words = Modules.WordCounter(parsed_files)
    interesting_words = Modules.InterestingWords(counted_words)

    for file in reader.get_files():
        print("Procesing:", file)
        for line in files.read_file(file):
            # print(line)
            for sentence in parsed_files.split_to_sentences(line):
                counted_words.word_counter_processor(sentence, file)
    # print(counted_words.get_word_count())
    print(interesting_words.getInterestingWords(counted_words))


def main():
    processor()


if __name__ == "__main__":
    main()
