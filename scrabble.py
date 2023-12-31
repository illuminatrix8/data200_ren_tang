from wordscore import score_word
from itertools import permutations

def run_scrabble(rack):
    """
    Returns a list of valid Scrabble words that can be constructed from the given rack, 
    sorted by their scores, and the total number of such valid words.

    Returns a tuple containing two elements:
      1) A list of tuples, each containing the score and the word.
      2) An integer representing the total number of valid words.
    """
    # Load the sowpods data within the function
    with open("sowpods.txt", "r") as infile:
        raw_input = infile.readlines()
        valid_words = set(datum.strip('\n').upper() for datum in raw_input)
    
    # Initial checks for input validity
    if not 2 <= len(rack) <= 7:
        return "Error: Rack should contain between 2 to 7 characters."

    # Check for more than two wildcards
    if rack.count('*') + rack.count('?') > 2:
        return "Error: Rack should contain at most two wildcards."
    
    for char in rack:
        if not char.isalpha() and char not in ['*', '?']:
            return f"Error: Invalid character '{char}' in rack. Only letters A-Z and wildcards are allowed."
    
    # Generate valid words from the rack
    possible_words = _generate_words_from_rack(rack)
    valid_scrabble_words = [(score_word(word), word) for word in possible_words if word in valid_words]

    # Sort the valid words by score and then alphabetically
    valid_scrabble_words.sort(key=lambda x: (-x[0], x[1]))

    return valid_scrabble_words, len(valid_scrabble_words)

def _generate_words_from_rack(rack):
    """
    A helper function that generates all possible words from the given rack, considering wildcards.
    """
    rack = rack.upper()
    possible_words = set()
    
    # wild card logic still has problem
    # Test run_scrabble with an input rack of '?a' (0/5)
    # Test Failed: False is not true : Expected: [(1, 'AA'), (1, 'AB'), (1, 'AD'), (1, 'AE'), (1, 'AG'), (1, 'AH'), (1, 'AI'), (1, 'AL'), (1, 'AM'), (1, 'AN'), (1, 'AR'), (1, 'AS'), (1, 'AT'), (1, 'AW'), (1, 'AX'), (1, 'AY'), (1, 'BA'), (1, 'DA'), (1, 'EA'), (1, 'FA'), (1, 'HA'), (1, 'JA'), (1, 'KA'), (1, 'LA'), (1, 'MA'), (1, 'NA'), (1, 'PA'), (1, 'TA'), (1, 'YA'), (1, 'ZA')]
    # Test run_scrabble with an input rack of 'abc*' (0/5)
    # Test Failed: False is not true : Returned word list result is not the same as expected
    # Test run_scrabble with an input rack of 'QU*ZZ' (0/5)
    # Test Failed: False is not true : Returned word list result is not the same as expected
    # Test run_scrabble with an input rack of '*?' (0/5)
    # Test Failed: False is not true : Returned word list result is not the same as expected

    if rack.count('*') + rack.count('?') == 2:  # both wildcards present
        for letter1 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            for letter2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                temp_rack = rack
                if '*' in temp_rack:
                    temp_rack = temp_rack.replace('*', letter1, 1)
                if '?' in temp_rack:
                    temp_rack = temp_rack.replace('?', letter2, 1)
                for length in range(2, len(temp_rack) + 1):
                    for perm in permutations(temp_rack, length):
                        possible_words.add(''.join(perm))
    elif '*' in rack or '?' in rack:  # only one wildcard present
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            temp_rack = rack
            if '*' in temp_rack:
                temp_rack = temp_rack.replace('*', letter, 1)
            if '?' in temp_rack:
                temp_rack = temp_rack.replace('?', letter, 1)
            for length in range(2, len(temp_rack) + 1):
                for perm in permutations(temp_rack, length):
                    possible_words.add(''.join(perm))
    else: # no wild card, so no need to replace anything
        for length in range(2, len(rack) + 1):
            for perm in permutations(rack, length):
                possible_words.add(''.join(perm))
    
    return list(possible_words)
