print("Number Guessing Game")
a=5
while(a>0) : 
    num = int(input("Enter a number from 1-9 : "))
    if(num < 6) : 
        print("Your guess is too small ")
        print("Guess a number greater than")
        print(num)
    elif(num < 9) : 
        print("You are close")
        print("Guess a number greater than")
        print(num)
    else :
        print("You chose the perfect number ")
        print("You win!! Congratulations!!")
        break
    a = a-1