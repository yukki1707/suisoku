import random
import sys
import msvcrt

wish = True
a = 1
b = 5
number = random.randint (a, b)

def start():    
    global a, b
              
    print ('-- Guess the number from ' + str(a) +' to ' + str(b) + ' to WIN')
    print ('-- Press ENTER to star')
    print ('-- Press "r" to change range')
    print ('-- Press ESC to exit\n')
    
    key = msvcrt.getch()
    
    if ord(key) == ord('r'):
        setting()
    elif ord(key) == ord('\r'): # \r значение для ENTER в ASCII
        game()
    elif ord(key) == ord ('\x1b'): # \x1b - значние для Esc в ASCII 
        sys.exit ('-- Closing...')

def setting():
        sett = True
        global a, b
        while sett:
            try:
                a = int(input ('-- Your range from: '))
                b = int(input('-- To: '))
            except:
                print ('-- You have to enter a number\n-- Try again\n')
                continue
            if b < a:
                print ('-- The second number must be bigger than the first one\n-- Try again\n')
                setting()
                sett = False
            else:
                print ('-- Guess the number from ' + str(a) +' to ' + str(b) + ' to WIN')
                game()
                sett = False

def game():
    running = True   
    global a, b, number
    number = random.randint (a,b)
    while running:
        try:
            guess = int(input('-- Enter a number\n'))
        except ValueError:
            print ('-- You have to enter a NUMBER')
            print ('-- Try again\n')
            continue
        if guess == number:
            print ('-- YOU WIN!!!')
            running = False
        elif guess == 0:
            sys.exit('-- Closing...')
        elif guess > number:
            print ('-- Your number is bigger')
            print ('-- Try again\n')
        else:
            print ('-- Your number is less')
            print ('-- Try again\n')

start()

while wish:
    print ('-- To start new game press ENTER\n-- To change the range press "r"\n-- To exit press ESC\n')
    key = msvcrt.getch()
    if ord(key) == ord('\r'):
        game()
    elif ord(key) == ord('r'):
        setting()
    elif ord(key) == ord('\x1b'):
        wish = False
        sys.exit ('-- Closing...')

