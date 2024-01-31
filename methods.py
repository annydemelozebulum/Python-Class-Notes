text = "abcdefg"

print(dir(text))
help(text.isidentifier)
print(text.isidentifier())
print("1234".isidentifier())
print("anananananannananan".count("ana"))
print("anananananannananan".replace("ana", "banana"))
print("anananananannananan".find("ana", 1))
print("bbbbbbabbbbbabbbbbabbbba".split("a"))
print("this is a sentence and i want the words".split(" "))
sentence = "Hello, kind sir, how many i be of service today?"
punctuation = ".,;?!-"

#sanitize the sentences

for p in punctuation:
    sentence = sentence.replace(p, "")#replace the punctuaiton with nothing
print(sentence)

#split into words
words = sentence.split(" ")
print(words)

text = "cat"
print(text.upper())
print(text)



name = "John"
second_name = "Bob"
print(f"Hi, {name} how are you? My name is {second_name}")
name = "Jane"
second_name = ("Mary")
print(f"Hi, {name} how are you? My name is {second_name}")