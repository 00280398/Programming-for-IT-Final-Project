#Nick Wunderlich
#Programming for IT Final Project
#Multiplication Test and Study Guide

import random
import time

score = 0
currenttime = time.asctime( time.localtime(time.time()) )
def test():
    global score
    rand1 = randint(1, 20)
    rand2 = randint(1, 20)
    print('Hello and welcome to this multiplication test and study guide!')
    que = input('Would you like to (s)tudy, take the (t)est, or (v)iew grades?')
    if que = ('s'):
        num = int(input('Which table would you like to view? (1-20)'))
        for i range(1, 20):
            print(num, 'x', i, '=', num * i)
    elif que = ('t'):
        name = input('Please enter your name')
        for i in range(20)
            question = int(input('What is ' + rand1 + '*' + rand2 + '?')
            answer = rand1 * rand2
            if question == answer:
                score = score + 1
        print('Your score was ' + str(score) + 'out of 20.')
        doc = open('grades.txt')
        doc.write(score + name + currenttime)
        doc.close()
    elif que = ('v'):
        doc()
        doc.read()
        doc.close()
        