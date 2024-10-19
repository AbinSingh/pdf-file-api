# 3. Helper Function
import re


def calculate_word_lengths(text: str):
    # Split text into words, considering non-alphabetic chars as delimiters
    words = re.findall(r'\b\w+\b', text)

    # Calculate the length of each word
    word_lengths = {word: len(word) for word in words}

    return word_lengths
