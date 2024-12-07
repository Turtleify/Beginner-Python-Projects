correct = 0

def checkq1():
    q1 = input('What is the capital of France? (a. Paris  b. London  c. Washington DC  d. Tokyo ) ')
    global correct
    if q1 == 'a':
        correct += 1
        print("That's right!")
    else:
        print('Wrong')

def checkq2():
    q2 = input('Which one of these is a food? (a. Laptop  b. The Sun  c. Steak  d. German )')
    global correct
    if q2 == 'c':
        correct += 1
        print("That's right!")
    else:
        print('Wrong')

def checkq3():
    q3 = input('What is the main language in the United States? (a. Spanish  b. Mandarin  c. Italian  d. English )')
    global correct
    if q3 == 'd':
        correct += 1
        print("That's right!")
    else:
        print('Wrong')

def quiz():
    while True:
        checkq1()
        checkq2()
        checkq3()
        print('You got ' + str(correct) + '/3 answers correct.')
        break

quiz()