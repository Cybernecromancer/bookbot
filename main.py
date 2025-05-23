def main():
    from stats import get_num_chars, get_num_words
    char_counts = get_num_chars()
    word_count = get_num_words()
    print(word_count, "words found in the document")
    print(char_counts)
main()