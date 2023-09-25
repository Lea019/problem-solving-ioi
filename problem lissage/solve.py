
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





    


def parse_input():
    nb_mesures  = int(input())
    diff_max = float(input())
    problem = {
        'nb_mesures': nb_mesures,
        'diff_max': diff_max,
        'nb_lissage': 0,
        'liste': [],
    }
    for i in range(problem['nb_mesures']):
        problem['liste'].append(float(input()))
    return problem

def solve(problem):
    liste = problem['liste']
    diff = check(liste)
    while diff > problem['diff_max']:
        liste = lissage(liste)
        problem['nb_lissage'] += 1
        diff = check(liste)
    return problem['nb_lissage']

def check(liste):
    diff_max = 0
    for i in range(len(liste) - 1):
        diff = abs(liste[i] - liste[i + 1]) 
        if diff > diff_max:
            diff_max = diff
    return diff_max
            
    
    
def output(result):
    print(result)
    
def lissage(liste):
    result = []
    result.append(liste[0])
    for i in range(len(liste) - 2):
        result.append((liste[i] + liste[i + 2]) / 2)
    result.append(liste[-1])
    return result         



problem = parse_input()
result = solve(problem)
output(result)