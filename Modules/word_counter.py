# import nltk
# from nltk.corpus import stopwords
# # nltk.download('stopwords')


class WordCounter:
    def __init__(self, file_parser):
        self.word_count = []
        self.file_parser = file_parser

    def word_counter_processor(self, sentence, document_name):
        individual_words = self.file_parser.split_to_words(sentence)
        # stopWords = set(stopwords.words('english'))
        # print(stopWords)

        for word in individual_words:
            find_word = next(
                (x for x in self.word_count if x["Word"] == word.lower()), None)

            if find_word is not None:
                find_word["Frequency"] += 1
                if document_name not in find_word["Document"]:
                    find_word["Document"].append(document_name)

            else:
                self.word_count.append({
                    "Word": word.lower(),
                    "Frequency": 1,
                    "Document": [document_name],
                    "Sentence": sentence
                })

    def get_word_count(self):
        return self.word_count
