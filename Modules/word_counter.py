class WordCounter:
    def __init__(self, file_parser):
        self._word_count = []
        self._file_parser = file_parser

    def word_counter_processor(self, sentence, document_name):
        individual_words = self._file_parser.split_to_words(sentence)
        count = 0
        for word in individual_words:
            print(word)
            if word == "the":
                count += 1
                print('count', count)
        self._word_count.append(count)

    def get_word_count(self):
        return self._word_count
