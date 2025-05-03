import sys

def get_num_words(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")

    words = file_contents.split()

    counter = 0 

    for word in words:
        counter += 1
    print(f"Found {counter} total words")	

def character_count(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    lowers = file_contents.lower()
    allw = {}
    
    chars = list(lowers)
      
    for char in chars:
        if char.isalpha == False:
            pass
        if char in allw:
            allw[char] += 1
        else:
            allw[char] = 1
    print(allw)

def sort_list(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    lowers = file_contents.lower()
    allw = {}
    
    chars = list(lowers)

    print("--------- Character Count -------")
      
    for char in chars:
        if char.isalpha():
            if char in allw:
                allw[char] += 1
            else:
                allw[char] = 1
        else:
            pass
    
    sortl = dict(sorted(allw.items(), key=lambda key_val: key_val[1], reverse=True))
    
    final_list = list(sortl)

    print()

    for word in final_list:
        print(f"{word}: {allw[word]}")
    print("============= END ===============")

       