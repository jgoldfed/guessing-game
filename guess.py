from random import randint

def main():
    print "Welcome to the number guessing game!"
    number=randint(1,10)
    while True:
        guess=raw_input("Guess a number between one and ten: ")
        if int(guess)==number:
            print "You got it!"
            break
        else:
            print "That's incorrect."


if __name__=='__main__':
    main()
