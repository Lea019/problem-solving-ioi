
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
    Problem = {
        'nb_mesures': nb_mesures,
        'diff_max': diff_max,
        'nb_lissage': 0,
        'liste': [],
    }
    for i in range(Problem['nb_mesures']):
        Problem['liste'].append(float(input()))
    return Problem

def solve(Problem):
    for i in range(Problem['nb_mesures'] - 1):
        if abs(Problem['liste'][i] - Problem['liste'][i + 1]) <= Problem['diff_max']:
            Problem['nb_lissage'] -= 1
            return Problem['nb_lissage']
       
    lissage(Problem)


    
    
def output(result):
    print(result)
    
def lissage(problem):
    result = []
    result.append(Problem['liste'][0])
    for i in range(Problem['nb_mesures'] - 2):
        result.append((Problem['liste'][i] + Problem['liste'][i + 2]) / 2)
    result.append(Problem['liste'][-1])
    Problem['liste'] = result
    Problem['nb_lissage'] += 1
    return Problem         



problem = parse_input()
result = solve(problem)
output(result)