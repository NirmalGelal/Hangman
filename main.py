#this is a console based hangman game.
#I've made a list with 10 different car names.


import random
cars =['bugatti','ferrari','mercedes','audi','lamborghini','rolls-royce','tata','ford','renault','jaguar','lexus','toyota']
s= random.choice(cars)
dash=len(s)*'_'
result=list(dash)
count=4

while count>0:
    n=0
    print('you have '+ str(count)+ ' guess left')
    x=input("your guess: ")

    for i in range(len(s)):
        if(x==s[i]):
            result[i]=x
            print(result[i],end='')
        else:
            print(result[i],end='')
            n=n+1
    print('\n')
    if n==len(s):
        count=count-1

    if(list(s)==result):
        print("Successsssss")
        break

if count==0:
    print('loseeeeee')

