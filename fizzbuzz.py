'''fizzbuzz is a game where you count from 1 to n and for specific conditions we say something
if the number is divisible by 3 we say fizz
if the number is divisible by 5 we say buzz
if the number is divisible by both we say fizzbuzz
for other we just say the numbers'''

def FizzBuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(i,"FizzBuzz")
        elif(i%3==0):
            print(i,"Fizz")
        elif(i%5==0):
            print(i,"Buzz")
        else:
            print(i)      
FizzBuzz(101)