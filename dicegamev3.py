# This game was taken from one of COMP10001's assignment,
# but I've made it 400% better recently to be fair.
# I know, this program is very complex to debug
# I may not be able to see all of the problems to happen
# Added more fileIO things to the code

from ast import Break
import random
import time
import os

#function to check prime number
def isPrime(number):
    if number >= 2:
        for y in range(2, number):
            if not (number % y): return False
    else:
        return False
    return True

#fuction to calculate score
def pointsCalc(diRolls):
    plyrScorePlus = 0
    print('')
    if (diRolls[0] + diRolls[1] + diRolls[2] + diRolls[3] + diRolls[4]) % 5 == 0:
        print('All dice adds up to a number divisible by 5! (+10)')
        plyrScorePlus += 10
    if isPrime(sum(diRolls)) == True: #uses a prime determining funtion defined above, Googled
        print('All dice adds up to a prime number! (+40)')
        plyrScorePlus += 40
    if diRolls[0] == diRolls[1] == diRolls[2] == diRolls[3] == diRolls[4]:
        print('All 5 dice rolls are the same value! (+80)')
        plyrScorePlus += 80
    elif diRolls.count(diRolls[0]) > 2 or diRolls.count(diRolls[1]) > 2 or diRolls.count(diRolls[2]) > 2:
        print('Minimum of 3 dies are the same value! (+30)') #3 compares are enough to know if min of 3 dies do have the same value
        plyrScorePlus += 30
    elif diRolls.count(diRolls[0]) > 1 or diRolls.count(diRolls[1]) > 1 or diRolls.count(diRolls[2]) > 1 or diRolls.count(diRolls[3]) > 1:
        print('Minimum of 2 dies are the same value! (+20)') #4 compares are enough to know if min of 3 dies do have the same value
        plyrScorePlus += 20
    else:
        print('All 5 dices are different! (+50)')
        plyrScorePlus += 50
    return plyrScorePlus

#shorten random, default highest dice count is 6
di_max = 6
def di():
    return random.randint(1, di_max)

#permenent variable initialize
playerScore = turn = 0
pCountDown = 3

#register
fst_name = str(input('''----------------Welcome to the dice game----------------\n
This game has 5 runs, each round will roll a dice for 5 times;
If numbers add up to a prime number, you'll gain 40 points;
If all 5 numbers rolled are the same, you'll gain 80 points;
If all 5 numbers rolled are different, you'll gain 50 points
If 4 numbers rolled are the same, you'll gain 30 points;
If 5 numbers adds up to be divisible by 5, you'll gain 10 points;
You have the option to reroll each of the dice number for 3 times.
What\'s your first name: ''')) #Input first name only

while fst_name.isalpha() == False: #Reject non alphabet player name
    fst_name = str(input('\nSorry \''+fst_name+'\', please input alphabets only: '))

fst_name = fst_name[0].upper() + fst_name[1:len(fst_name)].lower() #String processing to setup naming

#New feature: change the highest dice roll possible before playing
alt_di_max = str(input('\nEnter y to alter the highest dice count can be rolled\nDefault=6, higher is harder. Or press Enter to skip. (y/Enter): '))

while alt_di_max != 'y': #Reject false input: not 'y', not ''
    if alt_di_max == '': break #Because no input means default, the loop will be skipped

    alt_di_max = str(input('\nSorry \''+fst_name+', if you want to alter highest dice count, please input y, or press Enter to skip: '))

if alt_di_max  == 'y' : #Optimization: because default is set to 6, judgement of == 'n' is no longer needed
    di_max = str(input('\nPlease enter the highest dice number (integer larger than 1 only): '))

    while di_max.isdigit() == False: #Prevent program from crashing when NaN gets entered
        di_max = str(input('\nSorry \''+fst_name+', please input integer value larger than 1 only: '))

    di_max = int(di_max) #Convert to integer when we make sure input value is acceptable

    while di_max <= 1: #We can't use '>' for strings, therefore a 2nd while is needed
        di_max += 1 #Instead of asking user to input with risk of NaN gets entered again, just make it work  
        print('Highest dice count is < 1, adding 1 to this value...')

print('\nThank you '+fst_name+', you starts off with 0 points and a dice with 0~'+str(di_max)+'. Let\'s play.')

