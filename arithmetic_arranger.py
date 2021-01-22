import re


def input_check(problems):
    # check if the problems are not too many
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # check that operators are + or -
    pattern1 = '\w+ \+ \w+'
    pattern2 = '\w+ \- \w+'
    for problem in problems:
        if (re.search(pattern1, problem) == None) and (re.search(
                pattern2, problem) == None):
            return "Error: Operator must be '+' or '-'."
    # check that operands are numbers
    for problem in problems:
        l = problem.split()
        if not l[0].isdigit() or not l[2].isdigit():
            return 'Error: Numbers must only contain digits.'
    # check that operands are not longer than 4 digits
    for problem in problems:
        l = problem.split()
        if len(l[0]) > 4 or len(l[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    return ''


def operation(first_op, second_op, operator):
    '''
	Takes two operands and returns their sum or
	difference according to operator
	'''
    if operator == '+':
        return first_op + second_op
    else:
        return first_op - second_op


def arithmetic_arranger(problems, include_results=False):

    # check that input is correct
    input_error = input_check(problems)
    if input_error:
        return input_error

    # each problem is converted to a list, e.g.:
    # "23 + 456" --> [23, '+', 456]
    problems_list = []
    for problem in problems:
        l = []
        l = problem.split()
        l.append(max(len(l[0]), len(l[2])))
        l[0] = int(l[0])
        l[2] = int(l[2])
        problems_list.append(l)

    # building the string with arranged problems line by line
    arranged = ''
    # first line
    for l in problems_list:
        arranged += f'{l[0]:{l[3]+2}d}    '
    arranged = arranged.rstrip() + '\n'
    # second line
    for l in problems_list:
        arranged += f'{l[1]}' + f'{l[2]:{l[3]+1}d}    '
    arranged = arranged.rstrip() + '\n'
    # third line (dashes at the bottom)
    for l in problems_list:
        arranged += '-' * (l[3] + 2) + '    '
    arranged = arranged.rstrip()
    # fourth line: include results if the user asked for it
    if include_results:
        arranged += '\n'
        for l in problems_list:
            arranged += f'{operation(l[0], l[2], l[1]):{l[3]+2}d}    '
        arranged = arranged.rstrip()

    return arranged
