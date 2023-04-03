def improved_word_count(file_path: str) -> dict:
    """
    This function Counts the occurrence of each word in the given text file with improved logic.

    Args: file_path (str): The path of the text file to analyze.

    Returns: dict: if file exist else None
    """
    if not file_path:
        return None
    
    word_counts = {}
    
    with open(file_path, 'r') as text_file:
        for each_line in text_file:
            
            words_in_line = each_line.translate(str.maketrans('', '', '.,;!?-\t\n\'\"')).lower().split()
            
            for each_word in words_in_line:
                word_counts[each_word] = word_counts.get(each_word, 0) + 1
    
    return word_counts


if __name__ == "__main__":
    file_path_to_analyze = "sample.txt"    # Enter text file path here
    result = improved_word_count(file_path=file_path_to_analyze)
    print(result)
    
    
# Instead of iterating through the word list for each new word and checking 
# if it already exists in the dictionary, use a value of 1 to add each new word 
# to the dictionary or check that the existing one is incremented by 1.
# The time complexity of this implementation is O(N). where N is the number 
# of characters in the input file. This is because the implementation reads 
# the file line by line and processes each line by removing punctuation and 
# dividing it into words, so each character is read and processed once. 
# However, the dictionary retrieval method has an average time complexity of O(1). 
# This means that our overall runtime complexity is improved compared to previous 
# implementations. The implementation space complexity is still O(N). 
# where N is the number of unique words in the input file. This is because 
# the implementation maintains a dictionary of number of words that can have at most N entries.
