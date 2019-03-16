import argparse


def choose_root(roots):
    max = len(roots[0])
    res = roots[0]
    for r in roots:
        if max < len(r):
            max = len(r)
            res = r
    return res


def checkable(word, vocabulary):
    res = []

    for v in vocabulary:
        n = len(v)
        i = 0
        mistakes = 0
        word = word.lower()
        while(i+n<len(word)):
            for j in range(n):
                if word[j+i] != v[j]:
                    mistakes += 1
                if mistakes > 1:
                    break
            if mistakes == 1:
                res.append(v)
            if mistakes == 0:
                res.append(v)
            mistakes = 0
            i += 1
    if len(res) > 1:
        return choose_root(res)
    elif len(res) == 1:
        return res[0]
    else:
        return ""


def index_of_mistake(word, root):
    i = 0
    mistake = 0
    n = len(root)
    word = word.lower()
    while(i+n<len(word)):
        for j in range(n):
            if(word[j+i] != root[j]):
                mistake += 1
            if(mistake > 1):
                break
        if mistake==1:
            return i
        mistake = 0
        i += 1


def change_the_text(text, root, i1, i2):
    for i in range(i1+i2, i1+i2+len(root)):
        #text = text[:i1 + i] + root[i-i2] + text[i1 + i + 1:]
        if(text[i].lower() == root[i-i1-i2]):
            continue
        text[i] = root[i-i1-i2]
    return text


def find_mistake(text, vocabulary):
    index = 0
    marks = (" ", ":", ";", ",", ".", "\n", "(", ")") #add sth
    while(index != len(text)):
        if(text[index] in marks):
            index+=1
            continue
        word = ""

        while(index < len(text) and not(text[index] in marks)):
            word += text[index]
            index += 1
        result = checkable(word, vocabulary)
        if(result != ""):
            i = index_of_mistake(word, result)
            if(i!=None):
                text_list = list(text)
                text_list = change_the_text(text_list, result, index-len(word), i) #may be mistake with index
                text = ''.join(text_list)
    return text







'''
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
'''

def open_file(filename):
    file = ""
    with open(filename) as inf:
        for string in inf:
            file += string
        #temp = file.split("{")
        #text = removing_of_regular_expressions(temp[0])
        #vocabulary = removing_of_regular_expressions(temp[1])
    return file


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('fileTextName')
    parser.add_argument('fileVocabularyName')
    #parser.add_argument('--output')
    args = parser.parse_args()
    text = open_file(args.fileTextName)
    vocabulary = open_file(args.fileVocabularyName)
    #re.split('\s |, ',vocabulary)
    vocabulary = vocabulary.split(",")
    return [text, vocabulary]


def main():
    inputInf = parse_input()
    text = find_mistake(inputInf[0], inputInf[1])

    #text = open_file("text.txt")
    #vocabulary = open_file("vocabulary.txt")
    
    #inputInf = open_file(args.fileTextName)
    #text = inputInf[0]
    #vocabulary = inputInf[1]
    #text = find_mistakes(text, vocabulary)

    print(text)
'''
def print_result(text):
    for i in range(len(text)):
        print(text, end=' ')


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
'''

main()
