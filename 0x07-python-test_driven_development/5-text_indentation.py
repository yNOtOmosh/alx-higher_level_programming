#!/usr/bin/python3
"""Define the indentetion of text."""

def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    current_sentence = ""

    for char in text:
        if char in ".?:":
            sentences.append(current_sentence.strip())
            current_sentences = ""
        else:
            current_sentence += char

    if current_sentence:
        sentences.append(current_sentence.strip())

    for sentence in sentences:
        print(sentence)
        print("\n")
