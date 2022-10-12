# Python Dicegame

A python game to see who wins the highest score.<br>

This game has 5 rounds, each round will roll a dice for 5 times;<br>
If numbers rolled adds up to a prime number, the player will gain 40 points;<br>
If all 5 numbers rolled are the same, the player will gain 80 points;<br>
If all 5 numbers rolled are different, the player will you'll gain 50 points<br>
If 4 numbers rolled are the same, the player will gain 30 points;<br>
If 5 numbers adds up to be divisible by 5, the player will gain 10 points;<br>
The player has the option to reroll each of the dice number for 3 times.

 - This program was a hell of a coding, but have fun!

### How to play

 - For any PC with Python installed, simply right click --> open/Edit with --> Python/IDLE
 - For a portable Python environment, simply issue command line: X:/PythonXX/python.exe "x:/folder/dicegamev4.py"

### Versions:

**V1**:
 - Initial simple "working" code developed since COMP10001
 - The name string processing works
 - The isPrime function was created
 - The function random was used
 - The di() function -- a shortcut to roll dice was created
 - Python list to include dice rolls was created

**V2**:
 - Added more conditions to gain scores
 - Expanded introduction text to include all the point-gaining conditions
 - Optimizaiton on some if statements
 - Adjusted points for each condition to reduce luck influences
 - while loop check of valid username was created

**V3**:
 - Adjusted all the variables to better separate from comments and interaction with players
 - Introduced di_max parameter to adjust the highest number can a dice roll
 - while loop check of di_max was created
 - "else elimination" processing optimization was further adopted

**V4**:
 - Import time, os was used for FileIO
 - Advanced while loop (with if-break combination) was used when both while-or; while-and are not suitable
 - FileIO procesing was created to save score results, with os.path.join, os.environ[], os.path.exists, os.path.expanduser
 - while loop check of valid file path was created
 - Lin_or_Win processing with os.name was created to support Linux and Windows FileIO
 - time.strftime("%Y%m%d-%H%M%S") was added to filename for file separation
 - Example path was shown in user interaction to make user input of file saving path right
 - Default save to Desktop for both Windows and Linux OS

**V5**:
 - Being forced to turn this code into module
 - forced di() function to take parameter di_max due to functions don't take others' params, which is less elegant
 - User interaction is better thanks to indents created by functions
