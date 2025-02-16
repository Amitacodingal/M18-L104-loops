

#Sum of first n natural numbers:
n = int(input("Enter the number whose sum you want to find: "))
sum=0

#Iterates for n+1 times: i=1 to n+1
for i in range(1, n+1):
    sum = sum+i
    print("\nSum =", sum)
    
    
#Input a word or sentence reverse of a word reverse a string
string = input("Please enter your own String : ")

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe Original String = ", string)
print("The Reversed String = ", string2)


# input number greater than 1 reverse order
n = int(input("Enter the value of n: "))

# print the numbers from n to 1
print ("numbers from 0 to 1 are: ".format(n,1))

# loop to print numbers
for i in range(n,0,-1):
    print (i)
    
    
#input 
text = input(("Enter a sentence: "))
text = text.split()
bigWordLen = 0 
#chevking wrd length
for wrd in text: 
  wrdLen = len(wrd) 
  if wrdLen>bigWordLen: 
    bigWordLen = wrdLen

print("\nLargest Word: ")
for wrd in text: 
  wrdLen = len(wrd)
  if wrdLen==bigWordLen: 
    print(wrd) 
    
    
#Take input of a string
str1 = input("Please Enter a sentence: ")
total = 1 

for i in range(len(str1)): 
#l calculate the length of string operation
    if(str1[i] == ' ' ):
        total = total + 1

print("Total Number of Words in this String = ", total)

#ACP

import math
number=int(input("tell a no"))
power=int(input("enter the power no"))
print(math.pow(number,power))


