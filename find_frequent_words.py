import re
from collections import Counter

def most_frequent_words(file_path, num_words=10):
    
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\w+', text.lower())

    word_count = Counter(words)

    
    most_common = word_count.most_common(num_words)

    return most_common


file_path = 'your_text_file.txt'  
num_words = 10  

frequent_words = most_frequent_words(file_path, num_words)

for word, count in frequent_words:
    print(f"{word}: {count} times")
