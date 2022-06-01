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


#6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

orig_price = float(input('Input the original price: '))
disc_perc = float(input('percent discount percentage: '))

def apply_discount(origprice, discperc):
    perc = discperc/100
    total6 = origprice * (1-perc)
    return total6

apply_discount(orig_price, disc_perc)

#7 Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

num7 = input('Input number: ')

def handle_commas(num):
    return num.replace(',', "")

handle_commas(num7)




#8 Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

while True:
    num_grade = int(input('Integer grade please:'))
    if num_grade >= 88:
        print('A')
    elif num_grade >= 80:
        print('B')
    elif num_grade >= 67:
        print('C')
    elif num_grade >= 60:
        print('D')
    else:
        print('F')

    choice = input('Do you want to continue? Plese enter y or n')
    if choice.lower() == 'y':
        continue
    else:
        break



#9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def is_vowel(alpha):
    if alpha in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
      return True
    else:
        return False


def remove_vowels(words):
    for char in words:
        if is_vowel(char) == True:
            words = words.replace(char, '')
    return (words)


remove_vowels('potato')

#10 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
    # for example:
    #     Name will become name
    #     First Name will become first_name
    #     % Completed will become completed


def normalize_name(input):
    input.lower()









# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list):
    output = [list[0]]
    q= len(list)
    n=0
    while n < (q-1):
        r =output[n]+list[n+1]
        output.append(r)
        n += 1
    return output

cumulative_sum([1,1,1])