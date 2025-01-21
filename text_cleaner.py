#!/bin/python3
import re

#1(a) emove extra white spaces
def remove_extra_whitespace(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+(?=[.,,"\'!?;:])', '', text)
    return text.strip()

#1(b) convert to lower case
def to_lowercase(text):
    return text.lower()

#1(c) remove special characters while preserving punctuation
def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9.,<>!?\'";: ]+', '', text)

#1(d)handle common abbreviations
def handle_common_abbreviations(text):
    contractions_patterns = [
        (r"can't", "cannot"),
        (r"shan't", "shall not"),
        (r"won't", "will not"),
        (r"n't", " not"),
        (r"'m", " am"),
        (r"'re", " are"),
        (r"'d", " would"),
        (r"'ll", " will"),
        (r"'ve", " have"),
        (r"he's", "he is"),
        (r"she's", "she is"),
        (r"it's", "it is"),
        (r"that's", "that is"),
        (r"what's", "what is"),
        (r"there's", "there is"),
        (r"here's", "here is"),
        (r"where's", "where is"),
        (r"when's", "when is"),
        (r"why's", "why is"),
        (r"who's", "who is"),
        (r"how's", "how is"),
        (r"let's", "let us"),
    ]
    for pattern, replacement in contractions_patterns:
        text = re.sub(pattern, replacement, text)
    return text

#2(a) remove html tags
def remove_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)

#2(b) tokens replaced with placeholders before removing special characters and after the html tags have been removed.
def replace_tokens_with_placeholders(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
    text = re.sub(email_pattern, '<MAIL>', text)
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    text = re.sub(url_pattern, '<URL>', text)
    hashtag_pattern = re.compile(r'#[a-zA-Z0-9_+&!]+')
    text = re.sub(hashtag_pattern, '<HASHTAG>', text)
    mention_pattern = re.compile(r'@[a-zA-Z0-9_+&!]+')
    text = re.sub(mention_pattern, '<MENTION>', text)
    return text

#2(c) standardize quotation marks
def standardize_quotation_marks(text):
    text=re.sub(r"(?<!\w)`+|`+(?!\w)", '"', text)
    text=re.sub(r"(?<!\w)'+|'+(?!\w)", '"', text)
    text=re.sub(r'''(?<!\w)"+|"+(?!\w)''', '"', text)
    return text

#2(d) normalise ellipses
def normalise_ellipses(text):
    ellipses=re.compile(r'\.{2,}')
    text=re.sub(ellipses, "...", text)
    return text



#pipeline
def clean_text(text):
    text=to_lowercase(text)
    text=remove_extra_whitespace(text)
    text=remove_html_tags(text)
    text=replace_tokens_with_placeholders(text)
    text=standardize_quotation_marks(text)
    text=remove_extra_whitespace(text)
    text=normalise_ellipses(text)
    text=remove_special_characters(text)
    text=handle_common_abbreviations(text)
    return text
#----------------------------------main----------------------------------
f = open("12_text.txt", "r")
text = f.read()
f.close()

cleaned=clean_text(text)

f=open("cleaned_text.txt", "w")
f.write(cleaned)
