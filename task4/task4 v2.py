import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fileTextName')
    parser.add_argument('fileVocabularyName')
    #parser.add_argument('outputFile')
    args = parser.parse_args()
    text = open_file(args.fileTextName)
    #text = open_file("text.txt")
    #vocabulary = open_file("vocabulary.txt")
    vocabulary = open_file(args.fileVocabularyName)
    #inputInf = open_file(args.fileTextName)
    #text = inputInf[0]
    #vocabulary = inputInf[1]
    #text = find_mistakes(text, vocabulary)
    
    print_result(text)


def find_words(string, simbols):
    result = ""
    for char in string:
        if char in simbols:
            result += char
    return result


def char_range(start, end, simbols, step=1):
    for char in range(ord(start), ord(end), step):
        simbols.append(chr(char))


def removing_of_regular_expressions(string):
    simbols = []
    char_range('a', 'z', simbols)
    char_range('A', 'Z', simbols)
    char_range('А', 'Я', simbols)
    char_range('а', 'я', simbols)
    simbols.append(" ")
	
    text = find_words(string, simbols)
    text = text.split(" ")
    return text


def open_file(filename):
    file = ""
    with open(filename) as inf:
        for string in inf:
            file += string
        #temp = file.split("{")
        #text = removing_of_regular_expressions(temp[0])
        #vocabulary = removing_of_regular_expressions(temp[1])
    return file


def print_result(text):
    for i in range(len(text)):
        print(text[i], end=' ')


def find_mistakes(text, vocabulary):
    #mistakes = {} #key is incorrect word, value is correct word
    count = 0
    for i in range(len(text)):
        for j in range(len(vocabulary)):
            if len(vocabulary[j]) > len(text[i]):
                continue
            for k in range(len(vocabulary[j])):
                if (vocabulary[j][k] != text[i][k]) and (vocabulary[j][k].upper() != text[i][k]):
                    count += 1
            if count == 1:
                correct = ""
                for k in range(len(vocabulary[j])):
                    if (vocabulary[j][k] != text[i][k]) and (vocabulary[j][k].upper() != text[i][k]):
                        correct += vocabulary[j][k]
                    else:
                        correct += text[i][k]
                for k in range(len(vocabulary[j]), len(text[i])):
                    correct += text[i][k]
                text[i] = correct
            count = 0
    return text


main()
