from random import randint
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

def main():
    fullName = GenerateName() + " "
    #fullName += GenerateLastName()
    print(fullName)

def GenerateName():
    name = ''
    for x in range(randint(1, 4)):
        name += GenerateSyllable()
    return name

def GenerateSyllable():
    syllable = ''
    lenght = randint(2,3)
    for x in range(lenght):
        if(x > 0 and x < 2):
            syllable += RandomLetter(True)
        else:
            syllable += RandomLetter(False)
    return syllable

def RandomLetter(isVowel):
    if isVowel == True:
        return vowels[randint(0,len(vowels) - 1)]
    else:
        return letters[randint(0,len(letters) - 1)]

if __name__ == '__main__':
    main()
