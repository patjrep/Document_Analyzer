## How It Works

To run the program, navigate to the main folder and run:
```bash
python app.py
```


As defined in config.py, the program loops through the specified directory in the file and will read all the files included in the folder.

Once read, 'file_parser.py' parses the files, breaking it down into two usable forms; individual sentences and individual words.

You'll also notice that there are two types of reader Modules, one which reads the indiivdual lines, and one that reads the entire document. This distinction in necessary for the way the program handles the files.

The 'word_counter.py' module has two different methods inside:
    1) word_weighter() takes the entire read file from 'file_reader.py' and uses a NLP library called YAKE to process the text corpus. This then weights the words and provides a keyword ranking to each (the lower the value the more "important" the word is).
    There values are changeable withing the method including the abiilty to chosse the amount of keywords, duplication allowance threshold, etc.

    2) word_counter_processor() takes the read lines from the 'line_reader.py' Module. It then searches to see if the word is contained as one of the identified keywords found in the word_weighter() method. If so, it will then add it in JSON format self.word_count list.