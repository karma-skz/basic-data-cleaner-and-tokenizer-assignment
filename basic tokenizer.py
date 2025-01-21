from text_cleaner import clean_text
import re

#1 divide into sentences
def break_into_sentences(text):
    sentences=re.split(r'(?<=[.!?])(?<!\b(?:mr|dr|ms)\.)(?<!\b(?:mrs)\.)(?<!\b(?:prof)\.)\s', text)
    return sentences

def print_sentences(f, text):
    sentences=break_into_sentences(text)
    f.write("[")
    for i, sentence in enumerate(sentences, 1):
        f.write(f"{i}: '{sentence}',\n ")
    f.write("]")
    return

#2 divide into words
def break_into_words(text):
    regex=re.compile(r"\b\w+(?:[:]\w+)?|[^\w\s]")
    words=re.findall(regex, text)
    return words

def print_words(f, text):
    sentences=break_into_sentences(text)
    f.write("[")
    for i, sentence in enumerate(sentences, 1):
        words=break_into_words(sentence)
        for j, word in enumerate(words, 1):
            f.write(f"[{i}-{j}: '{word}'],\n ")
        f.write("\n")
    f.write("]")
    return
f=open('12_text.txt', 'r')
text=f.read()
f.close()
text=clean_text(text)

f=open("tokenized.txt", 'w')
#print_sentences(f, text)
print_words(f, text)
f.close()
