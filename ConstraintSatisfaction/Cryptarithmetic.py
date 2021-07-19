import constraint

problem = constraint.Problem()

import constraint
problem = constraint.Problem()
# We're using .addVariables() this time since we're adding
# multiple variables that have the same interval.
problem.addVariables("T", range(1, 10))
problem.addVariables("F", range(1, 10))
problem.addVariables("W", range(10))
problem.addVariables("O", range(10))
problem.addVariables("U", range(10))
problem.addVariables("R", range(10))

def sum_constraint(t, w, o, f, u, r):
    if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
        return True

problem.addConstraint(sum_constraint, "TWOFUR")
problem.addConstraint(constraint.AllDifferentConstraint(), "TWOFUR")

solutions = problem.getSolutions()
print("Number of solutions found: {}\n".format(len(solutions)))

for s in solutions:
    print("T = {}, W = {}, O = {}, F = {}, U = {}, R = {}".format(s['T'], s['W'], s['O'], s['F'], s['U'], s['R']))