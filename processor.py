import Modules
import config


def mainProcessor():
    reader = Modules.FileDiscovery(config.DIRECTORIES)
    parsed_files = Modules.FileParser()
    files = Modules.FileReader()
    lines = Modules.LineReader()
    counted_words = Modules.WordCounter(parsed_files)
    interesting_words = Modules.InterestingWords(counted_words)

    for file in reader.get_files():
        print("Procesing:", file)
        a = files.read_file(file)
        # if file == "test_docs/doc1.txt":
        #     print(a)
        counted_words.word_weighter(a)

        for line in lines.read_line(file):

            # Processes split lines
            for sentence in parsed_files.split_to_sentences(line):
                counted_words.word_counter_processor(sentence, file)

    # interesting_words.getInterestingWords(counted_words)
    # mapped_interesting_words = interesting_words.mostInterestingWords()

    counted_words.get_word_count()
    mapped_interesting_words = counted_words.get_word_count()
    return mapped_interesting_words
