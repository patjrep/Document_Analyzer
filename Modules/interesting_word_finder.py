# import nltk
# from nltk.corpus import stopwords


class InterestingWords:
    def __init__(self, word_counter):
        self.word_counter = word_counter
        self.interesting_words = []

    def getInterestingWords(self, word_counter):
        word_dictionary_counts = self.word_counter.get_word_count()
        # print(word_dictionary_counts)
        max_freq = sorted(word_dictionary_counts,
                          key=lambda item: item['Frequency'], reverse=True)
        print(max_freq[0], max_freq[1], max_freq[2])
        # for i in range(len(word_dictionary_counts)):

        #     print(word_dictionary_counts[i])

        self.interesting_words.append(word_dictionary_counts)
        # return self.interesting_words

    def mostInterestingWords(self):
        return self.interesting_words
