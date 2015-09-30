word = input()# takes in user entry

word = word.replace(" ", "")#removes any spaces
word = word.lower()#lowers the case so it can run the Oxo etc
print(word == word[::-1])#checks and prints a boolean logic on whether or not the variable is the same when reversed
