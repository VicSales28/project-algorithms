def is_palindrome_iterative(word):
    if not word or not isinstance(word,str):
        return False
    
    word = word.lower()

    left, right = 0, len(word) - 1
    
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True