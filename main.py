def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

file_contents = main()


def word_count(book):
    word_count = 0 
    words = book.split()
    for word in words:
        word_count += 1
    return word_count

word_count_number = word_count(file_contents) 

def characters(book):
    lowered_string = book.lower()
    character_dict = {}
    for character in lowered_string:
         if character not in character_dict:
            character_dict[character] = 1 
         elif character in character_dict:
            character_dict[character] += 1
    return character_dict        

character_dict = characters(file_contents)
dict_list = list(character_dict.items())

def sort_on(dict):
    return dict[0]


dict_list.sort(reverse=True, key=sort_on)

def pretty_list(list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count_number} words found in the document")
    for key in list:
        if key[0].isalpha():
            print(f"The '{key[0]}' character was found {key[1]} times")
    print("--- End report ---")









pretty_list(dict_list)



 
