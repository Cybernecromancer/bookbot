def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(filepath):
    result = get_book_text(filepath)
    wordlist = result.split()
    return(len(wordlist))

def get_num_chars(filepath):
    result = get_book_text(filepath)
    lowercase_result = result.lower()
    dict_result = {}
    for character in lowercase_result:
        if character in dict_result:
            dict_result[character] += 1
        else:
            dict_result[character] = 1
    return(dict_result)

def get_sorted_list(filepath):
    sorted_list = []
    raw_dict = get_num_chars(filepath)
    for char, count in raw_dict.items():
        char_info_dict = {}
        char_info_dict["char"] = char
        char_info_dict["num"] = count
        sorted_list.append(char_info_dict)
    sorted_list.sort(reverse=True, key=lambda dict: dict["num"])
    return sorted_list




