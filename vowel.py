def replaceVowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = ['jose','kd','dawn','liss','georlit','emy','divya']
    
    new_string = []
    for word in string:
        new_word = ''
        for letter in word:
            if letter in vowels:
                new_word += '0'
            else:
                new_word += letter
        new_string.append(new_word)
    print(new_string)
replaceVowels()

def replaceVowels1():
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = ['jose', 'kd', 'dawn', 'liss', 'georlit', 'emy', 'divya']
    
    new_string = []
    for word in string:
        for vowel in vowels:
            word = word.replace(vowel, '0')
        new_string.append(word)
    
    print(new_string)

replaceVowels1()

