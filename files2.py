print("Here will be the contents of the file:")
num_alines = 0
with open("x-files.txt", "r") as f:
    for line in f:
        num_alines += line.lower().count("alien")
#above words similar to alien capital lettters
# num_alines += line.count("alien") Exact word

print("the word alien shows up", num_alines, "times in the file")