#Prerequesities ends here
#Game starts here
while turn < 5:
    diRolls = [di(),di(),di(),di(),di()]
    diReads = [str(i) for i in diRolls]
    print('\nTurn ' + str(turn+1) + ' :\nYou\'ve rolled 5 dice. Their values are ' + ', '.join(diReads) + '. ')
    drrPhase = 0 #This value is for counting how much die re-roll phases
    pCountDown = 3
    while drrPhase < 3 or pCountDown == '!': #the exclaimation is to continue a turn when out of phase, for score calculation purposes
        drrUsed = False

        if pCountDown != '!' and pCountDown > 0:
            score_reRoll = str(input('\nDo you want to (s)core the points? This will end a turn;\nOr do you want to (r)eroll some dices? You have '+str(pCountDown)+' chances left (s/r): ')).lower()

        if score_reRoll == 's' or pCountDown == '!': #Enter scoring processing and end this turn
            playerScore += pointsCalc(diRolls)
            print('Your total points are '+str(playerScore)+'.')
            break
        
        elif pCountDown > 0 and score_reRoll == 'r': #Enter re-roll processing
            drrPhase += 1
            pCountDown -= 1
            for drr in range(0, 5):
                if str(input('Reroll die '+str(drr+1)+'? (y/n) ')).lower() == 'y': #it actually starts from die 0
                    diRolls[drr] = di()
                    print(diRolls[drr]) #show new die value
                    drrUsed = True
                else:
                    print('-') #show a line, corresponds to show new die value
                diReads = [str(i) for i in diRolls]
            print('You\'ve rerolled some dice and their current values are ' + ', '.join(diReads)+'.')

            if drrPhase == 3: #prevent early skip that makes a turn end before player score is registered
                drrPhase = 3
                pCountDown = '!'

            else:
                if drrUsed == False:
                    print('ERROR: Actually, you didn\'t re-roll any dice, restoring you re-roll chances.\n')
                    drrPhase -= 1
                print('You have rerolled '+str(drrPhase)+' times so far. ')

        else:
            print('ERROR: You choosed neither s OR r, or you are out of chances. Please retry.\n')
    turn += 1

print('\nThank you for playing! Game Over. '+fst_name+' has got '+str(playerScore)+' points!')

# Game finishes
# File export starts here
Lin_or_Win = 'L'
if os.name == 'nt': Lin_or_Win = 'W' #Detect OS type

exp_path = 'TBD' #If Desktop folder is not present, ask user where to write file later
if Lin_or_Win == 'L' and os.path.exists(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')) == True:
        exp_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') #Linux FileIO

if Lin_or_Win == 'W' and os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))  == True:
    exp_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #Windows FileIO

file_exp_flag = str(input('''\nStarting another round will clear all data,
Do you want to store your score (Default at Desktop folder)? (y)
Or store in a different location (c):
Or press Enter to skip (Enter)''')) #File IO master swtich

while file_exp_flag != 'y' or file_exp_flag != 'c' or file_exp_flag != '': #Reject non alphabet input
    file_exp_flag = str(input('\nSorry \' '+fst_name+'\', please input y for store scores on Desktop, c for change directory, or Enter to skip: '))

if file_exp_flag == 'c': #1st posibility of path change --- user specification
    exp_path = str(input('''\nPlease specify your file export location without filename.
    Windows format: "X:\\path\\to\\folder";
    Linux format: "/home/usr/path/to/folder/": '''))

    if Lin_or_Win == 'L':
       print('Operating system is Linux.')
       while os.path.exists(exp_path) == False:
           exp_path = str(input('Sorry \' '+fst_name+'\', please enter an existing path like "/home/usr/path/to/folder/" : '))
    else:
       print('Operating system is Windows.')
       while os.path.exists(exp_path) == False:
           exp_path = str(input('Sorry \' '+fst_name+'\', please enter an exising path like "X:\\path\\to\\folder": '))

    file_exp_flag = 'y' #Export path gained, changing file export flag for later elif use
        
if file_exp_flag == 'y' and exp_path == 'TBD': #2nd posibility of path change --- desktop not found
    exp_path = str(input('''\nDesktop folder was not found.
    Please specify your file export location.
    Windows format: "X:\\path\\to\\folder";
    Linux format: "/home/usr/path/to/folder/": '''))

    if Lin_or_Win == 'L':
       print('Operating system is Linux.')
       while os.path.exists(exp_path) == False:
           exp_path = str(input('Sorry \' '+fst_name+'\', please enter an existing path like "/home/usr/path/to/folder/" : '))
    else:
       print('Operating system is Windows.')
       while os.path.exists(exp_path) == False:
           exp_path = str(input('Sorry \' '+fst_name+'\', please enter an exising path like "X:\\path\\to\\folder": '))

elif file_exp_flag == 'y' and exp_path != 'TBD': #Time to write file
    timestr = time.strftime("%Y%m%d-%H%M%S")
    full_exp_path = exp_path+'\\dicegame_run'+timestr+'.txt' #create new file whenever a second passes

    files=open(full_exp_path, mode='a')
    files.write(fst_name+' has got '+str(playerScore)+' points! Highest dice count is '+str(di_max))
    files.close()

#when file_exp_flag == '', nothing will happen as it 'skips'