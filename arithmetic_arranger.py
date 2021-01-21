def operation(first_op, second_op, operator):
    '''
	Takes two operands and returns their addition
	or subtraction according to operator
	'''
    if operator == '+':
        return first_op + second_op
    else:
        return first_op - second_op


def arithmetic_arranger(problems, include_results=False):

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
			arranged += '-' * (l[3]+2) + '    '
		arranged = arranged.rstrip()
		# include results if the user asked for it
		if include_results:
			arranged += '\n'
			for l in problems_list:
				arranged += f'{operation(l[0], l[2], l[1]):{l[3]+2}d}    '		
			arranged = arranged.rstrip()
		
	return arranged
