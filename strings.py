#strings

#Exercise: Iterate over a string backwards using while

text = "abcdefg"
i = 0
while i < len(text):
    print(text[len(text)-1-i])
    i += 1
