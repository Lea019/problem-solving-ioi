'''

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

'''

##################################################################
# read input from file tests/test1.in as if type on the keyboard
# This shouldn't run on France-IOI
# replace this with the name of your test file
test_file = 'test1.in'

import sys, os, platform
# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ('3', '11'):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################




    

nb_frog = int(input())
nb_tour = int(input())

if not(1 <= nb_frog <= 100) or \
   not(1 <= nb_tour <= 1000):
    quit()
    

prems_frog = [0]*nb_frog
avancee = [0]*nb_frog

def first_frog(avancee):
    premiere = max(avancee)
    i = avancee.count(premiere)
    if i == 1:
       return avancee.index(premiere)
    else: 
       return 0

for i in range(nb_tour):
    first = first_frog(avancee)
    if first != 0:
       prems_frog[first] += 1
    frog, depl = [int(x) for x in input().split(" ")]
    if not(1 <= depl <= 100):
        quit()
    avancee[frog - 1] += depl
    
print(prems_frog.index(max(prems_frog)) + 1)

