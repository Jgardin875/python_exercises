
#1a


weekday = input('What day of the week is it? ')
if weekday.lower() == 'monday':
    print('Today is Monday')
else:
    print('Today is not Monday')

#note weekday.capitalize is a function too

#1b
weekday = input('What day of the week is it? ')
if weekday.lower() == 'saturday' or weekday.lower() == 'sunday':
    print('Weekend!!!!')
else:
    print('Work day.')


#1c
hrs_wk = float(input('Hours per week?'))
hrly_rate = float(input('hourly rate'))
full_time = 40

if hrs_wk <= full_time:
    q = hrs_wk * hrly_rate
    print(q)
else:
    p = (full_time * hrly_rate) + ((hrs_wk - full_time) * (1.5 * hrly_rate))
    print(p)



#2a
i = 5
while i <= 15:
    print(i)
    i += 1

z = 0
while z <= 100:
    print(z)
    z += 2


f = 100
while f >= -10:
    print(f)
    f -= 5

t = 2
while t <= 1_000_000:
    print(t)
    t *= t


f = 100
while f >= 5:
    print(f)
    f -= 5


#2bi
num = int(input('Input integer: '))
for s in range(1, 11):
    print(f'{num} x {s} = {s * num}')


#2bii
for r in range(1, 10):
    print(r * str(r))




#2c
num = input('Please enter an odd number betwween 1 and 50: ')

while True:
    if (num.isdigit() == False
        or int(num) > 50
        or int(num) <1 
        or int(num) % 2 == 0):
        print ('Invalid Input')
        num = input('Please enter an odd number betwween 1 and 50: ')
    else:
        break

num = int(num)

print('The number to skip is', num)
for i in range (1, 50):
    if i % 2 == 0:
        continue
    elif i == num:
        print('Yikes, skipping this number', i)
    else:
        print('Here is an odd number', i)


#2d  
num = input('Please input a positive integer: ')

while True:
    if (num.isdigit() == False 
        or int(num) < 0):
        print('Invalid Entry')
        num = input('Please input a positive integer: ')
    else:
        break 
    
for i in range(0, (int(num) + 1)):
    print(i)


#2e   
pos_num = input('Enter positive number: ')
while True:
    if (pos_num.isdigit() == False
        or int(pos_num) < 0):
        print('Invalid entry. Please enter a positive integer')
        pos_num = input('Enter positive number: ')
    else:
        break
pos_num = int(pos_num)

while (pos_num) >= 1:
        print(pos_num)
        pos_num -= 1


#3
for l in range (101):
    if l % 15 == 0:
        print('FizzBuzz')
    elif l % 5 ==0:
        print('Buzz')
    elif l % 3 == 0:
        print ('Fizz')
    else:
        print(l)    
    
#4 
v = int(input('What number would you like to go up to?'))

print('Here is your table!')
print('number | squared | cubed')
print('------ | ------- | -----')

for i in range (1, (v + 1)):
    print(f'{i:^6} | {i**2:>7} | {i**3:<5}')

# i:6 indicates that it will make 6 spaces in that column (6 letters in number, 7 in squared, 5 in cubed)
# ^ symbol centers the column
# > aligns column to the right
# < aligns column to the left




#5


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



#6
books = [{'title': 'Harry Potter', 'author': 'JK Rowling', 'genre': 'fantasy'},
        {'title': 'Sleeping Giants', 'author': 'S Neuvel', 'genre': 'sci-fi'},
        {'title': 'American Sniper', 'author': 'C Kyle', 'genre': 'autobiography'},
        {'title': 'Hitch Hikers Guide', 'author': 'D Adams', 'genre': 'fantasy'}]


for book in books:
    print(f"The book {book['title']} by {book['author']} is in the {book['genre']} genre")



user_input = input('Please enter an genre: ')
l = []
for book in books:
    if book['genre'] == user_input:
        l.append(book['title'])
        print(book['title'])

#why does print book titles work, i thought it had to be print l?

find_genre = input('What genre are you looking for? ')
l = []
for book in books:
    if find_genre == book['genre']:
        l.append(book['title'])
        print(l)