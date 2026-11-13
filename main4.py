import random
attempts=[]

def show():
    if len (attempts)<=0:
       print("Currently no high score.")
    else:
        print("The current highest score is {} attempts".format(min(attempts)))

def start():
    random_number=int(random.randint(1,10))
    print("Welcome to the quiz game!!!")
    name=input("Enter your name:")
    play=input("Hi, {} , would you like to play the quiz game?(Enter yes/no)".format(name))
    a=0
    show()
    while play.lower()=="yes":
        try:
            guess=input("what is 1 + 1? (Enter a number between 1 and 10):")
            if int(guess)<1 or int(guess)>10:
                raise ValueError("please guess number within valid range.")

            if int(guess)==2:
                print("Congrats you got it right!")
                a=a+1
                attempts.append(a)
                print("No of attempts={}".format(a))
                break
            elif int(guess)<random_number:
                print("Its lower.")
                a=a+1
            elif int(guess)>random_number:
                print("Its higher.")
                a=a+1
            play=input("Hi, {} , would you like to play  another round of the quiz game?(Enter yes/no)".format(name))
            a=0
            show()
            while play.lower()=="yes":
                guess=input("what is 2+2? (Enter a number between 1 and 10):")
                if int(guess)<1 or int(guess)>10:
                    raise ValueError("please guess number within valid range.")
                if int(guess)==4:
                    print("Congrats you got it right!")
                    a=a+1
                    attempts.append(a)
                    print("No of attempts={}".format(a))
                    break
                elif int(guess)<random_number:
                    print("Its lower.")
                    a=a+1
                elif int(guess)>random_number:
                    print("Its higher.")
                    a=a+1
        except ValueError as err:
            print("Try again....")
            print("({})".format(err))
        
        print("ok goodbye!")
if __name__=="__main__":
    start()