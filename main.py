def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    result = get_book_text("bookbot/books/frankenstein.txt")
    print(result)

main()