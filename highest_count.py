from word_count import word_count

def highest_count(words_dict: dict):
    """
    This function finds the word with the highest count in words dictionary.

    Args: word_counts (dict): A dictionary for all words in the list.

    Returns: The word with the highest occurance, or None if it's empty.
    """
    if not words_dict:
        return None
    
    highest_count = 0
    highest_count_word = None
    
    
    for word, count in words_dict.items():
        if count > highest_count:
            highest_count = count
            highest_count_word = word
    
    return {highest_count_word: highest_count}

if __name__ == "__main__":
    file_path_to_analyze = "sample.txt"    # Enter text file path here
    words_dictionary = word_count(file_path=file_path_to_analyze)
    result = highest_count(words_dict=words_dictionary)
    print(result)
    
    
# This above implementation basically itterates over the dictionary of words and keeps track 
# of the word with the highest count. The time complexity 
# of this execution is O(N), where N is the numbers dictionary, 
# since we got to emphasize over each key-value pair 
# within the dictionary. The space complexity of the execution is O(1), 
# because we only need to maintain a constant number of variables to keep 
# track of the highest count and the word with the highest count.