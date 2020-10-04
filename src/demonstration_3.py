"""
Given a `string`, write a function that finds the first non-repeating character in the `string` and return its index. If it doesn't exist, return -1.

Examples:

string = "lambdaschool"
return 2.

string = "lovelambdaschool"
return 2.

string = "abcabc"
return -1.
"""


def first_unique_char(string):
    # Your code here
    # list1 = [char for char in string]
    # for i, char in enumerate(list1):
    #     if char not in list1[i + 1:] and len(list1[i + 1:]) >= 2:
    #         return i
    #     else:
    #         return -1

    # for char in string:
    #     if string.lower().count(char) == 1:
    #         return string.index(char)
    # return -1

    counts = {}

    #  loop through our string to populate dictionary
    #  with the counts of each character

    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    #  loop over the string again
    #  for each char, check how many times it occurs
    #  return the index of the first char that occirs once

    for index, char in enumerate(string):
        if counts[char] == 1:
            return index

    # otherwise, no char in the string occured exactly once

    return -1


print(first_unique_char("lambdaschool"))
