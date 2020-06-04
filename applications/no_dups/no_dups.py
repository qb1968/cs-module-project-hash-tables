def no_dups(s):
    # Your code here
    dups = {}
    no_dups = []
    x = s.split(' ')

    for i in x:
        if i not in dups:
            dups[i] = 1
            no_dups.append(i)

    return ' '.join(no_dups)        

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))