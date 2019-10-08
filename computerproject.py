#!/usr/bin/env python3
# -*- coding: utf-8

n = input("Enter NAME of PLAYER:")
no = int(input("Enter number of overs(NO baby overs):"))
print("The game has been set for",no,"overs",end = '\n\n')
b = no * 6
#TOSS
print('\t\t',"TOSS",end = '\n\n')
print("INPUT:","H : Heads","T : Tails",sep = '\n')
c = input("YOUR CALL (H or T):")
print()
if c not in ('H','T'):
    while True:
        print("Invalid call")
        c = input("Call out a VALID option(H or T):")
        if c in ('H','T'):
            break   
if c == 'H':
    ch = 1
elif c == 'T':
    ch = 0
import random
m = random.randint(0,1)
if ch == m :
    print('\t',"You won the Toss")
    print("Enter:","1 to BAT","2 to BOWL",sep = '\n')
    cho = int(input("Choose to bat or bowl? "))
    if cho not in (1,2):
        while True:
            print("Invalid choice")
            cho = input("Choose a VALID option(1 or 2):")
            if cho in (1,2):
                break 
    if cho == 1:
        print("You chose to BAT",end = '\n\n')
        print('\t\t',"GAME BEGINS",end = '\n\n')
        print('\t\t',"First Innings",end = '\n\n')
        print("BATTING:",n)
        print("BOWLING:","Computer")
        print("OVERS:",no,end = '\n\n')
        s1 = 0
        s2 = 0
        i = 1
        while i <= b : 
            x = int(input("Enter runs:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("You Are OUT")
                    break
                else:
                    s1 = s1 + x
                    nob = b - i
                    print("(score:",s1,";Balls left:",nob,")")
        print()
        print("Your SCORE:",s1,end = '\n\n')
        print('\t\t',"Second Innings",end = '\n\n')
        print("BATTING:","Computer")
        print("BOWLING:",n)
        print("OVERS:",no,end = '\n\n')
        print("TARGET score:",(s1+1))
        i = 1
        while i <= b : 
            x = int(input("Enter no:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("Computer is OUT")
                    break
                else:
                    s2 = s2 + y
                    nob = b - i
                    print("(comp. score:",s2,";Target:",(s1+1),";Balls left:",nob,")")
                    if s2 > s1:
                        break
        print()
        print("COMPUTER's SCORE:",s2,end = '\n\n')
        if s1 > s2:
            print("You WIN")
        elif s2 > s1 :
            print("You LOSE ,Better luck next time")
        else:
            print("Match draw")
    else:
        print("You chose to BOWL",end = '\n\n')
        print('\t\t',"GAME BEGINS",end = '\n\n')
        print('\t\t',"First Innings",end = '\n\n')
        print("BATTING:","Computer")
        print("BOWLING:",n)
        print("OVERS:",no,end = '\n\n')
        s1 = 0
        s2 = 0
        i = 1
        while i <= b : 
            x = int(input("Enter no:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("Computer is OUT")
                    break
                else:
                    s1 = s1 + y
                    nob = b - i
                    i = i + 1
                    print("(comp. score:",s1,";Balls left:",nob,")")
        print()
        print("Computer's SCORE:",s1,end = '\n\n')
        print('\t\t',"Second Innings",end = '\n\n')
        print("BATTING:",n)
        print("BOWLING:","Computer")
        print("OVERS:",no,end = '\n\n')
        print("TARGET SCORE:",s1+1)
        i = 1
        while i <= b : 
            x = int(input("Enter no:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("You are OUT")
                    break
                else:
                    s2 = s2 + x
                    nob = b - i
                    i = i + 1
                    print("(YOUR score:",s2,";Balls left:",nob,";Target:",s1+1,")")
                    if s2 > s1:
                        break
        print()
        print("Your SCORE:",s2,end = '\n\n')
        if s1 < s2:
            print("You WIN")
        elif s2 < s1 :
            print("You LOSE ,Better luck next time")
        else:
            print("Match draw")
else:
    print('\t',"You lost the TOSS",end = '\n\n')
    ch = random.randint(1,2)
    if ch == 1:
        print("Computer chose to BAT",end = '\n\n')
        print('\t\t',"GAME BEGINS",end = '\n\n')
        print('\t\t',"First Innings",end = '\n\n')
        print("BATTING:","Computer")
        print("BOWLING:",n)
        print("OVERS:",no,end = '\n\n')
        s1 = 0
        s2 = 0
        i = 1
        while i <= b : 
            x = int(input("Enter no:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("Computer is OUT")
                    break
                else:
                    s1 = s1 + y
                    nob = b - i
                    i = i + 1
                    print("(comp. score:",s1,";Balls left:",nob,")")
        print()
        print("Computer's SCORE:",s1,end = '\n\n')
        print('\t\t',"Second Innings",end = '\n\n')
        print("BATTING:",n)
        print("BOWLING:","Computer")
        print("OVERS:",no,end = '\n\n')
        print("TARGET SCORE:",s1+1)
        i = 1
        while i <= b : 
            x = int(input("Enter no:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("You are OUT")
                    break
                else:
                    s2 = s2 + x
                    nob = b - i
                    i = i + 1
                    print("(YOUR score:",s2,";Balls left:",nob,";Target:",s1+1,")")
                    if s2 > s1 :
                        break
        print()
        print("Your SCORE:",s2,end = '\n\n')
        if s1 < s2:
            print("You WIN")
        elif s2 < s1 :
            print("You LOSE ,Better luck next time")
        else:
            print("Match draw")
    else:
        print("Computer chose to BOWL",end = '\n\n')
        print('\t\t',"GAME BEGINS",end = '\n\n')
        print('\t\t',"First Innings",end = '\n\n')
        print("BATTING:",n)
        print("BOWLING:","Computer")
        print("OVERS:",no,end = '\n\n')
        s1 = 0
        s2 = 0
        i = 1
        while i <= b : 
            x = int(input("Enter runs:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("You Are OUT")
                    break
                else:
                    s1 = s1 + x
                    nob = b - i
                    i = i + 1
                    print("(score:",s1,";Balls left:",nob,")")
        print()
        print("Your SCORE:",s1,end = '\n\n')
        print('\t\t',"Second Innings",end = '\n\n')
        print("BATTING:","Computer")
        print("BOWLING:",n)
        print("OVERS:",no,end = '\n\n')
        print("TARGET score:",(s1+1))
        i = 1
        while i <= b : 
            x = int(input("Enter no:"))
            y = random.randint(0,6)
            if x > 6 or x < 0:
                print("Don't cheat")
                i = i
            else:
                print("Computer played:",y)
                if x == y :
                    print("Computer is OUT")
                    break
                else:
                    s2 = s2 + y
                    nob = b - i
                    print("(comp. score:",s2,";Target:",(s1+1),";Balls left:",nob,")")
                    i = i + 1
                    if s2 > s1 :
                        break
        print()
        print("COMPUTER's SCORE:",s2,end = '\n\n')
        if s1 > s2:
            print("You WIN")
        elif s2 > s1 :
            print("You LOSE ,Better luck next time")
        else:
            print("Match draw")
print('\t\t',"GAME ENDS")
