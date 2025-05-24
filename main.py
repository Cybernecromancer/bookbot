def main():
    from stats import get_num_chars, get_num_words, get_sorted_list
    sorted_counts = get_sorted_list()
    #char_counts = get_num_chars()
    word_count = get_num_words()
    #print(word_count, "words found in the document")
    #print(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(word_count) + " total words")
    print("--------- Character Count -------")
    for dict in sorted_counts:
        char_string = str(dict["char"])
        num_string = str(dict["num"])
        if char_string.isalpha():
            print(char_string + ": " + num_string)
    print("============= END ===============")

main()