#game bulls and cows
#contributor: Ilya Murychev
#date: 03-01-2023
import random

def secret_number():#generation secret number by computer
    num=[0]*4

    num[0] = random.randint(0,9)
    num[1] = random.randint(0, 9)
    num[2] = random.randint(0, 9)
    num[3] = random.randint(0, 9)

    while num[0]==num[1]:
        num[1]=random.randint(0,9)

    while num[0]==num[2] or num[1]==num[2]:
        num[2] = random.randint(0,9)

    while num[0] == num[3] or num[1] == num[3] or num[2]==num[3]:
        num[2] = random.randint(0, 9)

    return num

def piruk(number):#convertation number to array
    array=[0]*4
    for i in range(3,-1,-1):
        array[i] = number % 10
        number = number // 10
    return array
def bulls_cows(arr1, arr2):#counting of cows and bulls in certain number
    bulls=0
    cows=0
    cowbulls=[0,0]
    for i in range(4):
        for j in range(4):
            if arr1[i]==arr2[j]:
                if i==j:
                    bulls +=1
                else:
                    cows+=1
    cowbulls[0]=bulls
    cowbulls[1]=cows
    return cowbulls

number_arr = secret_number()
print("secret number = ", number_arr)#printing secret computer's number

bulls = 0
i=0
while bulls < 4:
    guess = int(input(f"\nAttemmpt nu {i+1}: Enter 4-digits guess number: "))
    i=i+1
    guess_arr = piruk(guess)
    bulls = bulls_cows(number_arr, guess_arr)[0]
    cows = bulls_cows(number_arr, guess_arr)[1]
    if bulls ==4:
        print("You are winner!!\n")
        break
    print(f"{bulls} bulls and {cows} cows")
