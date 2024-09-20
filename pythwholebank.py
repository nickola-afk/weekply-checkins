x = 5
f = lambda x: 1 + 2
print(f(x))
##
##1.
##1 # The calc_power function calculates exponents  
##2 # x is the base
##3 # y is the exponent
##4 # The value of x raised to y power is returned
##5 def calc_power(x, y):
##6     comment = "#Return the value"  
##7     return x ** y # raise x to the y power
##
##
##2.
### Function accepts a list of words from a file,
### and letter to search for.
### Returns count of a particular letter in that list.
##def count_letter(letter, word_list):
##    count = 0
##    for 
##Question Blank 1 of 2
##word is word_list
##:
##       if 
##Question Blank 2 of 2
##word in letter
##:
##           count +=1
##       return count
##word_list = []
### word_list is populated from a file. Code not shown
##letter = input("Which letter would you like to count? ")
##letter_count = count_letter(letter, word_list)
##print("There are: ", letter_count, " instances of " + letter)
##
##
##
##
##5.
##1     
##2     name = input("What is your name? ")
##3     return name
##4
##5     calories = miles * calories_per_mile
##6     return calories
##7 distance = int(input("How many miles did you bike this week? "))
##8 burn_rate = 50
##9 biker = get_name()
##10 calories_burned = calc_calories(distance, burn_rate)
##11 print(biker, ", you burned about", calories_burned, "calories.")
##
##
##
##
##
##
##8.
##import math
##l =[str(round(math.pi)) for i in range (1, 6)]
##print(l)
##
##
##
##
##9.
##01 numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##02 index = 0
##03 while (index < 10)
##04     print(numbers[index])
##05
##06     if numbers(index) = 6
##07         break
##08     else :
##09         index += 1
##
##
##
##
##
##10.
##a = 0
##b = a ** 0
##if b < a + 1:
##     c = 1
##elif b == 1:
##     c = 2
##else:
##     c = 3
##print(a + b + c)
##
##
##14.
##numList = [1,2,3,4,5]
##alphaList = ["a", "b", "c", "d", "e"]
##print(numList is alphaList)
##print(numList == alphaList)
##numList = alphaList
##print(numList is alphaList)
##print(numList == alphaList)
##
##16.
##i = 250
##while len(str(i)) > 72:
##     i *= 2
##else:
##     i //= 2
##print(i)
##
##18.
##import sys
##try:
##    file_in = open('in.txt', 'r')
##    file_out = open('out.txt', 'w+')  # file DNE but 'w+' will create one 
##except IOError:
##    print('cannot open', file_name)  # file_name DNE
##else:
##    i = 1
##    for line in file_in:
##        print(line.rstrip())
##        file_out.write("line " + str(i) + ": " + line)
##        i = i + 1
##    file_in.close()
##    file_out.close()
##
##
##1.
##import os
##def read_file(file):
##     line = None
##     if os.path.isfile(file):
##         data = open(file, 'r')
##     while line != '':
##         line = data.readline()
##         print(line)
##
##
##
##
##
##7.
##i = 250
##while len(str(i)) > 72:
##     i *= 2
##else:
##     i //= 2
##print(i)
##
##
##
##
##
##
##5.
##sum = count = done = 0
##average = 0.0
##while (done != -1)
##        rating =  float(input("Enter next rating (1-5) or -1 for done "))
##        if rating == -1:
##                break
##          sum += rating
##        count += 1
##average = float(Sum/count)
##print("The average star rating for the NetVerZleep coffee is: " + format(average, '.2d'))
