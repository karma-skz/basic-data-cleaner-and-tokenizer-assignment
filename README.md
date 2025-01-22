The text provided to me is an extract from the Bible.
1) for data cleaning, I have implemented the following-
    1) convert all text to lower case-
        This might not be a good choice as a structured text like this might give information about named identities through capitalisation, but has been implemented nevertheless.
    2) removed extra white spaces.
    3) removed extra characters that might've occured due to incorrect data access while copying or so.
    4) expanded common contractions. Couldn't do it for all of the contractions present in the text as the english is really old and there are a lot of words I can't practically check them all manually as I am not familiar with them.
    5) Removed all HTML tags.
    6) Replaced mail ids with ```<MAIL>```, urls with ```<URL>```, hashtags with `<HASHTAG>`, mentions with ```<MENTION>```, although there were no instances in my text where this would actually be needed.
    7) Changed all quotations to " "
    8) Normalised ellipses.
    9) Combined them all into 1 pipeline function called "clean_text". This can be imported and called into any other files. (Called it for cleaning data before tokenization)

2) for tokenization, I implemented the following-
    1) Identified abbreviations like Dr. Mr. Mrs. Prof.
    2) Identified hyphenated words.
    3) Did not split numbers separated by colon(:) as they represent chapters and verses in the context of the given dataset.
    4) Did not need to work with currency, mails, mentions etc wrt given dataset.
    5) You can also call just the print_sentences function (which i have commented out in 'basic tokenizer.py') and comment out the print_words function call to split the text into different sentences only. 
    6) What I have done is break the text into sentences and break each sentence into words giving each sentence and word a unique i and j index with it.
    
