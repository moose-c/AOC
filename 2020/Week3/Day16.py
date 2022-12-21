constraints1, my_ticket, tickets1 = open('input.txt').read().split('\n\n')
constraints1, my_ticket, tickets1 = constraints1.split('\n'), my_ticket.split('\n'), tickets1.split('\n')
affoetickets = [[int(line) for line in ticket.split(',')] for ticket in tickets1[1:]]
constraints = []
constraints_names = []
unionconstraints = set()
for con in constraints1:
    l1 = con.split(': ')
    l = [l1[0]] + l1[1].split(' or ')
    bd1, bd2 = l[1].split('-'), l[2].split('-')
    values = [i for i in range(int(bd1[0]), int(bd1[1])+1)] + [i for i in range(int(bd2[0]), int(bd2[1])+1)]
    constraints.append(values)
    constraints_names.append(l[0])
    unionconstraints = unionconstraints.union(values)
####constraints dictionary is gevormd. 
## filter tickets
tickets = []
for ticket in affoetickets:
    bo = True
    for line in ticket:
        if line not in unionconstraints:
            bo = False
            break
    if bo:
        tickets.append(ticket)

def creating_cons_lst(tickets, constraints):
    cons_lst = [[] for i in range(len(constraints))]
    for ticket in tickets:
        for i, char in enumerate(ticket):
            cons_lst[i].append(char)
    return(cons_lst)
# dit werkt ook
values_per_constraint = creating_cons_lst(tickets, constraints)

def fits_constraint(values, constraints, constraints_names):
    possibilities = []
    for i, constraint in enumerate(constraints):
        bo = True
        for value in values:
            if value not in constraint:
                bo = False
        if bo:
            possibilities.append(constraints_names[i])
    return(possibilities)

order = []
for values in values_per_constraint:
    order.append(fits_constraint(values, constraints, constraints_names))

#constraints klopt, values per constraint ook, constraint_names ook.

#value_per_constraint klopt (denk ik...), dank de goden. Nu nog vinden wat wat is. 
values_per_constraint.sort()
values_per_constraint

matr = [[0 for i in range(20)] for i in range(20)]
for i in range(20):
    for j in range(20):
        if constraints_names[j] in order[i]:
            matr[i][j] = 1

i = 0
while True:
    for row in matr:
        if sum(row) == 1:
            for row1 in matr:
                if row1 != row:
                    row1[row.index(1)] = 0
    i+= 1
    if i > 10:
        break

actual_order = []
for row in matr:
    for el in row:
        if el == 1:
            actual_order.append(constraints_names[row.index(el)])

my_numb = my_ticket[1].split(',')

t = (0, 5, 10, 14, 15, 17)
s = 1
for i in t:
    s *= int(my_numb[i])

