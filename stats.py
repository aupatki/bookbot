def get_book_text(filepath):
    return filepath.read()

def word_count(book_text):
    return book_text.split()

def char_count(book_text):
    # initializing needed variables
    
    # chars dictionary will hold "char" -> int
    chars = {}  

    # function code
    text = word_count(book_text)
    for word in text:
        word = word.lower()
        for i in range(0,len(word)):
            character = word[i]
            if character in chars:
                chars[character] += 1
            else:
                chars[character] = 1
    
    return chars

def sort_on(items):
    return items["count"]

def dict_list(dictionary):
    # list of dictionaries
    d_list = []

    for char in dictionary:
        d_list.append({"char": char, "count": dictionary[char]})

    return d_list


