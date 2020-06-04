# Your code here
from operator import itemgetter

# Read in all the words in one go
with open("robin.txt") as f:
    words = f.read()
# strip out unwanted characters
words = words.lower().translate(str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&'))
# and convert to a list
list_s = words.split()


def word_count(s):
   
    c = {}
    for word in list_s:
        if word in c:
            c[word] += 1
        else:
            c[word] = 1

    return c


def print_histo(dct):
    items = list(dct.items())
    
    items.sort(key=lambda e: (-e[1], e[0]))  # , reverse=(True, False))

    longest = len(
        sorted(items, key=lambda e: len(e[0]), reverse=True)[0][0])
    
    for tup in items:
        print(f'{tup[0]:{longest+2}}', tup[1]*'#')

print_histo(word_count(list_s))
