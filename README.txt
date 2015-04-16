Run Match Algorithm:
>> python match.py

Run Match Algorithm excluding 1 or more people:
>> python match.py exclude [email] [email] [email] ...
Example: python match.py exclude jonathan@fiscalnote.com tim@fiscalnote.com gerald@fiscalnote.com

*Run Customized Matches must be even amount of arguments.
>> python match.py custom jonathan@fiscalnote.com tim@fiscalnote.com earl@fiscalnote.com john@fisacalnote.com
matches jonathan<->tim and earl<->john

*Run Match where people are not matched with their team
>> python match.py weight

Find Individual Statistics:
>> python match.py stats [email]
Example: python match.py stats jonathan@fiscalnote.com tim@fiscalnote.com gerald@fiscalnote.com

Reset Table:
>> python match.py reset
>> python match.py clear

