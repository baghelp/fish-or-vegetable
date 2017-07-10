#!/usr/bin/python

# Give a man a fish, feed him for a day, give a man a vegetable, and he might
# think it's a fish
# Author: baghelp <ankmike5@gmail.com>
# Is it a game, or a way of life?

from random import randint
import os

lists = ["fish.txt", "vegetable.txt"]
correct = ["you're correct!", "All you do is win", "100 percent",
"so much winning that I'm bored with winning."]
wrong = ["you're wrong!", "You need to win more!", "WRONG!"]
stupid = ["you're stupid!", "YOU\'RE TEARING ME APART, LISA!!!",
"Oh, hi mark", "wat", "fam, pls",
"I have some really great -- and I mean, some of the very best --" +
" the very\nbest characters there ever were. but not v or f."]


foodGroup = randint(0,1)

print "selected list is " + lists[foodGroup]
f = open(lists[foodGroup], 'r')
numLines = f.readline()
#index = randint(1, numlines)
index = 2
print "index is " + str(index)
for i in range(1, index):
  f.readline()

veshetable = f.readline().split(",")[0]
answer = raw_input(veshetable.lower() + ": Fish or Vegetable???? (f/v)\n")
if answer == 'f':
  if foodGroup == 0:
    print(correct[randint(0,len(correct) - 1)] )
  else:
    print(wrong[randint(0,len(wrong) - 1)] )
elif answer == 'v':
  if foodGroup == 1:
    print(correct[randint(0,len(correct) - 1)] )
  else:
    print(wrong[randint(0,len(wrong) - 1)] )
else:
  print(stupid[randint(0,len(stupid) - 1)] )

