def word_count(s):
    # Your code here
    c = {}
    
    word = s.lower()
    null = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' ')

    for i in null:
        word = word.replace(i, '')

    word = word.split()

    for x in word:
        if x == '':
            return{}
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
    return c                   



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))