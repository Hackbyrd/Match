Run Match Algorithm:
>> python match.py

Run Match Algorithm excluding 1 or more people:
>> python match.py exclude [email] [email] [email] ...
Example: python match.py exclude jonathan@fiscalnote.com tim@fiscalnote.com gerald@fiscalnote.com
python match.py exclude jacqueline@fiscalnote.com earl@fiscalnote.com rebekah@fiscalnote.com brian@fiscalnote.com

Run Customized Matches must be even amount of arguments.
>> python match.py custom jonathan@fiscalnote.com tim@fiscalnote.com earl@fiscalnote.com john@fisacalnote.com
matches jonathan<->tim and earl<->john

Run Match where people are not matched with their team
>> python match.py weight [integer]
Example: python match.py weight 7
This will increase weight between same team members by 7

When adding more people, first do a negative weight to remove weight, then add new members and then add weight again...
1. python match.py weight -7
2. Add new team members to group.txt and team.txt
3. python match.py weight 7
4. python match.py custom email email email

*Run Match with customized matches and a list of excludes

Find Individual Statistics:
>> python match.py stats [email]
Example: python match.py stats jonathan@fiscalnote.com tim@fiscalnote.com gerald@fiscalnote.com

Reset Table:
>> python match.py reset
>> python match.py clear

NYC:
craig@fiscalnote.com
kandel@fiscalnote.com
thomas@fiscalnote.com

Korea:
rebekah@fiscalnote.com

Intern/Part-Time:
jacqueline@fiscalnote.com
kris@fiscalnote.com
grant@fiscalnote.com
tony@fiscalnote.com

Remote:
brian@fiscalnote.com

python match.py exclude jacqueline@fiscalnote.com kris@fiscalnote.com rebekah@fiscalnote.com brian@fiscalnote.com kandel@fiscalnote.com tom@fiscalnote.com
