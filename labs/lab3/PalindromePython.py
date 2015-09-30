word = input()# takes in user entry

word = word.replace(" ", "")#removes any spaces
print(word == word[::-1])
