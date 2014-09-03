from random import randint

def main():
    print "Welcome to the number guessing game!"
    number=randint(1,10)
    i=1
    while True:
        if i>5:
            break
        guess=raw_input("Try #" + str(i) + ": Guess a number between one and ten: ")
        if int(guess)==number:
            print "You got it!"
            break
        else:
            print "That's incorrect."
            i+=1


if __name__=='__main__':
    main()
