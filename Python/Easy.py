from typing import List

""" 
                                344. Reverse String
 Write a function that reverses a string. The input string is given as an array of characters s.
 You must do this by modifying the input array in-place with O(1) extra memory.
"""


# Shifting the places for two characters at a time
def reverseString(self, s: List[str]) -> None:
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i = i + 1
        j = j - 1
