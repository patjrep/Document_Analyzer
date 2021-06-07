import Modules
import config


def mainProcessor():
    reader = Modules.FileDiscovery(config.DIRECTORIES)
    files = Modules.FileReader()
    parsed_files = Modules.FileParser()
    lines = Modules.LineReader()
    counted_words = Modules.WordCounter(parsed_files)

    for file in reader.get_files():
        print("Procesing:", file)
        a = files.read_file(file)

        counted_words.word_weighter(a)

        for line in lines.read_line(file):

            # Processes split lines
            for sentence in parsed_files.split_to_sentences(line):
                counted_words.word_counter_processor(sentence, file)

    counted_words.get_word_count()
    mapped_interesting_words = counted_words.get_word_count()
    return mapped_interesting_words
