"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if (x % 2 == 0):
        return False
    else:
        return True

def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    backwards = word[::-1]
    if word == backwards:
        return True
    else:
        return False

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    odd_list = []
    for i in range(len(numlist)):
        if (numlist[i] % 2 != 0):
            odd_list.append(numlist[i])
    return odd_list

def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    word_counts = {}
    word_list = text.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
        count = word_list.count(word_list[i])
        word_counts[word_list[i]] = count
    return word_counts

# Testing Functions


print(is_odd(5)) # Should be True
print(is_odd(4)) # Should be False

print(is_palindrome(('racecar'))) # Should be True
print(is_palindrome('car')) # Should be False

print(only_odds([1,2,3,4,5,6])) # Should be [1,3,5]

print(count_words('A cat is not a dog')) # Should be {'a': 2, 'cat': 1, 'is': 1, 'not': 1, 'dog': 1}



