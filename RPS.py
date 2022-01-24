import random
import webbrowser
R = 'Rock'
P = 'Paper'
S = 'scissor'
# by abdullah :)




gamerlol = input("choose,  (s)cissor, (p)aper, (r)ock   ")

if(gamerlol == 'r'):
   
    print("player chose Rock")
elif(gamerlol == 'p'):
    
    print("player chose Paper")
elif(gamerlol == 's'):

    print("player chose Scissor")
elif(gamerlol == ""):
    print("this is not NASA Government agency, dont leave it the space empty!")
    exit()
elif(gamerlol == "R"):
    webbrowser.open('https://www.google.com/search?q=is+python+case+sensitive')
    exit()
elif(gamerlol == "S"):
    webbrowser.open('https://www.google.com/search?q=is+python+case+sensitive')
    exit()
elif(gamerlol == "P"):
    webbrowser.open('https://www.google.com/search?q=is+python+case+sensitive')
    exit()
else:
    print("sorry but we do not have "+gamerlol+" here" )
    exit()

ps = random.randint(1,3)

if ps == (1): # rock
    pc = 'r'
    print("the computer chose "+R)


elif ps == 2: # paper
    pc = 'p'
    print("the computer chose "+P)
else: # Scissor
    pc = 's'
    print("the computer chose "+S)


if (gamerlol == pc):
    print(" DRAW")
elif gamerlol == 'p' and pc == 'r':
    print(" player win")
elif gamerlol == 'p' and pc == 's':
    print(" pc win")
elif gamerlol == 'r' and pc == 's':
    print(" player win")
elif gamerlol == 'r' and pc == 'p':
    print(" pc win")
elif gamerlol == 's' and pc == 'p':
    print(" player win")
elif gamerlol == 's' and pc == 'r':
    print(" pc win")
