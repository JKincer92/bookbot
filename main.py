
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    character_count = get_character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(character_count) 

    print("--- Begin report of books/frankenstein.txt---")
    print(f"{num_words} words found in the document\n")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("\n--- End report ---")   
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()      


def get_word_count(text):
    return len(text.split())

def get_character_count(chars):
    character_count = {}
    lowered_chars = chars.lower()
    for char in lowered_chars:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

    
if __name__ == "__main__":
     main()
     
        