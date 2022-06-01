#1 Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(arg):
    if arg in [2, '2']:
        return True
    else:
        return False

print(is_two(1))

print(is_two(2))

#or

def is_two(arg):
    if arg == 2 or arg == '2':
        return True
    else:
        return False

print(is_two(1))

print(is_two('2'))


#2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(alpha):
    if alpha in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
      return True
    else:
        return False

print(is_vowel('a'))
print(is_vowel('b'))

#3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(beta):
    if beta in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
      return False
    else:
        return True


print(is_consonant('a'))
print(is_consonant('b'))

#4 Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def const_capt(word):
    if is_vowel(word[0]) == True:
        return word
    if is_vowel(word[0]) == False:
        return word.capitalize()


print(const_capt('apple'))
print(const_capt('pig'))

#5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

tip = float(input('Please put tip amount in decimal form '))
bill = float(input('Please input total bill '))

while True:
    if (tip <0
        or tip >1):
        print('Invalid Input')
        tip = input('Please put tip amount in decimal form ')
    else:
        break


def calculate_tip(tip1, bill1):
    return(bill1 + (tip1*bill1))

calculate_tip(tip, bill)
