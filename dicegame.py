#I, 000758631, certify that all code submitted is my own work;
#that I have not copied it from any else source, which is not a shotgun answer
#I also certify that I have not allowed my work to be copied by others.

import random
#function to check prime number
def isPrime(number):
    if number >= 2:
        for y in range(2, number):
            if not (number % y):
                return False
    else:
        return False
    return True

#fuction to calculate score
def pointsCalc(dices):
    P = 0
    print('')
    if isPrime(sum(dices)) == True: #+50 points, fuction connected to another function
        print('All dice adds up to a prime number! (+50)')
        P += 50
            
    if dices[0] == dices[1] == dices[2] == dices[3] == dices[4]: #+100 points
        print('All 5 dices with same value! (+100)')
        P += 100
    elif dices.count(dices[0]) > 2:
        print('Minimum of 3 dies has same value! (+30)')
        P += 30
    elif dices.count(dices[1]) > 2:
        print('Minimum of 3 dies has same value! (+30)')
        P += 30
    elif dices.count(dices[2]) > 2: #+30 points
        print('Minimum of 3 dies has same value! (+30)')
        P += 30
    else:
        print('All 5 dice are different, or 2 dice has same value! (+25)')
        P += 25 #+25 points, the table did not tell what to do if 2 dices has same value so I put it here
    return P

#shorten random
def di():
    return random.randint(1, 6)

#permenent variable initialize
points = turn = 0
pCountDown = 3

#register
player = str(input('''Welcome to the dice game, \n
This game has 5 runs, each round will roll a dice for 5 times.\n
If numbers add up to a prime, you will gain 10 points;\n
If all 5 numbers rolled per-round are different,\n
OR 2 numbers are euqal, you will gain 12 points;\n
If 4~5 numbers rolled are the same, you will gain 30points;\n
You always have the option to re-roll the dice.\n
\n\n
what is yout first name? ''')) #input name

while player.isalpha() == False: #ask to re-input name until correct
    player = str(input('\nSorry \''+player+'\', please input alphabets only: '))

player = player[0].upper() + player[1:len(player)].lower() #mod name

print('''\nThank you '+player+', you starts off with 0 points, let\'s play!\n\n

''')

#the game
while turn < 5:
    A = di()
    B = di()
    C = di()
    D = di()
    E = di()
    dices = [A,B,C,D,E]
    dieReads = [str(i) for i in dices]
    print('\nTurn ' + str(turn+1) + ' :\nYou\'ve rolled 5 dice. Their values are ' + ', '.join(dieReads) + '.\n ')
    phase = 0
    while phase < 3 or pCountDown == '!': #the exclaimation is to continue a turn when out of phase, for score perpouses

        if pCountDown != '!':
            score_reRoll = str(input('Do you want to score the points? (this will end a turn);\nOr do you want to reroll dices? ('+str(pCountDown)+' chances left) (s/r) ')).lower()

        if score_reRoll == 's' or pCountDown == '!':
            phase = 0
            pCountDown = 3
            points += pointsCalc(dices)
            print('Your total points are '+str(points)+'.')
            break

        elif pCountDown > 0:
            if score_reRoll == 'r':
                phase += 1
                pCountDown -= 1
                for d in range(0, 5):
                    if str(input('Reroll die '+str(d+1)+'? (y/n) ')).lower() == 'y': #it actually starts from die 0
                        dices[d] = di()
                        print(dices[d]) #show new die value
                    else:
                        print('-') #show a line, corresponds to show new die value
                    dieReads = [str(i) for i in dices]
                print('You\'ve rerolled some dice and their current values are ' + ', '.join(dieReads)+'.')

            if phase == 3: #prevent early skip that makes a turn end before output points
                phase = 2
                pCountDown = '!'
            

        else:
            print('You choosed neither, or you are out of chances. This phase will reastart.\n')
    turn += 1


print('\nThank you for playing! Game Over. '+player+' has got '+str(points)+' points!')
