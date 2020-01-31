from collections import Counter
def word_count(f_name):
    with open(f_name) as f:
        return Counter(f.read().split())
print("words in text file:",word_count("char.txt"))