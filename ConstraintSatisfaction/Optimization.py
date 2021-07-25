from scipy import optimize

variables = []

while True:
    inputVar = input('Put your variables here. ENTER without data to exit.   ')
    if inputVar != '':
        variables.append(inputVar)
    else:
        break

varMultipliers = [int(input(f'Coefficient for variable {var}:   ')) for var in variables]

constraints = []

while True:
    inputConstraint = input('Put your constraints here. ENTER without data to exit.   ')
    if inputConstraint != '':
        constraints.append(inputConstraint)
    else:
        break

A_ub = [[input(f'Input coefficient for {var} for constraint {constraint}.   ') for var in variables] for constraint in constraints]

b_ub = [input(f'Insert constraint values for constraint {constraint}.  ') for constraint in constraints]

result = optimize.linprog(
    c = varMultipliers,
    A_ub = A_ub,
    b_ub = b_ub
)

if result.success:
    for var in range(len(result.x)):
        print(f'{round(result.x[var], 2)} of {variables[var]}')
    for constraintNum in range(len(constraints)):
        out = 0
        for coefficient in A_ub[constraintNum]:
            out += result.x[constraintNum] * int(coefficient)
        print(f'{out} of {b_ub[constraintNum]} of {constraints[constraintNum]} used.')
    out = 0
    for var in range(len(result.x)):
        out += variables[var]*varMultipliers[var]
    print(f'{out} points attained.')
else:
    print('No solution.')