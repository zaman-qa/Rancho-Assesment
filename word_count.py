def word_count(file_path: str) -> dict:
    """
    This function Counts the occurrence of each word in the given text file.

    Args: file_path (str): The path of the text file to analyze.

    Returns: The word with the highest occurance, or it's empty.
    """
    if not file_path:
        return None
    
    word_counts = {}
    
    with open(file_path, 'r') as text_file:
        for each_line in text_file:
            words_in_line = each_line.translate(str.maketrans('', '', '.,;!?-\t\n\'\"')).lower().split() # Remove punctuation and split into words
            for each_word in words_in_line:
                if each_word not in word_counts:
                    word_counts[each_word] = 0
                word_counts[each_word] += 1
    
    return word_counts


if __name__ == "__main__":
    file_path_to_analyze = "sample.txt"    # Enter text file path here
    result = word_count(file_path=file_path_to_analyze)
    print(result)
    

# This implementation reads a text file line by line and processes each 
# line by removing punctuation and breaking it into words. The functions 
# str.maketrans and translate are used to remove the specified punctuation 
# marks from each line. The resulting words are converted to lowercase to 
# avoid case sensitivity when counting words. Then memorize the word count 
# dictionary. where each key is a word and each value is the number of occurrences 
# of that word in the file. When a word is encountered for the first time, 
# it is added to the dictionary with the number 1. If the word is found again, its count is increased by 1.