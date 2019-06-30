
GREEN = '\033[32m'
PRETTY_GREEN = ' <span style="color: #ff6600;">'
END_COLOR = '</span>'

class Search():

    @staticmethod
    def color_find(pattern, string, ignore_case):
        """Find all matches of pattern in string. Returns colored string, or empty string if not found."""
        result = ''
        index = Search.index_find(pattern, string, ignore_case)

        while index != -1:
            result += string[:index]
            result += PRETTY_GREEN + string[index:index + len(pattern)] + END_COLOR
            string = string[index + len(pattern):]
            index = Search.index_find(pattern, string, ignore_case)

        return result if result == '' else result + string

    @staticmethod
    def index_find(pattern, string, ignore_case):
        """Find index of pattern match in string. Returns -1 if not found."""
        if ignore_case:
            pattern = pattern.lower()
            string = string.lower()

        for i in range(len(string)):
            for j in range(len(pattern)):
                if string[i+j] != pattern[j]:
                    break
                elif j == len(pattern) - 1:
                    return i
        return -1
