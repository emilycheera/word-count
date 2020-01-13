# put your code here.
def count_words(filename):

    text_file = open(filename)
    all_words = []

    for line in text_file:
        line = line.rstrip()
        line = line.split()
        all_words.extend(line)

    word_counts = {}

    for word in all_words:
        word_counts[word] = word_counts.get(word, 0) + 1


    return word_counts


def format_dict(counted_words):
    for word, count in counted_words.items():
        print(word, count)


counted_words = count_words("twain.txt")
format_dict(counted_words)
# print(counted_words)