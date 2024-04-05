from collections import Counter
import re

def find_top_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)

    top_words = word_counts.most_common(10)

    return top_words

def write_to_file(words_count, output_file='output.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in words_count:
            file.write(f"{word}-{count}\n")

if __name__ == "__main__":
    input_file = input("Enter the file path: ")

    top_words = find_top_words(input_file)
    write_to_file(top_words)

    print("The result is written in the output.txt file.")