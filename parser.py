# quick and dirty python text parser
#  by stanley kaymen


# name of the text file
textfile = "example.txt"

# for storing number of lines, words, characters, and counts per word length
nlines = 0
nwords = 0
nchars = 0
lencounts = [0] * 19

# counts of letters, nonletters, and numbers
lettercount = 0
nonlettercount = 0
numcount = 0

# letters and numbers for reference
letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numberlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# open up the file
with open(textfile, 'r') as f:
    # go line by line
    for line in f:

        nlines += 1

        words = line.split()
        nwords += len(words)
        nchars += len(line)

        # go word by word
        for word in words:
            thisnonlettercount = 0
            thisnumcount = 0

            # ignore case
            word.lower()
            prevchar = 'x'

            # go char by char
            for char in word:
                # we found a letter
                if char in letterlist:
                    lettercount += 1
                else:
                    # we found a number (make sure continuous numbers are only counted once)
                    if char in numberlist and prevchar not in numberlist:
                        thisnumcount += 1;
                    # whether number or not, we found a non letter
                    nonlettercount += 1
                    thisnonlettercount += 1
                prevchar = char
            numcount += thisnumcount
            # keep track of words of the designated length
            if (len(word) < 20):
                lencounts[len(word) - 1 -   thisnonlettercount] += 1


# print out our data
print("File name: " + textfile)
print("Number of lines: " + str(nlines))
print("Number of characters(total): " + str(nchars))
print("Number of letters: " + str(lettercount))
print("Number of figures: " + str(numcount))
print("Number of other characters: " + str(nonlettercount))
print("Number of spaces: " + str(nchars - lettercount - nonlettercount))
print("Number of words: " + str(nwords))

# print out words of the given lengths
for i in range(0,16):
    print("Number of " + str(i+1) + " letter words: " + str(lencounts[i]))
print("Number of 19 letter words: " + str(lencounts[18]))
