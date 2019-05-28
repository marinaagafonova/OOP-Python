class Filter:

    @staticmethod
    def filter_tags(inputstr):
        inputstr = list(inputstr)
        styletags = ("b", "i", "h1", "h2", "h3", "h4", "h5", "h6", "tt", "cite", "em", r'font.', r'a.', r'p.', "blockquote", "ol", "li", "ul")
        tag = ""
        tag_end = False
        # changes = {}   ключ - индекс открыв тега, значение - индекс закрывающегося тега
        for i in range(1, len(inputstr)):
            if (inputstr[i - 1] == '<' and inputstr[i] != '/') or inputstr[i - 1] == '/' and inputstr[i] != '>':
                tag += inputstr[i]
                tag_end = False
                continue
            if not(tag_end):
                if inputstr[i] != '>' and inputstr[i] != '/':
                    tag += inputstr[i]
                else:
                    tag_end = True
                    if not(tag in styletags):
                        key = i - len(tag) - 1
                        value = i
                        if(inputstr[key] == '/' or inputstr[key + 1] == '/'):
                            if inputstr[key] == '/':
                                inputstr[key - 1] = ""
                            else:
                                inputstr[key + 1] = ""
                        inputstr[key] = "&lt"
                        inputstr[value] = "&gt"
                        # changes[i - len(tag) - 1] = i
                    tag = ""



