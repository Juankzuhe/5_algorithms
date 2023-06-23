def length_of_longest_substring(s: str) -> int:
    """ Given a string, find the length of the longest substring without repeating characters. """
    output = 0
    count = {}
    pos = -1
    for index, letter in enumerate(s):
        if letter in count and count[letter] > pos:
            pos = count[letter]
        count[letter] = index
        output = max(output, index - pos)
    return output

string = "abcabcbb"
print(length_of_longest_substring(string))
string = "bbbbb"
print(length_of_longest_substring(string))
string = "pwwkew"
print(length_of_longest_substring(string))
string = ""
print(length_of_longest_substring(string))