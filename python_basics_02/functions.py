# How to write a function
'''def function_name(arguments):
  print('My name is '+ arguments)
  
function_name('Hero')'''
  
#fibonacci series
#0,1,1,2,3,5
'''def fibonacci(n):
    if n==0:
        return 0
    else:
        x=0
        y=1
        print(x,end=",")
        print(y,end=",")
        for i in range(1,n):
            z=x+y
            x=y
            y=z
            print(z,end=',')
fibonacci(8)'''

#Guess the number
import random as r
secret_num = r.randint(1,10)
flag = False

def game_guess_number(guessed_num, secret_num):
    if guessed_num<secret_num:
        return 'Too Low'
    elif guessed_num>secret_num:
        return 'Too High'
    else:
        return "Correct" 

for i in range(1,6):
    print("Take a guess. You have "+str(6-i)+" guesses left.")
    guess=input()
    if game_guess_number(int(guess),secret_num)=="Correct":
        print('YOU HAVE WON THE GAME!!!')
        flag=True
        break

if not flag:
    print("You Have Lost The Game")
    