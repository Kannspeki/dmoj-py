import math, sys


def wc16c1j1():
    s = int(input())
    print('sp' + 'o'*s + 'ky')

#wc16c1j1()    

def wc15c2j1():
    s = int(input())
    output=('A long time ago in a galaxy ' + 'far, '*s +  'away...')
    print(output.replace('far, away...', 'far away...'))


#wc15c2j1()    


def ccc13j1():
    y = int(input())
    m = int(input())
    print((m - y) + m)

#ccc13j1()    

def wc17c1j2():
    f = float(sys.stdin.readline())
    print(round((f * (9/5)) + 32))

#wc17c1j2()

def wc18c3j1():
    p = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    d = int(sys.stdin.readline())
    print(d * (p//b) + p % b)

#wc18c3j1()

def ccc19j1():
    a3 = int(sys.stdin.readline())
    a2 = int(sys.stdin.readline())
    a1 = int(sys.stdin.readline())
    b3 = int(sys.stdin.readline())
    b2 = int(sys.stdin.readline())
    b1 = int(sys.stdin.readline())
    a = (a3*3) + (a2*2) + (a1)
    #print(a)
    b = (b3*3) + (b2*2) + (b1)
    #print(b)
    if a > b:
        print('A')
    if b > a:
        print('B')
    else:
        print('T')


#ccc19j1() 

def cc18j1():
    telemarketer = 0
    n1 = int(sys.stdin.readline())
    n2 = int(sys.stdin.readline())
    n3 = int(sys.stdin.readline())
    n4 = int(sys.stdin.readline())

    if n1 == 8 or n1 == 9:
        telemarketer +=1
    if n2 == n3:
        telemarketer +=1
    if n4 == 8 or n4 == 9:
        telemarketer +=1
    if telemarketer == 3:
        print('ignore')
    else:
        print('answer')
        
#cc18j1()

def ccc06j1():
    calories = 0
    b = int(sys.stdin.readline())
    if b == 1:
        calories += 461
    if b == 2:
        calories += 431
    if b == 3:
        calories += 420
    s = int(sys.stdin.readline())
    if s == 1:
        calories += 100
    if s == 2:
        calories += 57
    if s == 3:
        calories += 70   
    d = int(sys.stdin.readline())
    if d == 1:
        calories += 130
    if d == 2:
        calories += 160
    if d == 3:
        calories += 118   
    de = int(sys.stdin.readline())
    if de == 1:
        calories += 167
    if de == 2:
        calories += 266
    if de == 3:
        calories += 75   
    print(f'Your total Calorie count is {calories}.')

#ccc06j1()


def ccc15j1():
    month = int(sys.stdin.readline())
    day = int(sys.stdin.readline())
    if month == 2 and day == 18:
        print('Special')
   
    elif month == 2:
        if day < 18:
            print('Before')
        if day > 18:    
            print('After')
        
    elif month > 2:
        print('After')
    elif month < 2:
        print('Before')

#ccc15j1()


def ccc15j2():
    usrInput = (sys.stdin.readline())
    sadNum = usrInput.count(':-(')
    hapNum = usrInput.count(':-)')

    if sadNum > hapNum:
        print('sad')
    elif hapNum > sadNum:
        print('happy')
    elif hapNum == 0 or sadNum == 0:
        print('none')
    elif hapNum == sadNum and hapNum > 0 and sadNum > 0:    
        print('unsure')

#ccc15j2()


def dmopc16c1p0():

    width = int(sys.stdin.readline())
    cheese = int(sys.stdin.readline())

    if width == 3 and cheese >= 95:
        print('C.C. is absolutely satisfied with her pizza.')
        sys.exit()

    if width == 1 and cheese < 51:
        print('C.C. is fairly satisfied with her pizza.')
        sys.exit()
    else:
        print('C.C. is very satisfied with her pizza.')
        sys.exit()
#dmopc16c1p0()


def ccc07j1():
    middle = [0]
    bowl1 = int(sys.stdin.readline())
    middle.append(bowl1)

    bowl2 = int(sys.stdin.readline())
    middle.append(bowl2)

    bowl3 = int(sys.stdin.readline())
    middle.append(bowl3)

    middle.sort()
    median = round((3 + 1)/2) 
    print(middle[median])


#ccc07j1()


