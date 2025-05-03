from stats import get_num_words, character_count, sort_list
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
book_path = sys.argv[1]



get_num_words(book_path)
sort_list(book_path)



