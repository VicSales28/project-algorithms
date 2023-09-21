def is_palindrome_recursive(word, low_index, high_index):
    if not isinstance(word, str) or len(word) == 0:
        return False

    word = word.lower()

    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False