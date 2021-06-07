import yake
import json


class WordCounter:
    def __init__(self, file_parser):
        self.word_count = []
        self.file_parser = file_parser
        self.keyword_weights = []
        self.keyword_variable = 0

    def word_counter_processor(self, sentence, document_name):
        individual_words = self.file_parser.split_to_words(sentence)
        # break_line = "<br/>"

        for word in individual_words:
            find_word = next(
                (x for x in self.word_count if x["Word"] == word.lower()), None)

            if find_word is not None:
                find_word["Frequency"] += 1
                find_word["Sentence"].append(sentence)

                if document_name not in find_word["Document"]:
                    find_word["Document"].append(document_name)

            else:
                if any(word in i for i in self.keyword_weights):

                    self.word_count.append({
                        "Word": word.lower(),
                        "Frequency": 1,
                        "Document": [document_name],
                        "Sentence": [sentence]
                    })

    def word_weighter(self, line):

        language = "en"
        # Greater value allows for more than one word (e.g. will group related words)
        max_ngram_size = 1
        # Lower number means less duplication when using larger n_grams
        deduplication_threshold = 0.1
        # Change for more or less keywords
        numOfKeywords = 1
        self.keyword_variable = numOfKeywords
        custom_kw_extractor = yake.KeywordExtractor(
            lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(line)

        for kw in keywords:
            self.keyword_weights.append(kw)
        return self.keyword_variable

    def get_word_count(self):
        return self.word_count
