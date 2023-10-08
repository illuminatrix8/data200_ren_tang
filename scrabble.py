from wordscore import score_word
from itertools import permutations

def run_scrabble(rack):
    """
    Returns a list of valid Scrabble words that can be constructed from the given rack, 
    sorted by their scores, and the total number of such valid words.

    Args:
    - rack (str): A string containing 2 to 7 characters representing the Scrabble rack.

    Returns:
    - tuple: A tuple containing two elements:
      1) A list of tuples, each containing the score and the word.
      2) An integer representing the total number of valid words.
    """
    # Load the sowpods data within the function
    with open("sowpods.txt", "r") as infile:
        raw_input = infile.readlines()
        valid_words = set(datum.strip('\n').upper() for datum in raw_input)
    
    # Initial checks for input validity
    if not 2 <= len(rack) <= 7:
        return "Error: Rack should contain between 2 to 7 characters.", 0
    
    for char in rack:
        if not char.isalpha():
            return f"Error: Invalid character '{char}' in rack. Only letters A-Z are allowed.", 0
    
    # Generate valid words from the rack
    possible_words = _generate_words_from_rack(rack)
    valid_scrabble_words = [(score_word(word), word) for word in possible_words if word in valid_words]

    # Sort the valid words by score and then alphabetically
    valid_scrabble_words.sort(key=lambda x: (-x[0], x[1]))

    return valid_scrabble_words, len(valid_scrabble_words)


def _generate_words_from_rack(rack):
    """
    A helper function that generates all possible words from the given rack without considering wildcards. 

    Args:
    - rack (str): The Scrabble rack.

    Returns:
    - list: A list of strings representing possible words.
    """
    rack = rack.upper()
    possible_words = set()  # Using a set to automatically handle duplicates

    for length in range(2, len(rack) + 1):
        for perm in permutations(rack, length):
            possible_words.add(''.join(perm))
    
    return list(possible_words)