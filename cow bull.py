import random
print("WELCOME! TO IN COW-BULL GAME")
name=input("ENTER HERE PLAYER NAME:")
print("WELCOME!",name)
def game():
    number=random.sample([0,1,2,3,4,5,6,7,8,9],4)
    print("--BEST OF LUCK--")
    cow=[]
    bull=[]
    for i in range(5):
        if bull==number:
                print("HURRAH! YOU ARE WINNER")
                play=input("DO YOU WANT TO PLAY AGAIN 'Y' OR 'N'")
                if play=='Y':
                    game()
                if play=='N':
                    print("THANK FOR PLAY THIS GAME")
                    break
        guess_number=int(input("Enter Your Guess Number:"))
        guess_position=int(input("Enter Your Guess Postion:"))
        for i in number:
            
            if guess_number in number:
                if guess_number in number and number.index(guess_number)==guess_position:
                    bull.insert(guess_position,guess_number)
                    print("Bull:",bull)
                    break
                else:
                    cow.insert(guess_position,guess_number)
                    print("Cow:",cow)
                    break
            else:
                print("Your number is not Exist in secret list!!")
                break
    else:
        print("SORRY! YOUR CHANCE IS FINISHED")            
game()



*cowbull
