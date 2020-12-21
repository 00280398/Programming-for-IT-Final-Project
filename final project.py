#Nick Wunderlich
#Programming for IT Final Project
#Multiplication Test and Study Guide

import random
import time
import re

score = 0
currenttime = time.asctime( time.localtime(time.time()) )
doc = open('grades.txt','w+')
def test():
    global score
    rand1 = random.randint(1, 20)
    rand2 = random.randint(1, 20)
    print('Hello and welcome to this multiplication test and study guide!')
    que = input('Would you like to (s)tudy, take the (t)est, or (v)iew grades?')
    if que == 's':
        num = int(input('Which table would you like to view? (1-20)'))
        for i in range(1, ):
            print(num, 'x', i, '=', num * i)
    if que == 't':
        name = str(input('Please enter your name'))
        for i in range(20):
            question = int(input('What is ' + rand1 + '*' + rand2 + '?'))
            answer = rand1 * rand2
            if question == answer:
                score = score + 1
        print('Your score was ' + str(score) + 'out of 20.')
        doc.write(score + name + currenttime)
        doc.close()
    if que == 'v':
        text = 'grades.txt'
        x = re.findall([0-20], text)
        print(x)

test()
input('Press ENTER to exit')