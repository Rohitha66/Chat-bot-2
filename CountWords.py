
class CountWords:
    # Python program to count the number of occurrence
    # of a word in the given string given string

    def countOccurences(str_, word):
        str_=str_.lower()
        word=word.lower()
        # split the string by spaces in a
        a = str_.split()
        # search for pattern in a
        count = 0
        for i in range(0, len(a)):
            # if match found increase count
            if (word == a[i]):
                count = count + 1
        return count


if __name__ == '__main__':
    str = "A computer science     portaL portal geeks  "
    word = "portaL"
    print(CountWords.countOccurences(str, word))
