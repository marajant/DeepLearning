b = 'pwwkew'

def lengthOfLongestSubstr(word):
    """Function takes in a string and finds the longest substring and returns the length
    and characters of the substring
    input: string
   output: a string and an int"""
    currentPosition = 1
    longest = 1
    seen = {}
    i = 1

    while i < len(word):
        letter = word[i]
        """if letter in last seen, set i back to the last seen character position
        and add one. Clear last seen and set the new max and reinitialize the current postion"""
        if letter in seen:
            i = seen[letter] + 1
            seen.clear()
            longest = max(longest, currentPosition)
            currentPosition = 0
        else:
            """else add the letter to the seen and iterate current position and I"""
            seen[letter] = i
            currentPosition += 1
            i += 1

    longest = max(longest, currentPosition)

    """Iterate through the keys of the dict and concatenate the keys to an empty string"""
    substr = ""
    for i in seen.keys():
        substr += i
    return longest,substr

print(lengthOfLongestSubstr(b))