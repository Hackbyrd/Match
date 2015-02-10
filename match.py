# Author: Jonathan Chen
# Description: This program determines the best match between 2 or more team members for events! It will take into account the number of times a person has been matched with another person.
# Read from team.txt and matrix.txt
# Write to matrix.txt
# python 2.7.6

from random import randint  # to generate random ints
import sys                  # for reading and writing to files

# Read in all team members
# args:
#   filename -> name of file that has team members and emails (ex. team.txt)
# returns:
#   team     -> returns a mapping of team name to index and index to team name
def read_team(filename):

  team  = {}  # hash of team to index and index to team
  index = 0   # the index that matches the team name

  # open file passed in to read
  file = open(filename, 'r')

  # loop through each line of the file and read in name
  for line in file:
    line = line.strip(' \t\n\r')    # strip out whitespace and newline characters
    name = line[0:line.find("|")]   # get substring to extract name, ignoring email
    team[name] = index              # store name -> index
    team[index] = name              # store index -> name
    index = index + 1               # update index

  file.close() # close file
  return team # return mapping of team name to index and index to team name

# end read_team
# -----------------------------------------------------------------------------

# Read in all team member emails
# args:
#   filename -> name of file that has team members and emails (ex. team.txt)
# returns:
#   emails   -> returns a mapping of a member email to index and index to email
def read_emails(filename):

  emails  = {}  # hash of member email to index and index to member email
  index   = 0   # the index that matches the team name

  # open file passed in to read
  file = open(filename, 'r')

  # loop through each line of the file and read in name
  for line in file:
    line = line.strip(' \t\n\r')   # strip out whitespace and newline characters
    email = line[line.find("|") + 1:]  # get substring to extract email, ignoring email
    emails[email] = index            # store email -> index
    emails[index] = email            # store index -> email
    index = index + 1              # update index

  file.close()  # close file
  return emails # return mapping of member email to index and index to member email

# end read_emails
# -----------------------------------------------------------------------------

# read in all past data in terms of who has been matched with whom
# args:
#   filename -> name of file that stores all past matching data
#   team_dic -> the mapping of team name to index and index to team name
# returns:
#   matrix -> returns the matrix of past data and past matchings
def read_matrix(filename, team_dic):

  num_team = len(team_dic) / 2 # get the number of team members
  count = 0 # count number of lines read

  # set up matrix of matching history with default value of all zeros
  matrix = [[0 for x in range(num_team)] for x in range(num_team)]

  # open file passed in to read
  file = open(filename, 'r')

  # loop through each line of the file
  for line in file:
    numbers = line.split() # break line into parts
    num_count = 0          # number of columns counted

    # go through each number on this row and store number of matches
    for num in numbers:
      matrix[count][num_count] = int(num)
      num_count = num_count + 1

    count = count + 1

  file.close()  # close file
  return matrix # return the matrix of past data and past matchings

# end read_matrix
# -----------------------------------------------------------------------------

# updates current matrix of matchings with new changes
# args:
#   filename  -> name of file that stores all past matching data
#   matrix    -> the mapping of team name to index and index to team name
def update_matrix(filename, matrix):

  # open file passed in to read
  file = open(filename, 'w')

  # write matrix to file
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):

      # don't put space on first element of line
      if (col == 0):
        file.write(str(matrix[row][col]))
      else:
        file.write(" " + str(matrix[row][col]))

    file.write("\n") # put newline

  file.close() # close file

# end update_matrix
# -----------------------------------------------------------------------------

# creates a matching of of all members to another member
# args:
#   team    -> mapping of team name to index and index to team name
#   matrix  -> matrix of past data and past matchings
# returns:
#   match_str -> string of all matches
def find_match(team, matrix):
  stack   = []    # create stack of team members' indices
  least   = 0     # smallest number of matches
  passed  = 0     # number of elements passed with the same least number of matches
  match_str = ""  # a string of all the matches

  # push everyone's index on stack
  for i in range(0, len(matrix)):
    stack.append(i)

  # if odd number of members
  if len(stack) % 2 == 1:
    temp = -1 # the person who will not be matched

    # go through each number that is left
    for num in stack:

      # if first element, update temp
      if temp == -1:
        temp = num

      # check if value is smaller than least
      if matrix[num][num] < least:
        least = matrix[num][num]
        temp = num
        passed = 0

      # check if value is equals to least
      elif matrix[num][num] == least:
        passed = passed + 1         # update number of elements passed to calculate probability of changing value
        random = randint(1, passed) # generate random integer between 1 and the number of passed elements with the same value as least

        # if random is 1, update temp
        if random == 1:
          temp = num

    # update string and count
    match_str = match_str + team[temp] + " <--> " + team[temp] + "\n"
    matrix[temp][temp] = matrix[temp][temp] + 1 # update match count
    stack.remove(temp) # remove temp from list

  # reset variables
  least = 0
  passed = 0

  # do pair-wise matches
  while(len(stack) > 0):
    rand_idx = randint(0, len(stack) - 1) # select a random index to remove
    temp = stack[rand_idx]                # get random index
    stack.remove(temp)                    # remove element
    match = -1                            # match is the match between temp and it's partner

    # go through each number that is left
    for num in stack:

      # if first element, force a match and update least
      if match == -1:
        match = num
        least = matrix[temp][num]

      # if the current element is less than the least, update match and least
      elif matrix[temp][num] < least:
        least = matrix[temp][num]
        match = num
        passed = 0 # reset passed if found lower value

      # if it is equal, than randomly change with equal probably to this current element or not
      elif matrix[temp][num] == least:
        passed = passed + 1         # update number of elements passed to calculate probability of changing value
        random = randint(1, passed) # generate random integer between 1 and the number of passed elements with the same value as least

        # if random is 1, update match
        if random == 1:
          match = num

    stack.remove(match) # remove the match from the stack
    matrix[temp][match] = matrix[temp][match] + 1 # update match count
    matrix[match][temp] = matrix[match][temp] + 1 # update match count
    match_str = match_str + team[temp] + " <---> " + team[match] + "\n" # update string of matches

  return match_str # return the string of matches

# end find_match
# -----------------------------------------------------------------------------

# return the stats for one member
# args:
#   member  -> index of member to find stats for
#   team    -> mapping of team name to index and index to team name
#   matrix  -> matrix of past data and past matchings
# returns:
#   stats   -> a string that shows the stats for this person
def match_stats(member, team, matrix):

  # match statistics sentence
  stats = "Match Statistics: " + team[member] + "\n" + str(matrix[member][member]) + " " + team[member] + " (You)\n"

  # loop through to get stats, skip yourself
  for i in range(0, len(matrix[member])):

    # if not yourself
    if member != i:
      stats = stats + str(matrix[member][i]) + " " + team[i] + "\n"

  return stats + "------------------------------\n"

# end match_stats
# -----------------------------------------------------------------------------

# main method
def main(argv):

  # read in all information
  team = read_team("team.txt")
  emails = read_emails("team.txt")
  matrix = read_matrix("matrix.txt", team)

  # if no arguments, find matches
  if len(argv) == 1:
    print find_match(team, matrix),

  # if one argument, should be an email, get stats for that person
  elif len(argv) == 2:
    if argv[1] in emails:
      print match_stats(emails[argv[1]], team, matrix),
    else:
      print "Email does not exist!",
      sys.exit()

  # update matrix
  update_matrix("matrix.txt", matrix)

# end main
# -----------------------------------------------------------------------------

main(sys.argv) # run full program!
