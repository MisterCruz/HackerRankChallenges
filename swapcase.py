'''
Sample Input:
>>> HackerRank.com presents "Pythonist 2".

Sample Output:
>>> hACKERrANK.COM PRESENTS "pYTHONIST 2".

'''

def swap_case(s):
    newWord = ""
    for char in s:
        if char.isupper():
            newWord += char.lower()
        if char.isalpha() != True:
            newWord += char
        elif char.islower():
            newWord += char.upper()
    return newWord
