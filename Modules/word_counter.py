class WordCounter:
    def __init__(self, file_parser):
        self.word_count = {}
        self.file_parser = file_parser

    def word_counter_processor(self, sentence, document_name):
        individual_words = self.file_parser.split_to_words(sentence)

        for word in individual_words:
            print(word)
            if word not in self.word_count:
                self.word_count[word] = 0
            self.word_count[word] += 1

    def get_word_count(self):
        return self.word_count
