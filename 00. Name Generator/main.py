from random import randint
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

def main():
    for x in range(0, 50):
        print(GenerateSyllable())

def GenerateSyllable():
    syllable = ''
    lenght = randint(2,3)
    for x in range(lenght):
        if(x > 0 and x < 2):
            syllable += RandomLetter(True)
        else:
            syllable += RandomLetter(False)
    return syllable

def RandomLetter(vowel):
    if vowel == True:
        return vowels[randint(0,len(vowels) - 1)]
    else:
        return letters[randint(0,len(letters) - 1)]

if __name__ == '__main__':
    main()
