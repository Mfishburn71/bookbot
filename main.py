def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    word_counts = word_count(file_contents)
    char_counts = char_finder(file_contents)
    sorted_dict = sort_dict(char_counts)
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_counts} words found in the document")
    print("")
    for key, value in sorted_dict.items():
        print(f"The '{key}' character was found {value} times")
    print ("--- End report ---")



    
def word_count(file_contents):    
    words = len(file_contents.split())
    return (words)

def char_finder(file_contents):
    char_counts = {}
    lowered = file_contents.lower()
    for c in lowered:
        if c in char_counts:
            char_counts[c] += 1
        else:
            if c.isalpha() == True:
                char_counts[c] = 1
    return char_counts

def sort_dict(char_counts):
    sorted_dict = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

main()